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

# CREATE MODEL
@router.post("/models", response_model=modelSchema.ModelCreate)
def create_new_model(model: modelSchema.ModelCreate, db: Session = Depends(get_db)):
    return modelController.create_model(db, model)

# UPDATE MODEL (Menggunakan POST)
@router.post("/models/{mod_id}/update", response_model=modelSchema.ModelCreate)
def update_existing_model(mod_id: int, model: modelSchema.ModelUpdate, db: Session = Depends(get_db)):
    return modelController.update_model(db, mod_id, model)

# DELETE MODEL (Menggunakan POST)
@router.post("/models/{mod_id}/delete")
def delete_existing_model(mod_id: int, db: Session = Depends(get_db)):
    return modelController.delete_model(db, mod_id)
