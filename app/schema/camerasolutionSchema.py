from pydantic import BaseModel
from typing import Optional
from datetime import date

# Create schema
class CameraSolutionCreate(BaseModel):
    cms_id: int
    cms_camera_id: Optional[int]
    cms_solution_usage_id: Optional[int]
    cms_status: Optional[int]

# Update schema
class CameraSolutionUpdate(BaseModel):
    cms_camera_id: Optional[int] = None
    cms_solution_usage_id: Optional[int] = None
    cms_status: Optional[int] = None

# Response schema (optional but recommended)
class CameraSolutionResponse(BaseModel):
    cms_id: int
    cms_camera_id: Optional[int]
    cms_solution_usage_id: Optional[int]
    cms_status: Optional[int]

    class Config:
        orm_mode = True
