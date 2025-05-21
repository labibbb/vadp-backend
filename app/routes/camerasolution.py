from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schema import camerasolutionSchema
from app.controller import camerasolutionController
from app import database
from typing import List

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
@router.get("/camerasolution/{solution_usage_id}", response_model=list[camerasolutionSchema.CameraSolutionResponse])
def get_by_usage(solution_usage_id: int, db: Session = Depends(get_db)):
    return camerasolutionController.get_camerasolution_by_solution_usage_id(db, solution_usage_id)

@router.post("/camerasolution", response_model=camerasolutionSchema.CameraSolutionResponse)
def create(cs: camerasolutionSchema.CameraSolutionCreate, db: Session = Depends(get_db)):
    return camerasolutionController.create_camerasolution(db, cs)

@router.post("/camerasolution/{cms_id}")
def delete(cms_id: int, db: Session = Depends(get_db)):
    return camerasolutionController.delete_camerasolution(db, cms_id)