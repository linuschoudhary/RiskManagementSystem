from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def Intro():
    return {"Message":"Welcome to Risk Management System","Creator": "Sunil Choudhary"}

@router.get("/show")
def showUser():
    return "Users List"

@router.get("/show/{user_id}")
def showUserByUserID(user_id: int):
    return f"here is your user with user ID: {user_id}"

@router.push("/add")
def addUser():
    return "User added successfully"

@router.put("/update/{user_id}")
def updateUser(user_id: int):
    return f"user with user id {user_id} has be updated successfully."

@router.delete("/delete/{user_id}")
def deleteUser(user_id: int):
    return f"user deleted with user id {user_id} successfully."