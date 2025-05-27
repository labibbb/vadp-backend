from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.controller import userController
from app.model import userModel
from app.schema import userSchema
from app import database
from fastapi.responses import JSONResponse

router = APIRouter()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET ALL CAMERAS
@router.get("/users", response_model=list[userSchema.UserCreate])
def get_all_users(db: Session = Depends(get_db)):
    return userController.get_all_users(db)

# GET CAMERA BY ID
@router.get("/users/{usr_id}", response_model=userSchema.UserCreate)
def get_user(usr_id: int, db: Session = Depends(get_db)):
    return userController.get_users(db, usr_id)

# CREATE CAMERA
@router.post("/users", response_model=userSchema.UserCreate)
def create_user(user: userSchema.UserCreate, db: Session = Depends(get_db)):
    return userController.create_user(db, user)

# UPDATE CAMERA (Menggunakan POST)
@router.post("/users/{usr_id}/update", response_model=userSchema.UserCreate)
def update_camera(usr_id: int, user: userSchema.UserUpdate, db: Session = Depends(get_db)):
    return userController.update_user(db, usr_id, user)

# DELETE CAMERA (Menggunakan POST)
@router.post("/users/{usr_id}/delete")
def delete_user(usr_id: int, db: Session = Depends(get_db)):
    return userController.delete_user(db, usr_id)

@router.get("/users/by-username/{username}", response_model=userSchema.UserResponse)
def get_user_by_username_route(username: str, db: Session = Depends(get_db)):
    user = userController.get_user_by_username(db, username)
    if user is None:
        # Buat object kosong sesuai schema UserResponse
        return JSONResponse(content={
            "usr_id": None,
            "usr_username": "",
            "usr_password": "",
            "usr_name": "",
            "usr_role": None,
            "usr_status": None,
            "usr_creaby": None,
            "usr_creadate": None,
            "usr_modiby": None,
            "usr_modidate": None
        })
    return user