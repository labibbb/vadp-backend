from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "tbm_istd_user"

    usr_id = Column(Integer, primary_key=True, index=True)
    usr_username = Column(String, index=True)
    usr_password = Column(String, index=True)
    usr_name = Column(String, index=True)
    usr_role = Column(Integer, primary_key=True, index=True)
    usr_status = Column(Integer, primary_key=True, index=True)
    usr_creaby = Column(Integer, nullable=True)
    usr_creadate = Column(Date, nullable=True)
    usr_modiby = Column(Integer, nullable=True)
    usr_modidate = Column(Date, nullable=True)