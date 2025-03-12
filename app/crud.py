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
def get_camera(db: Session, camera_id: int):
    return db.query(models.Camera).filter(models.Camera.camera_id == camera_id).first()

# CREATE CAMERA
def create_camera(db: Session, camera: schemas.CameraCreate):
    db_camera = models.Camera(
        camera_rtsp=camera.camera_rtsp,
        camera_status=camera.camera_status,
        camera_creaby=camera.camera_creaby,
        camera_creadate=camera.camera_creadate
    )
    db.add(db_camera)
    db.commit()
    db.refresh(db_camera)
    return db_camera

# UPDATE CAMERA (Menggunakan POST)
def update_camera(db: Session, camera_id: int, camera: schemas.CameraUpdate):
    db_camera = db.query(models.Camera).filter(models.Camera.camera_id == camera_id).first()
    if db_camera:
        db_camera.camera_rtsp = camera.camera_rtsp
        db_camera.camera_status = camera.camera_status
        db_camera.camera_modiby = camera.camera_modiby
        db_camera.camera_modidate = camera.camera_modidate
        db.commit()
        db.refresh(db_camera)
    return db_camera

# DELETE CAMERA (Menggunakan POST)
def delete_camera(db: Session, camera_id: int):
    db_camera = db.query(models.Camera).filter(models.Camera.camera_id == camera_id).first()
    if db_camera:
        db.delete(db_camera)
        db.commit()
    return db_camera