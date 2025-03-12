from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET ALL CAMERAS
@router.get("/cameras", response_model=list[schemas.CameraCreate])
def read_cameras(db: Session = Depends(get_db)):
    return crud.get_cameras(db)

# GET CAMERA BY ID
@router.get("/cameras/{camera_id}", response_model=schemas.CameraCreate)
def read_camera(camera_id: int, db: Session = Depends(get_db)):
    return crud.get_camera(db, camera_id)

# CREATE CAMERA
@router.post("/cameras", response_model=schemas.CameraCreate)
def create_new_camera(camera: schemas.CameraCreate, db: Session = Depends(get_db)):
    return crud.create_camera(db, camera)

# UPDATE CAMERA (Menggunakan POST)
@router.post("/cameras/{camera_id}/update", response_model=schemas.CameraCreate)
def update_existing_camera(camera_id: int, camera: schemas.CameraUpdate, db: Session = Depends(get_db)):
    return crud.update_camera(db, camera_id, camera)

# DELETE CAMERA (Menggunakan POST)
@router.post("/cameras/{camera_id}/delete")
def delete_existing_camera(camera_id: int, db: Session = Depends(get_db)):
    return crud.delete_camera(db, camera_id)
