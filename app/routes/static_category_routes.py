from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.schemas.static_category import StaticCategory, StaticCategoryCreate,StaticCategoryUpdate
from app.services.static_category_service import StaticCategoryService
from typing import Optional
from fastapi import HTTPException

router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post('/categories', response_model=StaticCategory)
def create_category(
    catName: str = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    category = StaticCategoryCreate(catName=catName)
    service = StaticCategoryService(db)
    return service.create_category(category, image)

@router.get('/categories',response_model=list[StaticCategory])
def read_categories(db:Session = Depends(get_db)):
    service =StaticCategoryService(db)
    return service.get_categories()

@router.put('/categories/{category_id}',response_model=StaticCategory)
def update_category(category_id:int,  catName: Optional[str] = Form(None),
    views: Optional[int] = Form(None),
    image: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)):
    category_data = StaticCategoryUpdate(catName=catName, views=views)
    service = StaticCategoryService(db)
    updated_category = service.update_catgory(category_id,category_data,image)
    if updated_category:
        return updated_category
    raise HTTPException(status_code=404, detail="Category not found")
    
@router.delete('/categories/{category_id}', response_model=StaticCategory)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    service = StaticCategoryService(db)
    deleted_category = service.delete_category(category_id)
    if deleted_category:
        return deleted_category
    raise HTTPException(status_code=404, detail="Category not found")