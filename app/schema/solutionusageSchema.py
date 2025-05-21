from pydantic import BaseModel
from typing import Optional
from datetime import date

# Create schema
class SolutionUsageCreate(BaseModel):
    slu_id: int
    slu_solution_id: Optional[int]
    slu_user_id: Optional[int]
    slu_status: Optional[int]

# Update schema
class SolutionUsageUpdate(BaseModel):
    slu_solution_id: Optional[int] = None
    slu_user_id: Optional[int] = None
    slu_status: Optional[int] = None

# Response schema (optional but recommended)
class SolutionUsageResponse(BaseModel):
    slu_id: int
    slu_solution_id: Optional[int]
    slu_user_id: Optional[int]
    slu_status: Optional[int]

    class Config:
        orm_mode = True
