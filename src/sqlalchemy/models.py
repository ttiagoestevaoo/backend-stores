from sqlalchemy.sql.functions import char_length
from sqlalchemy.sql.sqltypes import Boolean
from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time, Float, BigInteger


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String)
    name = Column(String, unique=True)

    transactions = relationship("Transaction", back_populates="store")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(Date)
    time_at = Column(Time(timezone=True))
    store_id = Column(Integer, ForeignKey("stores.id"))
    amount = Column(Float)
    cpf = Column(BigInteger)
    card = Column(String)
    transaction_type_id = Column(Integer, ForeignKey("transaction_types.id"))
    transaction_type = relationship("TransactionType", back_populates="transactions")

    store = relationship("Store", back_populates="transactions")

class TransactionType(Base):
    __tablename__ = "transaction_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    symbol = Column(String)
    is_enter = Column(Boolean)

    transactions = relationship("Transaction", back_populates="transaction_type")
