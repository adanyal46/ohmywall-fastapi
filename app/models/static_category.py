from sqlalchemy import Column,Integer,String,DateTime
from app.database.database import Base
from datetime import datetime

class StaticCategory(Base):
    __tablename__ = "static_categories"
    
    id = Column(Integer, primary_key=True, index=True)
    catName = Column(String(255),nullable=False, )
    imageName = Column(String(255), nullable=False)
    dimension = Column(String(100), nullable=True)
    size = Column(Integer, nullable=True)
    originalName = Column(String(255), nullable=True)
    views = Column(Integer, default=0)
    wallpaperCount = Column(Integer, default=0)
    Order = Column(Integer, nullable=True)
    createdAt = Column(DateTime, default=datetime.utcnow)