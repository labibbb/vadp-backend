from pydantic import BaseModel
from typing import Optional
from datetime import date

# Schema untuk CREATE
class UserCreate(BaseModel):
    usr_id: int
    usr_username: Optional[str]
    usr_password: Optional[str]
    usr_name: Optional[str]
    usr_role: Optional[int]
    usr_status: Optional[int]
    usr_creaby: Optional[int]
    usr_creadate: Optional[date]

# Schema untuk UPDATE
class UserUpdate(BaseModel):
    usr_username: Optional[str] = None
    usr_password: Optional[str] = None
    usr_name: Optional[str] = None
    usr_role: Optional[int] = None
    usr_status: Optional[int] = None
    usr_modiby: Optional[int] = None
    usr_modidate: Optional[date] = None

class UserResponse(BaseModel):
    usr_id: int
    usr_username: Optional[str]
    usr_password: Optional[str]
    usr_name: Optional[str]
    usr_role: Optional[int]
    usr_status: Optional[int]
    usr_creaby: Optional[int]
    usr_creadate: Optional[date]
    usr_modiby: Optional[int]
    usr_modidate: Optional[date]

    class Config:
        orm_mode = True

