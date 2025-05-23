import os
from datetime import datetime, date
from typing import Optional
from fastapi import UploadFile
from sqlalchemy.orm import Session
from app.model import modelModel
from app.schema import modelSchema

UPLOAD_DIR = "uploads"

def create_model_with_file(db: Session, mod_name: str, mod_status: int, mod_creaby: int, mod_creadate: date, file: UploadFile):
    # Buat folder upload jika belum ada
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # Buat nama file baru: mod_name + tanggal (YYYYMMDD_HHMMSS) + ekstensi asli
    now_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_ext = os.path.splitext(file.filename)[1]
    file_name = f"{mod_name}_{now_str}{file_ext}"

    # Simpan file
    file_path = os.path.join(UPLOAD_DIR, file_name)
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    # Simpan ke DB
    db_model = modelModel.Model(
        mod_name=mod_name,
        mod_file_name=file_name,
        mod_status=mod_status,
        mod_creaby=mod_creaby,
        mod_creadate=mod_creadate or datetime.date.today()
    )
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model

def update_model_with_file(db: Session, mod_id: int, mod_name: str, file: Optional[UploadFile] = None):
    db_model = db.query(modelModel.Model).filter(modelModel.Model.mod_id == mod_id).first()
    if not db_model:
        return None

    db_model.mod_name = mod_name
    db_model.mod_modidate = date.today()  # update last modified date

    # Jika ada file baru yang dikirim
    if file and file.filename:
        now_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_ext = os.path.splitext(file.filename)[1]
        file_name = f"{mod_name}_{now_str}{file_ext}"
        file_path = os.path.join(UPLOAD_DIR, file_name)

        os.makedirs(UPLOAD_DIR, exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        # Optional: hapus file lama (kalau mau)
        if db_model.mod_file_name:
            old_path = os.path.join(UPLOAD_DIR, db_model.mod_file_name)
            if os.path.exists(old_path):
                os.remove(old_path)

        db_model.mod_file_name = file_name  # update nama file baru

    db.commit()
    db.refresh(db_model)
    return db_model

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