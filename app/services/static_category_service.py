from sqlalchemy.orm import Session
from app.models.static_category import StaticCategory
from app.schemas.static_category import StaticCategoryCreate,StaticCategoryUpdate
from fastapi import UploadFile
import uuid
import os
from PIL import Image
from typing import Optional


class StaticCategoryService:
    def __init__(self, db:Session):
        self.db = db
        
    def create_category(self, category:StaticCategoryCreate, image:UploadFile):
        unique_filename = f"{uuid.uuid4()}_{image.filename}"
        file_path = f"app/media/static_categories/{unique_filename}"
        
        with open(file_path, "wb") as buffer:
            buffer.write(image.file.read())
            
        with Image.open(file_path) as img:
            width, height = img.size
            size = os.path.getsize(file_path)
        
        db_category = StaticCategory(
            catName=category.catName,
            imageName=unique_filename,
            dimension=f"{width}x{height}",
            size=size,
            originalName=image.filename,  
            views=0,
            wallpaperCount=0,
            Order=0
        )
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category
    
    def get_categories(self):
        return self.db.query(StaticCategory).all()
    
    def update_catgory(self, category_id:int, category_data: StaticCategoryUpdate,image: Optional[UploadFile] = None):
        db_category = self.db.query(StaticCategory).filter(StaticCategory.id == category_id).first()
        if not  db_category:
            return None
        
        if category_data.catName:
            db_category.catName = category_data.catName
        if category_data.views:
            db_category.views = category_data.views
            
        if image:
            old_image_path = f"app/media/static_categories/{db_category.imageName}"
            if os.path.exists(old_image_path):
                os.remove(old_image_path)
                
            unique_filename = f"{uuid.uuid4()}_{image.filename}"
            new_file_path = f"app/media/static_categories/{unique_filename}"
            
            with open(new_file_path, "wb") as buffer:
                buffer.write(image.file.read())
                
            with Image.open(new_file_path) as img:
                width, height = img.size
                size = os.path.getsize(new_file_path)
                
            db_category.imageName = unique_filename
            db_category.dimension = f"{width}x{height}"
            db_category.size = size
            db_category.originalName = image.filename
        self.db.commit()
        self.db.refresh(db_category)
        return db_category
        
    def delete_category(self,category_id:int):
        db_category = self.db.query(StaticCategory).filter(StaticCategory.id == category_id).first()
        if not db_category:
            return None
        
        old_image_path = f"app/media/static_categories/{db_category.imageName}"
        if os.path.exists(old_image_path):
            os.remove(old_image_path)
            
        self.db.delete(db_category)
        self.db.commit()
        return db_category
        