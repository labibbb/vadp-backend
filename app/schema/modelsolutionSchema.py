from pydantic import BaseModel
from typing import Optional
from datetime import date

# Create schema
class ModelSolutionCreate(BaseModel):
    mds_id: int
    mds_model_id: Optional[int]
    mds_solution_id: Optional[int]
    mds_status: Optional[int]

# Update schema
class ModelSolutionUpdate(BaseModel):
    mds_model_id: Optional[int] = None
    mds_solution_id: Optional[int] = None
    mds_status: Optional[int] = None

# Response schema (optional but recommended)
class ModelSolutionResponse(BaseModel):
    mds_id: int
    mds_model_id: Optional[int]
    mds_solution_id: Optional[int]
    mds_status: Optional[int]
    mdl_name: Optional[str]  # <-- ditambahkan

    class Config:
        orm_mode = True
