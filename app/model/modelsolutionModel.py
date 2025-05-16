from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ModelSolution(Base):
    __tablename__ = "tbd_istd_modelsolution"

    mds_id = Column(Integer, primary_key=True, index=True)
    mds_model_id = Column(Integer, nullable=True)
    mds_solution_id = Column(Integer, nullable=True)
    mds_status = Column(Integer, nullable=True)
    