from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.schemas.static_wallpaper import StaticWallpaperCreate, StaticWallpaperOut
from app.services.static_wallpaper_service import create_static_wallpaper, get_static_wallpapers, get_static_wallpaper_by_id

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new wallpaper
@router.post("/static_wallpapers", response_model=StaticWallpaperOut)
def create_wallpaper(wallpaper: StaticWallpaperCreate, db: Session = Depends(get_db)):
    return create_static_wallpaper(db, wallpaper)

# Get all wallpapers
@router.get("/static_wallpapers", response_model=dict)
def read_wallpapers(db: Session = Depends(get_db)):
    wallpapers = get_static_wallpapers(db)
    # Transform the response to match the required format
    response = [
        {
            "id": wallpaper.id,
            "cat_name": wallpaper.catname,  # Changed to 'cat_name'
            "image_name": wallpaper.new_name,  # Changed to 'image_name'
            "hd_url": f"https://ohmywall.nyc3.digitaloceanspaces.com/staticwallpaper/hd/{wallpaper.imagename}",
            "compress_url": f"https://ohmywall.nyc3.digitaloceanspaces.com/staticwallpaper/hd/{wallpaper.imagename}",
            "size": str(wallpaper.size),  # Assuming you want size as a string
            "pro": False,  # Assuming this is a static value
            "tags": wallpaper.tags,
            "capacity": wallpaper.dimension,  # Adjust based on your model
        }
        for wallpaper in wallpapers
    ]
    
    return {'images': response}
# Get a single wallpaper by ID
@router.get("/static_wallpapers/{wallpaper_id}", response_model=StaticWallpaperOut)
def read_wallpaper(wallpaper_id: int, db: Session = Depends(get_db)):
    db_wallpaper = get_static_wallpaper_by_id(db, wallpaper_id)
    if db_wallpaper is None:
        raise HTTPException(status_code=404, detail="Wallpaper not found")
    return db_wallpaper
