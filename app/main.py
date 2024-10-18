from fastapi import FastAPI
from app.routes.static_category_routes import router as static_category_router
from app.routes.static_wallpaper_routes import router as static_wallpaper_router
from app.database.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(static_category_router, prefix='/api')
app.include_router(static_wallpaper_router, prefix='/api')