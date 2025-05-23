from pydantic import BaseModel
from typing import Optional
from datetime import date

# Create schema
class ModelOutputCreate(BaseModel):
    mdo_id: int
    mdo_model_id: Optional[int]
    mdo_output_name: Optional[str]
    mdo_status: Optional[int]

# Update schema
class ModelOutputUpdate(BaseModel):
    mdo_model_id: Optional[int] = None
    mdo_output_name: Optional[str] = None
    mdo_status: Optional[int] = None

# Response schema (optional but recommended)
class ModelOutputResponse(BaseModel):
    mdo_id: int
    mdo_model_id: Optional[int]
    mdo_output_name: Optional[str]
    mdo_status: Optional[int]
    mdl_name: Optional[str]  # <-- ditambahkan

    class Config:
        orm_mode = True
