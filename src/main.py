from fastapi import FastAPI, Depends, HTTPException
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import crud
# import models
import schemas
from database import get_db, SessionLocal, engine

app = FastAPI()

@app.post('/users', response_model = schemas.UserCreate)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    data = jsonable_encoder(crud.create_user(user=user, db=db))
    return JSONResponse(data)

@app.get('/users/{user_id}')
def read_user(user_id: int ,db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id = user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get('/users')
def read_all_user(db: Session = Depends(get_db)):
    db_user = crud.get_all_user(db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

