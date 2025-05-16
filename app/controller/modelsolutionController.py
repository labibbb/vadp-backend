from sqlalchemy.orm import Session
from app.model import modelsolutionModel
from app.schema import modelsolutionSchema
from app.utils.response import success_response, error_response
import datetime

# GET BY ID
def get_modelsolution(db: Session, solution_id: int):
    modelsolution = db.query(modelsolutionModel.ModelSolution).filter(modelsolutionModel.ModelSolution.mds_solution_id == solution_id).first()
    if not modelsolution:
        raise HTTPException(status_code=404, detail="Detail not found")
    return modelsolution

# CREATE
def create_modelsolution(db: Session, modelsolution: modelsolutionSchema.ModelSolutionCreate):
    db_modelsolution = modelsolutionModel.ModelSolution(
        mds_model_id=modelsolution.mds_model_id,
        mds_solution_id=modelsolution.mds_solution_id,
        mds_statis_id=modelsolution.mds_status,
    )
    db.add(db_modelsolution)
    db.commit()
    db.refresh(db_modelsolution)
    return db_modelsolution

# DELETE
def delete_modelsolution(db: Session, mds_id: int):
    # Cari semua data yang cocok
    solutions = db.query(modelsolutionModel.ModelSolution).filter(
        modelsolutionModel.ModelSolution.mds_solution_id == mds_id
    ).all()

    # Kalau tidak ada data, lempar exception
    if not solutions:
        raise HTTPException(status_code=404, detail="Camera(s) not found")

    # Hapus satu per satu (aman untuk kasus ada foreign key/ORM tracking)
    for sol in solutions:
        db.delete(sol)

    db.commit()
    return {"detail": "Camera(s) deleted successfully"}