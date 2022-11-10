#main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine
import os
import random

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

# create tables in database 'sqlitedata.db' (check datapase.py database-URL)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency (to create a new database session for each request)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# populate database with quotes
@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    crud.populate_database(db)

# Create quote
@app.post("/quotes/", response_model=schemas.Quote)
def create_quote(quote: schemas.QuoteCreate, db: Session = Depends(get_db)):
    return crud.create_quote(db=db, quote=quote)

# GET alle quotes
@app.get("/quotes/all", response_model=list[schemas.Quote])
def read_quotes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    quotes = crud.get_quotes(db, skip=skip, limit=limit)
    return quotes

# GET random quote
@app.get("/quotes/random", response_model=schemas.Quote)
def read_quote_random(db: Session = Depends(get_db)):
    quotes = crud.get_quotes(db)
    quote = random.choice(quotes)
    return quote


# GET last quote
@app.get("/quotes/last", response_model=schemas.Quote)
def read_quote_last(db: Session = Depends(get_db)):
    all_quotes = crud.get_quotes(db)
    quote = all_quotes[-1]
    return quote
