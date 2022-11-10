#crud.py

import requests
from sqlalchemy.orm import Session
import models
import schemas


# get quote from API
def call_api(url: str):
    response = requests.get('https://officeapi.dev/api/quotes/random')
    return response.json()['data']['content']

# populate database with quotes from API
def populate_database(db: Session):
    for i in range(0, 20):
        quote = call_api('https://officeapi.dev/api/quotes/random')
        db_quote = models.Quote(content=quote)
        db.add(db_quote)
        db.commit()
        db.refresh(db_quote)
    return "INFO:     Database populated!"


def create_quote(db: Session, quote: schemas.QuoteCreate):
    db_quote = models.Quote(content=quote.content)
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote


def get_quote(db: Session, quote_id: int):
    return db.query(models.Quote).filter(models.Quote.id == quote_id).first()


def get_quotes(db: Session, skip: int = 0, limit: int = 25):
    return db.query(models.Quote).offset(skip).limit(limit).all()


def get_quote_last(db: Session):
    db_quote = db.query(models.Quote).all()
    quote = db_quote[-1]
    return quote