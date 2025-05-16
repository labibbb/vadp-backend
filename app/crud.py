from sqlalchemy.orm import Session
from app import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# GET ALL CAMERAS
def get_cameras(db: Session):
    return db.query(models.Camera).all()

# GET CAMERA BY ID
def get_camera(db: Session, cam_id: int):
    return db.query(models.Camera).filter(models.Camera.cam_id == cam_id).first()

# CREATE CAMERA
def create_camera(db: Session, camera: schemas.CameraCreate):
    db_camera = models.Camera(
        cam_rtsp=camera.cam_rtsp,
        cam_status=camera.cam_status,
        cam_creaby=camera.cam_creaby,
        cam_creadate=camera.cam_creadate
    )
    db.add(db_camera)
    db.commit()
    db.refresh(db_camera)
    return db_camera

# UPDATE CAMERA (Menggunakan POST)
def update_camera(db: Session, cam_id: int, camera: schemas.CameraUpdate):
    db_camera = db.query(models.Camera).filter(models.Camera.cam_id == cam_id).first()
    if db_camera:
        db_camera.cam_rtsp = camera.cam_rtsp
        db_camera.cam_status = camera.cam_status
        db_camera.cam_modiby = camera.cam_modiby
        db_camera.cam_modidate = camera.cam_modidate
        db.commit()
        db.refresh(db_camera)
    return db_camera

# DELETE CAMERA (Menggunakan POST)
def delete_camera(db: Session, cam_id: int):
    db_camera = db.query(models.Camera).filter(models.Camera.cam_id == cam_id).first()
    if db_camera:
        db.delete(db_camera)
        db.commit()
    return db_camera

# GET ALL MODELS
def get_models(db: Session):
    return db.query(models.Model).all()

# GET MODEL BY ID
def get_model(db: Session, mod_id: int):
    return db.query(models.Model).filter(models.Model.mod_id == mod_id).first()

# CREATE MODEL
def create_model(db: Session, model: schemas.ModelCreate):
    db_model = models.Model(
        mod_name=model.mod_name,
        mod_file_name=model.mod_file_name,
        mod_status=model.mod_status,
        mod_creaby=model.mod_creaby,
        mod_creadate=model.mod_creadate
    )
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model

# UPDATE MODEL (Menggunakan POST)
def update_model(db: Session, mod_id: int, model: schemas.ModelUpdate):
    db_model = db.query(models.Model).filter(models.Model.mod_id == mod_id).first()
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
    db_model = db.query(models.Model).filter(models.Model.mod_id == mod_id).first()
    if db_model:
        db.delete(db_model)
        db.commit()
    return db_model
