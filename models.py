from sqlalchemy import Column, Boolean, ForeignKey, String, Integer, Float
from sqlalchemy.orm import relationship
from app.database import Base


class SubPage(Base):
    __tablename__ = "subpage"
    id = Column(Integer, primary_key=True)
    heading = Column(String, default="This is SubPage heading")
    description = Column(String, default="This is SubPage Description")
    footer = Column(String, default="This is SubPage Footer")
    pg_no = Column(Integer, default=0)
    pg_dim = Column(Float, default=0.0)
