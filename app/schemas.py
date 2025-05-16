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
    cam_name: str
    cam_rtsp: str
    cam_status: int
    cam_creaby: int
    cam_creadate: date

# Schema untuk UPDATE
class CameraUpdate(BaseModel):
    cam_name: Optional[str] = None
    cam_rtsp: Optional[str] = None
    cam_status: Optional[int] = None
    cam_modiby: Optional[int] = None
    cam_modidate: Optional[date] = None

# Base schema (shared attributes)
class ModelBase(BaseModel):
    mod_name: Optional[str] = None
    mod_file_name: Optional[str] = None
    mod_status: Optional[int] = None

# Create schema
class ModelCreate(ModelBase):
    mod_creaby: Optional[int] = None
    mod_creadate: Optional[date] = None

# Update schema
class ModelUpdate(ModelBase):
    mod_modiby: Optional[int] = None
    mod_modidate: Optional[date] = None

# Response schema (optional but recommended)
class ModelOut(ModelBase):
    mod_id: int
    mod_creaby: Optional[int] = None
    mod_creadate: Optional[date] = None
    mod_modiby: Optional[int] = None
    mod_modidate: Optional[date] = None