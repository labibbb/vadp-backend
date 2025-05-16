from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.controller import modelsolutionController
from app.model import modelsolutionModel
from app.schema import modelsolutionSchema
from app import database

router = APIRouter()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET ALL CAMERAS
# GET CAMERA BY ID
@router.get("/modelsolution/{solution_id}", response_model=modelsolutionSchema.ModelSolutionCreate)
def read_modelsolution(solution_id: int, db: Session = Depends(get_db)):
    return modelsolutionController.get_modelsolution(db, solution_id)

# CREATE CAMERA
@router.post("/modelsolution", response_model=modelsolutionSchema.ModelSolutionCreate)
def create_new_modelsolution(solution: modelsolutionSchema.ModelSolutionCreate, db: Session = Depends(get_db)):
    return modelsolutionController.create_modelsolution(db, solution)

# DELETE CAMERA (Menggunakan POST)
@router.post("/modelsolution/{mds_id}/delete")
def delete_existing_modelsolution(mds_id: int, db: Session = Depends(get_db)):
    return modelsolutionController.delete_modelsolution(db, mds_id)