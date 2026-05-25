from fastapi import APIRouter

router = APIRouter()

@router.get("/risks")
def showRisks():
    return "Here is the list of all the risks."

@router.get("/risks/{risk_id}")
def showRiskByRiskID(risk_id: int):
    return f"risk with risk id {risk_id}"

@router.put("/risks/update/{risk_id}")
def updateRisk(risk_id: int):
    return f"risk updated with id {risk_id}"

@router.delete("/risk/delete/{risk_id}")
def deleteRisk(risk_id:int):
    return f"risk deleted with id {risk_id}"