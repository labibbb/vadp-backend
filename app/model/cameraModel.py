from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Camera(Base):
    __tablename__ = "tbm_istd_camera"

    cam_id = Column(Integer, primary_key=True, index=True)
    cam_name = Column(String(255), nullable=True)
    cam_ip = Column(String(255), nullable=True)
    cam_rtsp = Column(String(255), nullable=True)
    cam_status = Column(Integer, nullable=True)
    cam_creaby = Column(Integer, nullable=True)
    cam_creadate = Column(Date, nullable=True)
    cam_modiby = Column(Integer, nullable=True)
    cam_modidate = Column(Date, nullable=True)