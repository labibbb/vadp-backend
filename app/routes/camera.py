from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.controller import cameraController
from app.model import cameraModel
from app.schema import cameraSchema
from app import database
from fastapi.responses import StreamingResponse
import cv2

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

@router.get("/cameras/{cam_id}/stream")
def stream_camera(cam_id: int, db: Session = Depends(get_db)):
    # Ambil data kamera (RTSP/IP) dari DB
    camera = cameraController.get_camera(db, cam_id)
    if not camera:
        raise HTTPException(status_code=404, detail="Camera not found")

    # Ambil URL RTSP atau IP
    rtsp_url = camera.cam_rtsp if camera.cam_rtsp != '-' else camera.cam_ip

    # Cek jika ingin akses webcam lokal (input dari DB = '0')
    if str(rtsp_url).strip() == "0":
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(rtsp_url)
    
    if not cap.isOpened():
        raise HTTPException(status_code=500, detail="Failed to open camera stream")

    # Generator MJPEG frame
    def generate():
        while True:
            success, frame = cap.read()
            if not success:
                break
            # Encode JPEG
            ret, jpeg = cv2.imencode('.jpg', frame)
            if not ret:
                continue
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
        cap.release()

    # Streaming MJPEG response
    return StreamingResponse(generate(), media_type='multipart/x-mixed-replace; boundary=frame')