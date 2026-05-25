from fastapi import APIRouter
from main import get_db
from fastapi import HTTPException,status,Depends
from fastapi.responses import JSONResponse
from Model import model,database
from Schema import schema
from typing import List
from sqlalchemy import and_
from hashing import Hash
from sqlalchemy.orm import Session

get_db = database.get_db()

router = APIRouter()

# Users
@router.get("/user",tags=['User'],response_model=List[schema.UserOutput])
def showUser(db: Session = Depends(get_db)):
    users = db.query(model.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Users Found.")
    result = []
    for user in users:
        result.append({
            "user_id" : user.user_id,
            "user_name" : user.user_name,
            "user_role" : user.user_role,
            "user_email": user.user_email
        })
    return result

@router.get("/user/{user_id}",tags=['User'],response_model=schema.UserOutput)
def showUserByUserID(user_id: int,db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Users Found.")
    result = {
        "user_id" : user.user_id,
        "user_name" : user.user_name,
        "user_role" : user.user_role,
        "user_email": user.user_email
    }
    return result

@router.post("/user/add",tags=['User'])
def addUser(details: schema.User,db : Session = Depends(get_db)):
    try:
        new_user = model.User(
            user_name = details.user_name,
            user_role = details.user_role,
            user_email = details.user_email,
            user_password = Hash.bcryptPassword(details.user_password)
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        id = db.query(model.User).filter(and_(model.User.user_email == details.user_email, model.User.user_name == details.user_name)).first().user_id
        return JSONResponse(status_code=status.HTTP_200_OK,content = f"User added successfully and user ID is allocated is: {id}")
    except Exception as e:
        raise HTTPException(status_code=status.WS_1007_INVALID_FRAME_PAYLOAD_DATA,details = "Please Fill Required Field Email, Name and Password.")
    
@router.put("/user/update/{user_id}",tags=['User'],response_model = schema.UserOutputUpdated)
def updateUser(user_id: int,details : schema.UserUpdate, db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User not found for user id {user_id}")
    updated_user = details.model_dump(exclude_unset=True)
    for key,value in updated_user.items():
        setattr(user,key,value)
    db.commit()
    db.refresh(user)
    result = showUserByUserID(user_id = user_id)
    update = {"update_status": "Updated"}
    updated_result= {**update, **result}
    return updated_result

@router.delete("/user/delete/{user_id}",tags=['User'])
def deleteUser(user_id: int,db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.user_id==user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found")
    db.delete(user)
    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK,content={"Message": "Deleted Successfully","User ID": user_id})