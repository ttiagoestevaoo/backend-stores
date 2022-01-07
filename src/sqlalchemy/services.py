
from .database import Base
from sqlalchemy.orm import Session

class Service:
    model : Base

    def get_all(self, db : Session):
        return db.query(self.model).all()


    def create(self, db: Session, store):
        db_store = self.model(owner=store.owner, name=store.name)
        db.add(db_store)
        db.commit()
        db.refresh(db_store)
        return db_store