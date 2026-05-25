from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    user_name : str
    user_role : Optional[str] = None
    user_email : str
    user_password : str

class UserUpdate(BaseModel):
    user_name : Optional[str] = None
    user_role : Optional[str] = None
    user_email : Optional[str] = None
    user_password : Optional[str] = None

class Risk(BaseModel):
    risk_description : str
    risk_priority : str
    risk_status : str
    user_id : int
    risk_type: str

class RiskUpdate(BaseModel):
    risk_description : Optional[str] = None
    risk_priority : Optional[str] = None
    risk_status : Optional[str] = None
    user_id : Optional[int] = None
    risk_type: Optional[str] = None


class UserOutput(BaseModel):
    user_id : int
    user_name : str
    user_role : str
    user_email: str

    model_config = {"from_attributes": True}

class RiskOutput(BaseModel):
    risk_id : int
    risk_description : str
    risk_priority: str
    risk_status : str
    risk_allocation : UserOutput
    risk_type : str
    model_config = {"from_attributes": True}

class RiskOutputUpdated(BaseModel):
    update_result : str
    risk_id : int
    risk_description : str
    risk_priority: str
    risk_status : str
    risk_allocation : UserOutput
    risk_type : str
    model_config = {"from_attributes": True}

class UserOutputUpdated(BaseModel):
    update_result : str
    user_id : int
    user_name : str
    user_role : str
    user_email: str

    model_config = {"from_attributes": True}

class Login(BaseModel):
    user_email:str
    password:str

class Token(BaseModel):
    access_token : str
    token_data : str = "bearer"

class TokenData(BaseModel):
    user_email : str | None = None