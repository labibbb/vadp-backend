from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ModelOutput(Base):
    __tablename__ = "tbd_istd_modeloutput"

    mdo_id = Column(Integer, primary_key=True, index=True)
    mdo_model_id = Column(Integer, nullable=True)
    mdo_output_name = Column(String, nullable=True)
    mdo_status = Column(Integer, nullable=True)
    