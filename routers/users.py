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
from Scheme.oauth2 import get_current_user
from Scheme import RoleBasedAccess



get_db = database.get_db

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

# Users
@router.get("/",response_model=List[schema.UserOutput])
def showUser(db: Session = Depends(get_db),current_user : schema.User = Depends(RoleBasedAccess.adminAccess)):
    return users.all_users(db)

@router.get("/{user_id}")
def showUserByUserID(user_id: int,db: Session = Depends(get_db),current_user : schema.User = Depends(get_current_user)):
    return users.user_by_id(db,user_id)

@router.post("/add")
def addUser(details: schema.User,db : Session = Depends(get_db),current_user : schema.User = Depends(RoleBasedAccess.adminAccess)):
    return users.add_user(db, details)
    
@router.put("/update/{user_id}",response_model = schema.UserOutputUpdated)
def updateUser(user_id: int,details : schema.UserUpdate, db: Session = Depends(get_db),current_user : schema.User = Depends(RoleBasedAccess.adminAccess)):
    return users.update_user(db,user_id,details)

@router.delete("/delete/{user_id}")
def deleteUser(user_id: int,db: Session = Depends(get_db),current_user : schema.User = Depends(RoleBasedAccess.adminAccess)):
    return users.delete_user(db, user_id)