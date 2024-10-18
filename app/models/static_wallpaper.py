from app.database.database import Base
from sqlalchemy import Column,Integer,String,DateTime,Enum
from enum import Enum as PyEnum
from datetime import datetime, timezone

class StatusEnum(PyEnum):
    active = "active"
    inactive = "inactive"


class StaticWallpaper(Base):
    __tablename__ = "static_wallpapers"
    
    id = Column(Integer, primary_key=True, index=True)
    catname = Column(String(50), nullable=False)
    imagename = Column(String(100), nullable=False)
    size = Column(Integer, nullable=True)
    dimension = Column(String(100), nullable=False)
    views = Column(Integer, nullable=True, default=0)
    likes = Column(Integer, nullable=True, default=0)
    download = Column(Integer, nullable=True, default=0)
    tags = Column(String(255), nullable=False)
    new_name = Column(String(255), nullable=False)
    createdAt = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    status = Column(Enum(StatusEnum), nullable=True)
    
