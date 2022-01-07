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
