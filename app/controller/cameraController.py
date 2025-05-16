from sqlalchemy.orm import Session
from app.model import cameraModel
from app.schema import cameraSchema
from app.utils.response import success_response, error_response
import datetime

# GET ALL CAMERAS
def get_cameras(db: Session): 
    return db.query(cameraModel.Camera).all()

# GET BY ID
def get_camera(db: Session, cam_id: int):
    camera = db.query(cameraModel.Camera).filter(cameraModel.Camera.cam_id == cam_id).first()
    if not camera:
        raise HTTPException(status_code=404, detail="Camera not found")
    return camera

# CREATE
def create_camera(db: Session, camera: cameraSchema.CameraCreate):
    db_camera = cameraModel.Camera(
        cam_name=camera.cam_name,
        cam_ip=camera.cam_ip,
        cam_rtsp=camera.cam_rtsp,
        cam_status=camera.cam_status,
        cam_creaby=camera.cam_creaby,
        cam_creadate=camera.cam_creadate or datetime.date.today()
    )
    db.add(db_camera)
    db.commit()
    db.refresh(db_camera)
    return db_camera

# UPDATE
def update_camera(db: Session, cam_id: int, camera: cameraSchema.CameraUpdate):
    db_camera = db.query(cameraModel.Camera).filter(cameraModel.Camera.cam_id == cam_id).first()
    if not db_camera:
        raise HTTPException(status_code=404, detail="Camera not found")

    db_camera.cam_name = camera.cam_name
    db_camera.cam_ip = camera.cam_ip
    db_camera.cam_rtsp = camera.cam_rtsp
    db_camera.cam_status = camera.cam_status
    db_camera.cam_modiby = camera.cam_modiby
    db_camera.cam_modidate = camera.cam_modidate or datetime.date.today()

    db.commit()
    db.refresh(db_camera)
    return db_camera

# DELETE
def delete_camera(db: Session, cam_id: int):
    db_camera = db.query(cameraModel.Camera).filter(cameraModel.Camera.cam_id == cam_id).first()
    if not db_camera:
        raise HTTPException(status_code=404, detail="Camera not found")

    db.delete(db_camera)
    db.commit()
    return {"detail": "Camera deleted successfully"}