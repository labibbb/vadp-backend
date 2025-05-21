from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SolutionUsage(Base):
    __tablename__ = "tbt_istd_solutionusage"

    slu_id = Column(Integer, primary_key=True, index=True)
    slu_solution_id = Column(Integer, nullable=True)
    slu_user_id = Column(Integer, nullable=True)
    slu_status = Column(Integer, nullable=True)
    