from datetime import datetime, time, date
from typing import List
from pydantic import BaseModel

class TransactionType(BaseModel):
    id: int
    name: str
    symbol: str
    is_enter: bool
    class Config:
        orm_mode=True

class TransactionBase(BaseModel):
    created_at: date
    amount: float
    cpf: int
    card: str
    time_at: time
    store_id: int

class TransactionCreate(TransactionBase):
    transaction_type_id: int
    
    pass

class Transaction(TransactionBase):
    id: int
    transaction_type: TransactionType

    class Config:
        orm_mode=True



class TransactionFile(BaseModel):
    status : bool
    created_at: str


class StoreBase(BaseModel):
    owner: str
    name: str

class StoreCreate(StoreBase):
    pass

class Store(StoreBase):
    id: int
    transactions: List[Transaction] = []

    class Config:
        orm_mode=True