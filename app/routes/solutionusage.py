from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schema import solutionusageSchema
from app.controller import solutionusageController
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
# GET ALL
@router.get("/solutionusage", response_model=list[solutionusageSchema.SolutionUsageResponse])
def get_all_solutionusage(db: Session = Depends(get_db)):
    return solutionusageController.get_all_solutionusage(db)

# GET BY ID
@router.get("/solutionusage/{slu_id}", response_model=solutionusageSchema.SolutionUsageResponse)
def get_solutionusage_by_id(slu_id: int, db: Session = Depends(get_db)):
    return solutionusageController.get_solutionusage_by_id(db, slu_id)

# CREATE
@router.post("/solutionusage", response_model=solutionusageSchema.SolutionUsageResponse)
def create_solutionusage(su: solutionusageSchema.SolutionUsageCreate, db: Session = Depends(get_db)):
    return solutionusageController.create_solutionusage(db, su)

# UPDATE
@router.post("/solutionusage/{slu_id}/update", response_model=solutionusageSchema.SolutionUsageResponse)
def update_solutionusage(slu_id: int, su: solutionusageSchema.SolutionUsageUpdate, db: Session = Depends(get_db)):
    return solutionusageController.update_solutionusage(db, slu_id, su)

# DELETE
@router.post("/solutionusage/{slu_id}/delete")
def delete_solutionusage(slu_id: int, db: Session = Depends(get_db)):
    return solutionusageController.delete_solutionusage(db, slu_id)