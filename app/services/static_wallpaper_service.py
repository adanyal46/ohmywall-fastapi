from sqlalchemy.orm import Session
from app.models.static_wallpaper import StaticWallpaper
from app.schemas.static_wallpaper import StaticWallpaperCreate
from datetime import datetime, timezone


def create_static_wallpaper(db: Session, wallpaper: StaticWallpaperCreate):
    db_wallpaper = StaticWallpaper(
        catname=wallpaper.catname,
        imagename=wallpaper.imagename,
        size=wallpaper.size,
        dimension=wallpaper.dimension,
        tags=wallpaper.tags,
        new_name=wallpaper.new_name,
        createdAt=datetime.now(timezone.utc)
    )
    db.add(db_wallpaper)
    db.commit()
    db.refresh(db_wallpaper)
    return db_wallpaper

# Retrieve all wallpapers
def get_static_wallpapers(db: Session):
    return db.query(StaticWallpaper).all()
# Get a specific wallpaper by ID
def get_static_wallpaper_by_id(db: Session, wallpaper_id: int):
    return db.query(StaticWallpaper).filter(StaticWallpaper.id == wallpaper_id).first()