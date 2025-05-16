from sqlalchemy.orm import Session
from app.model import solutionModel
from app.schema import solutionSchema
from app.utils.response import success_response, error_response
import datetime

# GET ALL CAMERAS
def get_solutions(db: Session): 
    return db.query(solutionModel.Solution).all()

# GET BY ID
def get_solution(db: Session, sol_id: int):
    solution = db.query(solutionModel.Solution).filter(solutionModel.Solution.sol_id == sol_id).first()
    if not solution:
        raise HTTPException(status_code=404, detail="Solution not found")
    return solution

# CREATE
def create_solution(db: Session, solution: solutionSchema.SolutionCreate):
    db_solution = solutionModel.Solution(
        sol_name=solution.sol_name,
        sol_camera_amount=solution.sol_camera_amount,
        sol_model_amount=solution.sol_model_amount,
        sol_status=solution.sol_status,
        sol_creaby=solution.sol_creaby,
        sol_creadate=solution.sol_creadate or datetime.date.today()
    )
    db.add(db_solution)
    db.commit()
    db.refresh(db_solution)
    return db_solution

# UPDATE
def update_solution(db: Session, sol_id: int, solution: solutionSchema.SolutionUpdate):
    db_solution = db.query(solutionModel.Solution).filter(solutionModel.Solution.sol_id == sol_id).first()
    if not db_solution:
        raise HTTPException(status_code=404, detail="Solution not found")

    db_solution.sol_name=solution.sol_name
    db_solution.sol_camera_amount=solution.sol_camera_amount
    db_solution.sol_model_amount=solution.sol_model_amount
    db_solution.sol_status=solution.sol_status
    db_solution.sol_modiby = solution.sol_modiby
    db_solution.sol_modidate = solution.sol_modidate or datetime.date.today()

    db.commit()
    db.refresh(db_solution)
    return db_solution

# DELETE
def delete_solution(db: Session, sol_id: int):
    db_solution = db.query(solutionModel.Solution).filter(solutionModel.Solution.sol_id == sol_id).first()
    if not db_solution:
        raise HTTPException(status_code=404, detail="Solution not found")

    db.delete(db_solution)
    db.commit()
    return {"detail": "Solution deleted successfully"}