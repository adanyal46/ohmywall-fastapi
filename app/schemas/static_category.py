from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from fastapi import UploadFile

class StaticCategoryBase(BaseModel):
    catName: str
    imageName: Optional[str] = None
    dimension: Optional[str] = None
    size: Optional[int] = None
    originalName: Optional[str] = None
    views: Optional[int] = 0
    wallpaperCount: Optional[int] = 0
    Order: Optional[int] = None
    
class StaticCategoryCreate(StaticCategoryBase):
    pass

class StaticCategoryUpdate(BaseModel):
    catName: Optional[str] = None
    image: Optional[UploadFile] = None
    views: Optional[int] = None

class StaticCategory(StaticCategoryBase):
    id: int
    createdAt: datetime

    class Config:
        orm_mode = True