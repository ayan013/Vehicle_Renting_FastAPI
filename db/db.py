from sqlmodel import create_engine, Session
from core.config import settings

DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL,echo=True)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()