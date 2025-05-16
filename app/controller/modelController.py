from sqlalchemy.orm import Session
from app.model import modelModel
from app.schema import modelSchema

# GET ALL MODELS
def get_models(db: Session):
    return db.query(modelModel.Model).all()

# GET MODEL BY ID
def get_model(db: Session, mod_id: int):
    return db.query(modelModel.Model).filter(modelModel.Model.mod_id == mod_id).first()

def create_model(db: Session, model: modelSchema.ModelCreate):
    db_model = modelModel.Model(
        mod_name = model.mod_name,
        mod_file_name = model.mod_file_name,
        mod_status = model.mod_status,
        mod_creaby = model.mod_creaby,
        mod_creadate = model.mod_creadate or datetime.date.today()
    )
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model

# UPDATE MODEL (Menggunakan POST)
def update_model(db: Session, mod_id: int, model: modelSchema.ModelUpdate):
    db_model = db.query(modelModel.Model).filter(modelModel.Model.mod_id == mod_id).first()
    if db_model:
        db_model.mod_name = model.mod_name
        db_model.mod_file_name = model.mod_file_name
        db_model.mod_status = model.mod_status
        db_model.mod_modiby = model.mod_modiby
        db_model.mod_modidate = model.mod_modidate
        db.commit()
        db.refresh(db_model)
    return db_model

# DELETE MODEL (Menggunakan POST)
def delete_model(db: Session, mod_id: int):
    db_model = db.query(modelModel.Model).filter(modelModel.Model.mod_id == mod_id).first()
    if db_model:
        db.delete(db_model)
        db.commit()
    return db_model