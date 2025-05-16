from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Model(Base):
    __tablename__ = "tbm_istd_model"

    mod_id = Column(Integer, primary_key=True, index=True)
    mod_name = Column(String(255), nullable=True)
    mod_file_name = Column(String(255), nullable=True)
    mod_status = Column(Integer, nullable=True)
    mod_creaby = Column(Integer, nullable=True)
    mod_creadate = Column(Date, nullable=True)
    mod_modiby = Column(Integer, nullable=True)
    mod_modidate = Column(Date, nullable=True)