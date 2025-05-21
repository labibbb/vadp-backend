from sqlalchemy.orm import Session
from app.model import camerasolutionModel  # <-- ganti nama model
from app.schema import camerasolutionSchema
from fastapi import HTTPException

# GET by solution_usage_id
def get_camerasolution_by_solution_usage_id(db: Session, solution_usage_id: int):
    results = (
        db.query(camerasolutionModel.CameraSolution)
        .filter(camerasolutionModel.CameraSolution.cms_solution_usage_id == solution_usage_id)
        .all()
    )

    if not results:
        raise HTTPException(status_code=404, detail="Detail not found")

    # Langsung return list of ORM, bisa otomatis serialize jika pakai response_model Pydantic (orm_mode)
    return results

def create_camerasolution(db: Session, cs: camerasolutionSchema.CameraSolutionCreate):
    db_camerasolution = camerasolutionModel.CameraSolution(
        cms_camera_id=cs.cms_camera_id,
        cms_solution_usage_id=cs.cms_solution_usage_id,
        cms_status=cs.cms_status,
    )
    db.add(db_camerasolution)
    db.commit()
    db.refresh(db_camerasolution)
    return db_camerasolution

def delete_camerasolution(db: Session, cms_id: int):
    solution = db.query(camerasolutionModel.CameraSolution).filter(
        camerasolutionModel.CameraSolution.cms_id == cms_id
    ).first()

    if not solution:
        raise HTTPException(status_code=404, detail="Camera Solution not found")

    db.delete(solution)
    db.commit()
    return {"detail": "Camera Solution deleted successfully"}

def delete_all_camerasolution_by_usage(db: Session, solution_usage_id: int):
    solutions = db.query(camerasolutionModel.CameraSolution).filter(
        camerasolutionModel.CameraSolution.cms_solution_usage_id == solution_usage_id
    ).all()

    if not solutions:
        raise HTTPException(status_code=404, detail="Camera Solution(s) not found")

    for sol in solutions:
        db.delete(sol)

    db.commit()
    return {"detail": "Camera Solution(s) deleted successfully"}

