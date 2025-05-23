from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from app.controller import modelController
from app.model import modelModel
from app.schema import modelSchema
from app import database
from typing import List
import shutil
import os
from datetime import date

router = APIRouter()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET MODEL BY ID
@router.get("/models", response_model=List[modelSchema.ModelResponse])
def get_all_models(db: Session = Depends(get_db)):
    return modelController.get_models(db)

# GET MODEL BY ID
@router.get("/models/{mod_id}", response_model=modelSchema.ModelCreate)
def read_model(mod_id: int, db: Session = Depends(get_db)):
    return modelController.get_model(db, mod_id)

@router.post("/models", response_model=modelSchema.ModelCreate)
def create_new_model(
    mod_name: str = Form(...),
    mod_status: int = Form(None),
    mod_creaby: int = Form(None),
    mod_creadate: date = Form(None),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    return modelController.create_model_with_file(
        db, mod_name, mod_status, mod_creaby, mod_creadate, file
    )

# UPDATE MODEL (Menggunakan POST)
@router.patch("/models/{mod_id}")
def update_model(
    mod_id: int,
    mod_name: str = Form(...),
    file: UploadFile = File(None),  # file boleh kosong
    db: Session = Depends(get_db)
):
    updated = modelController.update_model_with_file(db, mod_id, mod_name, file)
    if not updated:
        return {"error": "Model not found"}
    return updated

# DELETE MODEL (Menggunakan POST)
@router.post("/models/{mod_id}/delete")
def delete_existing_model(mod_id: int, db: Session = Depends(get_db)):
    return modelController.delete_model(db, mod_id)
