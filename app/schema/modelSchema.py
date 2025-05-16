from pydantic import BaseModel
from typing import Optional
from datetime import date

# Create schema
class ModelCreate(BaseModel):
    mod_id: int
    mod_name: Optional[str]
    mod_file_name: Optional[str]
    mod_status: Optional[int]
    mod_creaby: Optional[int]
    mod_creadate: Optional[date]

# Update schema
class ModelUpdate(BaseModel):
    mod_name: Optional[str] = None
    mod_file_name: Optional[str] = None
    mod_status: Optional[int] = None
    mod_modiby: Optional[int] = None
    mod_modidate: Optional[date] = None

# Response schema (optional but recommended)
class ModelResponse(BaseModel):
    mod_id: int
    mod_name: Optional[str]
    mod_file_name: Optional[str] 
    mod_status: Optional[int] 
    mod_creaby: Optional[int] 
    mod_creadate: Optional[date] 
    mod_modiby: Optional[int] 
    mod_modidate: Optional[date]

    class Config:
        orm_mode = True