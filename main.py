from fastapi import FastAPI,HTTPException,status,Depends
from fastapi.responses import JSONResponse
from Model import model,database
from Schema import schema
import default
from typing import List
from sqlalchemy import and_
from hashing import Hash
from sqlalchemy.orm import Session
from routers import risks,users
app = FastAPI()

model.Base.metadata.create_all(database.engine)

app.include_router(risks.router)
app.include_router(users.router)


# def get_db():
#     session = database.session
#     try:
#         yield session
#     finally:
#         session.close()

    
# # Introduction
# @app.get("/",tags=['Introduction'])
# def Intro():
#     return {"Message":"Welcome to Risk Management System","Creator": "Sunil Choudhary"}

# @app.post("/")
# def addDefault():
#     default.addALL()
#     return "Default values Added"

# # Risks
# @app.get("/risks",tags=['Risks'],response_model=List[schema.RiskOutput])
# def showRisks(db: Session = Depends(get_db)):
#     try:
#         risks =db.query(model.Risk).all()
#         if not risks:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Risks Found.")
#         result = []
#         for risk in risks:
#             result.append({
#                 "risk_id":risk.risk_id,
#                 "risk_description" : risk.risk_description,
#                 "risk_priority" : risk.risk_priority,
#                 "risk_status" : risk.risk_status,
#                 "risk_allocation" : {
#                     "user_id" : risk.user_id,
#                     "user_name" : risk.user.user_name,
#                     "user_role" : risk.user.user_role,
#                     "user_email": risk.user.user_email
#                 },
#                 "risk_type" : risk.risk_type
#             })

#         return result
#     except Exception as e:
#         return e

# @app.get("/risks/{risk_id}",tags=['Risks'],response_model=schema.RiskOutput)
# def showRiskByRiskID(risk_id: int,db: Session = Depends(get_db)):
#     risk = db.query(model.Risk).filter(model.Risk.risk_id == risk_id).first()
#     if not risk:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Risk ID Not Found.")
#     result = {
#         "risk_id":risk.risk_id,
#         "risk_description" : risk.risk_description,
#         "risk_priority" : risk.risk_priority,
#         "risk_status" : risk.risk_status,
#         "risk_allocation" : {
#             "user_id" : risk.user_id,
#             "user_name" : risk.user.user_name,
#             "user_role" : risk.user.user_role
#         },
#         "risk_type" : risk.risk_type
#     }
#     return result

# @app.post("/risks/add",tags=["Risks"])
# def addRisk(details:schema.Risk,db : Session = Depends(get_db)):
#     try:
#         new_risk = model.Risk(
#             risk_description = details.risk_description,
#             risk_priority = details.risk_priority,
#             risk_status = details.risk_status,
#             user_id = details.user_id,
#             risk_type = details.risk_type
#         )
#         db.add(new_risk)
#         db.commit()
#         db.refresh(new_risk)
#         return "Details Added."
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{e}")

# @app.put("/risks/update/{risk_id}",tags=['Risks'],response_model=schema.RiskOutputUpdated)
# def updateRisk(risk_id: int,details: schema.RiskUpdate,db : Session = Depends(get_db)):
#     risk = db.query(model.Risk).filter(model.Risk.risk_id == risk_id).first()
#     if not risk:
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail= "Risk ID Not Found.")
#     updated_risk = details.model_dump(exclude_unset=True)
#     for key,value in updated_risk.items():
#         setattr(risk,key,value)
#     db.commit()
#     db.refresh(risk)
#     result = showRiskByRiskID(risk_id=risk_id)
#     update = {"update_result": "Updated"}
#     updated_result = {**update,**result}

#     return updated_result

# @app.delete("/risk/delete/{risk_id}",tags=['Risks'])
# def deleteRisk(risk_id:int,db: Session = Depends(get_db)):
#     risk = db.query(model.Risk).filter(model.Risk.risk_id == risk_id).first()
#     if not risk:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Risk ID Not Found.")
#     db.delete(risk)
#     db.commit()
#     return JSONResponse(status_code=status.HTTP_200_OK, content={"Message":"Risk Deleted Successfully", "Risk ID": risk_id})


# # Users
# @app.get("/user",tags=['User'],response_model=List[schema.UserOutput])
# def showUser(db: Session = Depends(get_db)):
#     users = db.query(model.User).all()
#     if not users:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Users Found.")
#     result = []
#     for user in users:
#         result.append({
#             "user_id" : user.user_id,
#             "user_name" : user.user_name,
#             "user_role" : user.user_role,
#             "user_email": user.user_email
#         })
#     return result

# @app.get("/user/{user_id}",tags=['User'],response_model=schema.UserOutput)
# def showUserByUserID(user_id: int,db: Session = Depends(get_db)):
#     user = db.query(model.User).filter(model.User.user_id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Users Found.")
#     result = {
#         "user_id" : user.user_id,
#         "user_name" : user.user_name,
#         "user_role" : user.user_role,
#         "user_email": user.user_email
#     }
#     return result

# @app.post("/user/add",tags=['User'])
# def addUser(details: schema.User,db : Session = Depends(get_db)):
#     try:
#         new_user = model.User(
#             user_name = details.user_name,
#             user_role = details.user_role,
#             user_email = details.user_email,
#             user_password = Hash.bcryptPassword(details.user_password)
#         )

#         db.add(new_user)
#         db.commit()
#         db.refresh(new_user)
#         id = db.query(model.User).filter(and_(model.User.user_email == details.user_email, model.User.user_name == details.user_name)).first().user_id
#         return JSONResponse(status_code=status.HTTP_200_OK,content = f"User added successfully and user ID is allocated is: {id}")
#     except Exception as e:
#         raise HTTPException(status_code=status.WS_1007_INVALID_FRAME_PAYLOAD_DATA,details = "Please Fill Required Field Email, Name and Password.")
    
# @app.put("/user/update/{user_id}",tags=['User'],response_model = schema.UserOutputUpdated)
# def updateUser(user_id: int,details : schema.UserUpdate, db: Session = Depends(get_db)):
#     user = db.query(model.User).filter(model.User.user_id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User not found for user id {user_id}")
#     updated_user = details.model_dump(exclude_unset=True)
#     for key,value in updated_user.items():
#         setattr(user,key,value)
#     db.commit()
#     db.refresh(user)
#     result = showUserByUserID(user_id = user_id)
#     update = {"update_status": "Updated"}
#     updated_result= {**update, **result}
#     return updated_result

# @app.delete("/user/delete/{user_id}",tags=['User'])
# def deleteUser(user_id: int,db: Session = Depends(get_db)):
#     user = db.query(model.User).filter(model.User.user_id==user_id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found")
#     db.delete(user)
#     db.commit()
#     return JSONResponse(status_code=status.HTTP_200_OK,content={"Message": "Deleted Successfully","User ID": user_id})