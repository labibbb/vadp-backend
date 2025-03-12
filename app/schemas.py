from pydantic import BaseModel
from typing import Optional
from datetime import date

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

# Schema untuk CREATE
class CameraCreate(BaseModel):
    camera_rtsp: str
    camera_status: int
    camera_creaby: int
    camera_creadate: date

# Schema untuk UPDATE
class CameraUpdate(BaseModel):
    camera_rtsp: Optional[str] = None
    camera_status: Optional[int] = None
    camera_modiby: Optional[int] = None
    camera_modidate: Optional[date] = None
