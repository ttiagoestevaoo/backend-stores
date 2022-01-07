from sqlalchemy.orm import Session

from . import models
from src.models import StoreCreate, TransactionCreate

def get_all_stores(db: Session):
    return db.query(models.Store).all()
    
def get_all_store_transactions(db: Session, store_id: int):
    return db.query(models.Transaction).filter(models.Transaction.store_id == store_id).all()

def get_stores_by_name(db: Session, name: str):
    return db.query(models.Store).filter(models.Store.name==name).all()

def create_store(db: Session, store: StoreCreate):
    db_store = models.Store(owner=store.owner, name=store.name)
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store

def create_transaction(db: Session, transaction: TransactionCreate):
    db_transaction = models.Transaction(
        transaction_type_id=transaction.transaction_type_id, 
        card=transaction.card, 
        cpf=transaction.cpf, 
        created_at=transaction.created_at, 
        time_at=transaction.time_at, 
        amount=transaction.amount,
        store_id=transaction.store_id,
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction