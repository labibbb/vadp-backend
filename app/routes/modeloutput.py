from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.controller import modeloutputController
from app.model import modelModel
from app.schema import modeloutputSchema
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

# GET BY ID
@router.get("/modeloutput/{mdo_id}", response_model=modeloutputSchema.ModelOutputResponse)
def read_modeloutput(mdo_id: int, db: Session = Depends(get_db)):
    return modeloutputController.get_modeloutput(db, mdo_id)

# GET ALL (Optional)
@router.get("/modeloutput", response_model=List[modeloutputSchema.ModelOutputResponse])
def read_all_modeloutput(db: Session = Depends(get_db)):
    return modeloutputController.get_all_modeloutput(db)

# CREATE
@router.post("/modeloutput", response_model=modeloutputSchema.ModelOutputResponse)
def create_new_modeloutput(modeloutput: modeloutputSchema.ModelOutputCreate, db: Session = Depends(get_db)):
    data = modeloutputController.create_modeloutput(db, modeloutput)
    # Ambil nama modelnya (jika ingin), atau set None
    mdl_name = None
    if data.mdo_model_id:
        mdl = db.query(modelModel.Model).filter(modelModel.Model.mod_id == data.mdo_model_id).first()
        mdl_name = mdl.mod_name if mdl else None
    return {
        "mdo_id": data.mdo_id,
        "mdo_model_id": data.mdo_model_id,
        "mdo_output_name": data.mdo_output_name,
        "mdo_status": data.mdo_status,
        "mdl_name": mdl_name
    }

# UPDATE
@router.post("/modeloutput/{mdo_id}", response_model=modeloutputSchema.ModelOutputResponse)
def update_existing_modeloutput(mdo_id: int, modeloutput: modeloutputSchema.ModelOutputUpdate, db: Session = Depends(get_db)):
    return modeloutputController.update_modeloutput(db, mdo_id, modeloutput)

# DELETE
@router.post("/modeloutput/{mdo_id}")
def delete_existing_modeloutput(mdo_id: int, db: Session = Depends(get_db)):
    return modeloutputController.delete_modeloutput(db, mdo_id)

@router.get("/modeloutput/model/{mdo_model_id}", response_model=List[modeloutputSchema.ModelOutputResponse])
def read_modeloutput_by_modelid(mdo_model_id: int, db: Session = Depends(get_db)):
    return modeloutputController.get_modeloutput_by_modelid(db, mdo_model_id)