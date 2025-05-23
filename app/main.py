from fastapi import FastAPI
from app.routes import users, camera, model, solution, modelsolution, camerasolution, solutionusage, modeloutput
from app.database import engine
from app.models import Base
from fastapi.middleware.cors import CORSMiddleware
# Inisialisasi database
Base.metadata.create_all(bind=engine)

# Inisialisasi FastAPI
app = FastAPI()

# Konfigurasi CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # atau ganti dengan ['http://localhost'] untuk lebih aman
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Tambahkan router
app.include_router(users.router)
app.include_router(camera.router)
app.include_router(model.router)
app.include_router(solution.router)
app.include_router(modelsolution.router)
app.include_router(camerasolution.router)
app.include_router(solutionusage.router)
app.include_router(modeloutput.router)
