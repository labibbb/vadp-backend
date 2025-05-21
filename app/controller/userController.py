from sqlalchemy.orm import Session
from app.model import userModel
from app.schema import userSchema

# GET ALL CAMERAS
def get_all_users(db: Session): 
    return db.query(userModel.User).all()

# GET BY ID
def get_users(db: Session, usr_id: int):
    user = db.query(userModel.User).filter(userModel.User.usr_id == usr_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# CREATE
def create_user(db: Session, user: userSchema.UserCreate):
    db_user = userModel.User(
        usr_username=user.usr_username,
        usr_password=user.usr_password,
        usr_name=user.usr_name,
        usr_role=user.usr_role,
        usr_status=user.usr_status,
        usr_creaby=user.usr_creaby,
        usr_creadate=user.usr_creadate or datetime.date.today()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# UPDATE
def update_user(db: Session, usr_id: int, user: userSchema.UserUpdate):
    db_user = db.query(userModel.User).filter(userModel.User.usr_id == usr_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.usr_username = user.usr_username
    db_user.usr_password = user.usr_password
    db_user.usr_name = user.usr_name
    db_user.usr_role = user.usr_role
    db_user.usr_status = user.usr_status
    db_user.usr_modiby = user.usr_modiby
    db_user.usr_modidate = user.usr_modidate or datetime.date.today()

    db.commit()
    db.refresh(db_user)
    return db_user

# DELETE
def delete_user(db: Session, usr_id: int):
    db_user = db.query(userModel.User).filter(userModel.User.usr_id == usr_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Camera not found")

    db.delete(db_user)
    db.commit()
    return {"detail": "User deleted successfully"}