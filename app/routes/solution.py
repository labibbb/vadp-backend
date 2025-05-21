from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.controller import solutionController
from app.model import solutionModel
from app.schema import solutionSchema
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
@router.get("/solutions", response_model=list[solutionSchema.SolutionCreate])
def read_solutions(db: Session = Depends(get_db)):
    return solutionController.get_solutions(db)

# GET CAMERA BY ID
@router.get("/solutions/{sol_id}", response_model=solutionSchema.SolutionCreate)
def read_camera(sol_id: int, db: Session = Depends(get_db)):
    return solutionController.get_solution(db, sol_id)

# CREATE CAMERA
@router.post("/solutions", response_model=solutionSchema.SolutionCreate)
def create_new_solutions(solution: solutionSchema.SolutionCreate, db: Session = Depends(get_db)):
    return solutionController.create_solution(db, solution)

# UPDATE CAMERA (Menggunakan POST)
@router.post("/solutions/{sol_id}/update", response_model=solutionSchema.SolutionCreate)
def update_existing_solution(sol_id: int, solution: solutionSchema.SolutionUpdate, db: Session = Depends(get_db)):
    return solutionController.update_solution(db, sol_id, solution)

# DELETE CAMERA (Menggunakan POST)
@router.post("/solutions/{sol_id}/delete")
def delete_existing_solution(sol_id: int, db: Session = Depends(get_db)):
    return solutionController.delete_solution(db, sol_id)
