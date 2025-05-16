from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.controller import cameraController
from app.model import cameraModel
from app.schema import cameraSchema
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
@router.get("/cameras", response_model=list[cameraSchema.CameraCreate])
def read_cameras(db: Session = Depends(get_db)):
    return cameraController.get_cameras(db)

# GET CAMERA BY ID
@router.get("/cameras/{cam_id}", response_model=cameraSchema.CameraCreate)
def read_camera(cam_id: int, db: Session = Depends(get_db)):
    return cameraController.get_camera(db, cam_id)

# CREATE CAMERA
@router.post("/cameras", response_model=cameraSchema.CameraCreate)
def create_new_camera(camera: cameraSchema.CameraCreate, db: Session = Depends(get_db)):
    return cameraController.create_camera(db, camera)

# UPDATE CAMERA (Menggunakan POST)
@router.post("/cameras/{cam_id}/update", response_model=cameraSchema.CameraCreate)
def update_existing_camera(cam_id: int, camera: cameraSchema.CameraUpdate, db: Session = Depends(get_db)):
    return cameraController.update_camera(db, cam_id, camera)

# DELETE CAMERA (Menggunakan POST)
@router.post("/cameras/{cam_id}/delete")
def delete_existing_camera(cam_id: int, db: Session = Depends(get_db)):
    return cameraController.delete_camera(db, cam_id)

@router.post("/cameras", response_model=cameraSchema.CameraResponse)
def create_new_camera(camera: cameraSchema.CameraCreate, db: Session = Depends(get_db)):
    return cameraController.create_camera(db, camera)
