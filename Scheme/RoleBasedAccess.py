from Model.database import get_db
from fastapi import Depends,HTTPException,status
from Scheme.oauth2 import get_current_user

def adminAccess(current_user = Depends(get_current_user)):
    if current_user.user_role != "Admin":
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail= "Only Admins allowed")
    return current_user

def managerAccess(current_user = Depends(get_current_user)):
    if current_user.user_role != "Manager":
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail= "Only Admins allowed")
    return current_user

def employeeAccess(current_user = Depends(get_current_user)):
    if current_user.user_role != "Employee":
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail= "Only Admins allowed")
    return current_user