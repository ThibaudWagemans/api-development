#crud.py  # CRUD = Create, Read, Update, Delete

from sqlalchemy.orm import Session
import models
import schemas


def populate_database(db: Session):
    quotes = [
        "The greatest glory in living lies not in never falling, but in rising every time we fall.",
        "The way to get started is to quit talking and begin doing.",
        "Your time is limited, so don't waste it living someone else's life.",
        "If life were predictable it would cease to be life, and be without flavor.",
        "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",
        "Life is what happens when you're busy making other plans.",
        "Spread love everywhere you go. Let no one ever come to you without leaving happier.",
        "When you reach the end of your rope, tie a knot in it and hang on.",
        "Always remember that you are absolutely unique. Just like everyone else.",
        "Don't judge each day by the harvest you reap but by the seeds that you plant.",
        "The future belongs to those who believe in the beauty of their dreams.",
        "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
        "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.",
        "It is during our darkest moments that we must focus to see the light.",
        "Whoever is happy will make others happy too.",
        "Do not go where the path may lead, go instead where there is no path and leave a trail.",
        "You will face many defeats in life, but never let yourself be defeated.",
        "In the end, it's not the years in your life that count. It's the life in your years.",
        "Never let the fear of striking out keep you from playing the game.",
        "Life is either a daring adventure or nothing at all.",
        "Many of life's failures are people who did not realize how close they were to success when they gave up.",
        "You only live once, but if you do it right, once is enough.",
        "Many people think of prosperity that concerns money only to forget that true prosperity is of the mind.",
        "To live a creative life, we must lose our fear of being wrong.",
        "If you are not willing to risk the usual you will have to settle for the ordinary."]
    for quote in quotes:
        db_quote = models.Quote(content=quote)
        db.add(db_quote)
        db.commit()
        db.refresh(db_quote)
    return 0


def get_quote(db: Session, quote_id: int):
    return db.query(models.Quote).filter(models.Quote.id == quote_id).first()


def get_quotes(db: Session, skip: int = 0, limit: int = 25):
    return db.query(models.Quote).offset(skip).limit(limit).all()


def create_quote(db: Session, quote: schemas.QuoteCreate):
    db_quote = models.Quote(content=quote.content)
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote
