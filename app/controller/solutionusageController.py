from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.model import solutionusageModel, solutionModel
from app.schema import solutionusageSchema

# GET ALL
def get_all_solutionusage(db: Session):
    # Join ke table Solution
    results = (
        db.query(
            solutionusageModel.SolutionUsage.slu_id,
            solutionusageModel.SolutionUsage.slu_solution_id,
            solutionusageModel.SolutionUsage.slu_user_id,
            solutionusageModel.SolutionUsage.slu_status,
            solutionModel.Solution.sol_name
        )
        .outerjoin(
            solutionModel.Solution,
            solutionusageModel.SolutionUsage.slu_solution_id == solutionModel.Solution.sol_id
        )
        .all()
    )
    # Konversi ke dict list
    return [
        {
            "slu_id": row.slu_id,
            "slu_solution_id": row.slu_solution_id,
            "slu_user_id": row.slu_user_id,
            "slu_status": row.slu_status,
            "sol_name": row.sol_name
        }
        for row in results
    ]

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

    # Ambil data solution_name & sol_id via join
    solution = db.query(solutionModel.Solution).filter(solutionModel.Solution.sol_id == db_su.slu_solution_id).first()
    sol_name = solution.sol_name if solution else None
    sol_id = solution.sol_id if solution else None

    return {
        "slu_id": db_su.slu_id,
        "slu_solution_id": db_su.slu_solution_id,
        "slu_user_id": db_su.slu_user_id,
        "slu_status": db_su.slu_status,
        "sol_id": sol_id,
        "sol_name": sol_name
    }

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
    
    # --- Join ke tabel Solution untuk ambil sol_name
    sol = db.query(solutionModel.Solution).filter(solutionModel.Solution.sol_id == db_su.slu_solution_id).first()
    sol_name = sol.sol_name if sol else None

    # --- Return dict response (supaya konsisten seperti create)
    return {
        "slu_id": db_su.slu_id,
        "slu_solution_id": db_su.slu_solution_id,
        "slu_user_id": db_su.slu_user_id,
        "slu_status": db_su.slu_status,
        "sol_name": sol_name,
    }

# DELETE
def delete_solutionusage(db: Session, slu_id: int):
    db_su = db.query(solutionusageModel.SolutionUsage).filter(solutionusageModel.SolutionUsage.slu_id == slu_id).first()
    if not db_su:
        raise HTTPException(status_code=404, detail="SolutionUsage not found")
    db.delete(db_su)
    db.commit()
    return {"detail": "SolutionUsage deleted successfully"}
