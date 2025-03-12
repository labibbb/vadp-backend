from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

class Camera(Base):
    __tablename__ = "tbm_istd_camera"

    camera_id = Column(Integer, primary_key=True, index=True)
    camera_rtsp = Column(String(255), nullable=True)
    camera_status = Column(Integer, nullable=True)
    camera_creaby = Column(Integer, nullable=True)
    camera_creadate = Column(Date, nullable=True)
    camera_modiby = Column(Integer, nullable=True)
    camera_modidate = Column(Date, nullable=True)