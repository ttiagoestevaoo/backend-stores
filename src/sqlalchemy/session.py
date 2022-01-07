from .database import SessionLocal

# Dependency
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
