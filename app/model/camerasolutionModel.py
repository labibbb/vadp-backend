from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CameraSolution(Base):
    __tablename__ = "tbd_istd_camerasolution"

    cms_id = Column(Integer, primary_key=True, index=True)
    cms_camera_id = Column(Integer, nullable=True)
    cms_solution_usage_id = Column(Integer, nullable=True)
    cms_status = Column(Integer, nullable=True)
    