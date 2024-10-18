from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from typing import Optional

class StatusEnum(Enum):
    active = "active"
    inactive = "inactive"
    
class StaticWallpaperCreate(BaseModel):
    catname: str
    imagename: str
    size: Optional[int]
    dimension: str
    tags: str
    new_name: str
    
class StaticWallpaperOut(BaseModel):
    id: int
    cat_name: str
    image_name: str
    size: Optional[int]
    capacity: str
    tags: str
    
    class Config:
        orm_mode = True