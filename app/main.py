from fastapi import FastAPI
from app.routes import users, camera
from app.database import engine
from app.models import Base

# Inisialisasi database
Base.metadata.create_all(bind=engine)

# Inisialisasi FastAPI
app = FastAPI()

# Tambahkan router
app.include_router(users.router)
app.include_router(camera.router)
