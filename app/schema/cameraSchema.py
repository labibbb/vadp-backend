from pydantic import BaseModel
from typing import Optional
from datetime import date

# Schema untuk CREATE
class CameraCreate(BaseModel):
    cam_id: int
    cam_name: Optional[str]
    cam_ip: Optional[str]
    cam_rtsp: Optional[str]
    cam_status: Optional[int]
    cam_creaby: Optional[int]
    cam_creadate: Optional[date]

# Schema untuk UPDATE
class CameraUpdate(BaseModel):
    cam_name: Optional[str] = None
    cam_ip: Optional[str] = None
    cam_rtsp: Optional[str] = None
    cam_status: Optional[int] = None
    cam_modiby: Optional[int] = None
    cam_modidate: Optional[date] = None


class CameraResponse(BaseModel):
    cam_id: int
    cam_name: Optional[str]
    cam_rtsp: Optional[str]
    cam_status: Optional[int]
    cam_creaby: Optional[int]
    cam_creadate: Optional[date]
    cam_modiby: Optional[int]
    cam_modidate: Optional[date]

    class Config:
        orm_mode = True