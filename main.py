from datetime import datetime
from fastapi import Depends, FastAPI, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from src.models import Store, StoreCreate, Transaction, TransactionCreate
from src.sqlalchemy.crud import create_store, create_transaction, get_all_store_transactions, get_all_stores, get_stores_by_name
from src.sqlalchemy.database import SessionLocal

app = FastAPI()


origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/stores/")
async def post_store(store: StoreCreate, db: Session = Depends(get_db)):
    return create_store(db, store)

@app.get("/stores/", response_model=List[Store])
async def get_stores(db: Session = Depends(get_db)):
    stores = get_all_stores(db)
    return stores

@app.get("/stores/{store_id}/transactions/", response_model=List[Transaction])
async def get_store_transactions( store_id : int, db: Session = Depends(get_db)):
    return get_all_store_transactions(db, store_id)

@app.post("/transactions/upload/")
async def create_upload_file(db: Session = Depends(get_db), file: UploadFile = File(...)):
    try:
        lines = (await file.read()).decode("utf-8").split("\n")
        for line in lines:

            transaction_type_id  = line[0:1].strip()
            created_at = line[1:9].strip()
            amount = line[9:19].strip()
            cpf= line[19:30].strip()
            card= line[30:42].strip()
            time_at= line[42:48].strip()
            owner= line[48:62].strip()
            store= line[62:81].strip()

            stores = get_stores_by_name(db, name=store)
            if not stores:
                store = create_store(db, StoreCreate(name=store, owner=owner))
            else:
                store = stores[0]
            print(store)
            create_transaction(db, TransactionCreate(
                transaction_type_id  = transaction_type_id,
                created_at = datetime.strptime(created_at, "%Y%m%d").strftime("%Y-%m-%d"),
                amount = amount,
                cpf= cpf,
                card= card,
                time_at= datetime.strptime(time_at, "%H%M%S").strftime("%H:%M:%S"),
                store_id=store.id
            ))

        return {"filename": file.filename}
    except Exception:
        raise HTTPException(status_code=422, detail="Não foi possivel importar os dados desse arquivo")

