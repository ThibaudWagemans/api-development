#main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import os
import random

import crud, models, schemas
from database import SessionLocal, engine

# make database dir if it doesn't exist
if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

# create tables in database 'sqlitedata.db' (check datapase.py database-URL)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# make database session/connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# allowed origins for CORS
origins = ["*"]

# add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"]
)

# populate database with quotes on startup
@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    print(crud.populate_database(db))

# Create custom quote
@app.post("/quotes/", response_model=schemas.Quote)
async def create_quote(quote: schemas.QuoteCreate, db: Session = Depends(get_db)):
    new_quote = crud.create_quote(db=db, quote=quote)
    return new_quote

# GET all quotes
@app.get("/quotes/all", response_model=list[schemas.Quote])
async def read_quotes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    quotes = crud.get_quotes(db, skip=skip, limit=limit)
    return quotes

# GET random quote
@app.get("/quotes/random", response_model=schemas.Quote)
async def read_quote_random(db: Session = Depends(get_db)):
    quotes = crud.get_quotes(db)
    quote = random.choice(quotes)
    return quote

# GET last quote
@app.get("/quotes/last", response_model=schemas.Quote)
async def read_quote_last(db: Session = Depends(get_db)):
    quote = crud.get_quote_last(db)
    return quote
