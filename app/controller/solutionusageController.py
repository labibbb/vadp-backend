from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.model import solutionusageModel
from app.schema import solutionusageSchema

# GET ALL
def get_all_solutionusage(db: Session):
    return db.query(solutionusageModel.SolutionUsage).all()

# GET BY ID
def get_solutionusage_by_id(db: Session, slu_id: int):
    result = db.query(solutionusageModel.SolutionUsage).filter(solutionusageModel.SolutionUsage.slu_id == slu_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="SolutionUsage not found")
    return result

# CREATE
def create_solutionusage(db: Session, su: solutionusageSchema.SolutionUsageCreate):
    db_su = solutionusageModel.SolutionUsage(
        slu_solution_id=su.slu_solution_id,
        slu_user_id=su.slu_user_id,
        slu_status=su.slu_status
    )
    db.add(db_su)
    db.commit()
    db.refresh(db_su)
    return db_su

# UPDATE
def update_solutionusage(db: Session, slu_id: int, su: solutionusageSchema.SolutionUsageUpdate):
    db_su = db.query(solutionusageModel.SolutionUsage).filter(solutionusageModel.SolutionUsage.slu_id == slu_id).first()
    if not db_su:
        raise HTTPException(status_code=404, detail="SolutionUsage not found")
    if su.slu_solution_id is not None:
        db_su.slu_solution_id = su.slu_solution_id
    if su.slu_user_id is not None:
        db_su.slu_user_id = su.slu_user_id
    if su.slu_status is not None:
        db_su.slu_status = su.slu_status
    db.commit()
    db.refresh(db_su)
    return db_su

# DELETE
def delete_solutionusage(db: Session, slu_id: int):
    db_su = db.query(solutionusageModel.SolutionUsage).filter(solutionusageModel.SolutionUsage.slu_id == slu_id).first()
    if not db_su:
        raise HTTPException(status_code=404, detail="SolutionUsage not found")
    db.delete(db_su)
    db.commit()
    return {"detail": "SolutionUsage deleted successfully"}
