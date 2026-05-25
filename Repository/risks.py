from Model import model
from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse


def get_all(db:Session):
    try:
        risks =db.query(model.Risk).all()
        if not risks:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Risks Found.")
        result = []
        for risk in risks:
            result.append({
                "risk_id":risk.risk_id,
                "risk_description" : risk.risk_description,
                "risk_priority" : risk.risk_priority,
                "risk_status" : risk.risk_status,
                "risk_allocation" : {
                    "user_id" : risk.user_id,
                    "user_name" : risk.user.user_name,
                    "user_role" : risk.user.user_role,
                    "user_email": risk.user.user_email
                },
                "risk_type" : risk.risk_type
            })

        return result
    except Exception as e:
        return f"{e}"

def get_risks_by_id(db:Session,risk_id:int):
    risk = db.query(model.Risk).filter(model.Risk.risk_id == risk_id).first()
    if not risk:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Risk ID Not Found.")
    result = {
        "risk_id":risk.risk_id,
        "risk_description" : risk.risk_description,
        "risk_priority" : risk.risk_priority,
        "risk_status" : risk.risk_status,
        "risk_allocation" : {
            "user_id" : risk.user_id,
            "user_name" : risk.user.user_name,
            "user_role" : risk.user.user_role
        },
        "risk_type" : risk.risk_type
    }
    return result

def add_risks(db:Session,details):
    try:
        new_risk = model.Risk(
            risk_description = details.risk_description,
            risk_priority = details.risk_priority,
            risk_status = details.risk_status,
            user_id = details.user_id,
            risk_type = details.risk_type
        )
        db.add(new_risk)
        db.commit()
        db.refresh(new_risk)
        return "Details Added."
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{e}")
    

def update_risks(db: Session,risk_id:int,details):
    risk = db.query(model.Risk).filter(model.Risk.risk_id == risk_id).first()
    if not risk:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail= "Risk ID Not Found.")
    updated_risk = details.model_dump(exclude_unset=True)
    for key,value in updated_risk.items():
        setattr(risk,key,value)
    db.commit()
    db.refresh(risk)
    return JSONResponse(status_code=status.HTTP_200_OK,content= "Risk updated successfully.")

def delete_risk(db, risk_id):
    risk = db.query(model.Risk).filter(model.Risk.risk_id == risk_id).first()
    if not risk:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Risk ID Not Found.")
    db.delete(risk)
    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK, content={"Message":"Risk Deleted Successfully", "Risk ID": risk_id})