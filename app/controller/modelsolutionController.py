from sqlalchemy.orm import Session
from app.model import modelsolutionModel, modelModel
from app.schema import modelsolutionSchema
from app.utils.response import success_response, error_response
import datetime

# GET BY ID
def get_modelsolution(db: Session, solution_id: int):
    results = (
        db.query(
            modelsolutionModel.ModelSolution.mds_id,
            modelsolutionModel.ModelSolution.mds_model_id,
            modelsolutionModel.ModelSolution.mds_solution_id,
            modelsolutionModel.ModelSolution.mds_status,
            modelModel.Model.mod_name
        )
        .join(modelModel.Model, modelsolutionModel.ModelSolution.mds_model_id == modelModel.Model.mod_id)
        .filter(modelsolutionModel.ModelSolution.mds_solution_id == solution_id)
        .all()
    )

    if not results:
        raise HTTPException(status_code=404, detail="Detail not found")

    # Konversi manual ke dict agar cocok dengan response_model
    response = []
    for row in results:
        response.append({
            "mds_id": row.mds_id,
            "mds_model_id": row.mds_model_id,
            "mds_solution_id": row.mds_solution_id,
            "mds_status": row.mds_status,
            "mdl_name": row.mod_name
        })

    return response

# CREATE
def create_modelsolution(db: Session, modelsolution: modelsolutionSchema.ModelSolutionCreate):
    db_modelsolution = modelsolutionModel.ModelSolution(
        mds_model_id=modelsolution.mds_model_id,
        mds_solution_id=modelsolution.mds_solution_id,
        mds_status=modelsolution.mds_status,
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