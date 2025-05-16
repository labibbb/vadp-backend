from pydantic import BaseModel
from typing import Optional
from datetime import date

# Create schema
class SolutionCreate(BaseModel):
    sol_id: int
    sol_name: Optional[str]
    sol_camera_amount: Optional[int]
    sol_model_amount: Optional[int]
    sol_status: Optional[int]
    sol_creaby: Optional[int]
    sol_creadate: Optional[date]

# Update schema
class SolutionUpdate(BaseModel):
    sol_name: Optional[str] = None
    sol_camera_amount: Optional[int] = None
    sol_model_amount: Optional[int] = None
    sol_status: Optional[int] = None
    sol_modiby: Optional[int] = None
    sol_modidate: Optional[date] = None

# Response schema (optional but recommended)
class SolutionResponse(BaseModel):
    sol_id: int
    sol_name: Optional[str]
    sol_camera_amount: Optional[int]
    sol_model_amount: Optional[int]
    sol_status: Optional[int]
    sol_creaby: Optional[int]
    sol_creadate: Optional[date]
    sol_modiby: Optional[int]
    sol_modidate: Optional[date]

    class Config:
        orm_mode = True