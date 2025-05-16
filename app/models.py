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

    cam_id = Column(Integer, primary_key=True, index=True)
    cam_rtsp = Column(String(255), nullable=True)
    cam_status = Column(Integer, nullable=True)
    cam_creaby = Column(Integer, nullable=True)
    cam_creadate = Column(Date, nullable=True)
    cam_modiby = Column(Integer, nullable=True)
    cam_modidate = Column(Date, nullable=True)

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