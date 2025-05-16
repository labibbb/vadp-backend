from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Solution(Base):
    __tablename__ = "tbm_istd_solution"

    sol_id = Column(Integer, primary_key=True, index=True)
    sol_name = Column(String(255), nullable=True)
    sol_camera_amount = Column(Integer, nullable=True)
    sol_model_amount = Column(Integer, nullable=True)
    sol_status = Column(Integer, nullable=True)
    sol_creaby = Column(Integer, nullable=True)
    sol_creadate = Column(Date, nullable=True)
    sol_modiby = Column(Integer, nullable=True)
    sol_modidate = Column(Date, nullable=True)