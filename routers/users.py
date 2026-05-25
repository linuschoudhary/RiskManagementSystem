from fastapi import APIRouter
from fastapi import HTTPException,status,Depends
from fastapi.responses import JSONResponse
from Model import model,database
from Schema import schema
from typing import List
from sqlalchemy import and_
from hashing import Hash
from sqlalchemy.orm import Session
from Repository import users



get_db = database.get_db

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

# Users
@router.get("/",response_model=List[schema.UserOutput])
def showUser(db: Session = Depends(get_db)):
    return users.all_users(db)

@router.get("/{user_id}")
def showUserByUserID(user_id: int,db: Session = Depends(get_db)):
    return users.user_by_id(db,user_id)

@router.post("/add")
def addUser(details: schema.User,db : Session = Depends(get_db)):
    return users.add_user(db, details)
    
@router.put("/update/{user_id}",response_model = schema.UserOutputUpdated)
def updateUser(user_id: int,details : schema.UserUpdate, db: Session = Depends(get_db)):
    return users.update_user(db,user_id,details)

@router.delete("/delete/{user_id}")
def deleteUser(user_id: int,db: Session = Depends(get_db)):
    return users.delete_user(db, user_id)