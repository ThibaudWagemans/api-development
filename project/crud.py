#crud.py  # CRUD = Create, Read, Update, Delete

from sqlalchemy.orm import Session
import models
import schemas


def get_quote(db: Session, quote_id: int):
    return db.query(models.Quote).filter(models.Quote.id == quote_id).first()


def get_quotes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Quote).offset(skip).limit(limit).all()


def create_quote(db: Session, quote: schemas.QuoteCreate):
    db_quote = models.Quote(content=quote.content)
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote
