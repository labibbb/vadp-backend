from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.model import modeloutputModel, modelModel
from app.schema import modeloutputSchema

# GET BY ID
def get_modeloutput(db: Session, mdo_id: int):
    result = (
        db.query(
            modeloutputModel.ModelOutput.mdo_id,
            modeloutputModel.ModelOutput.mdo_model_id,
            modeloutputModel.ModelOutput.mdo_output_name,
            modeloutputModel.ModelOutput.mdo_status,
            modelModel.Model.mod_name.label("mdl_name")
        )
        .join(modelModel.Model, modeloutputModel.ModelOutput.mdo_model_id == modelModel.Model.mod_id, isouter=True)
        .filter(modeloutputModel.ModelOutput.mdo_id == mdo_id)
        .first()
    )

    if not result:
        raise HTTPException(status_code=404, detail="Detail not found")

    return {
        "mdo_id": result.mdo_id,
        "mdo_model_id": result.mdo_model_id,
        "mdo_output_name": result.mdo_output_name,
        "mdo_status": result.mdo_status,
        "mdl_name": result.mdl_name
    }

# GET ALL (optional, bisa diaktifkan)
def get_all_modeloutput(db: Session):
    results = (
        db.query(
            modeloutputModel.ModelOutput.mdo_id,
            modeloutputModel.ModelOutput.mdo_model_id,
            modeloutputModel.ModelOutput.mdo_output_name,
            modeloutputModel.ModelOutput.mdo_status,
            modelModel.Model.mod_name.label("mdl_name")
        )
        .join(modelModel.Model, modeloutputModel.ModelOutput.mdo_model_id == modelModel.Model.mod_id, isouter=True)
        .all()
    )
    return [
        {
            "mdo_id": row.mdo_id,
            "mdo_model_id": row.mdo_model_id,
            "mdo_output_name": row.mdo_output_name,
            "mdo_status": row.mdo_status,
            "mdl_name": row.mdl_name
        }
        for row in results
    ]

# CREATE
def create_modeloutput(db: Session, modeloutput: modeloutputSchema.ModelOutputCreate):
    db_modeloutput = modeloutputModel.ModelOutput(
        mdo_model_id=modeloutput.mdo_model_id,
        mdo_output_name=modeloutput.mdo_output_name,
        mdo_status=modeloutput.mdo_status,
    )
    db.add(db_modeloutput)
    db.commit()
    db.refresh(db_modeloutput)
    return db_modeloutput

# UPDATE
def update_modeloutput(db: Session, mdo_id: int, modeloutput: modeloutputSchema.ModelOutputUpdate):
    db_modeloutput = db.query(modeloutputModel.ModelOutput).filter(modeloutputModel.ModelOutput.mdo_id == mdo_id).first()
    if not db_modeloutput:
        raise HTTPException(status_code=404, detail="Model Output not found")

    for var, value in vars(modeloutput).items():
        if value is not None:
            setattr(db_modeloutput, var, value)
    db.commit()
    db.refresh(db_modeloutput)
    return db_modeloutput

# DELETE
def delete_modeloutput(db: Session, mdo_id: int):
    db_modeloutput = db.query(modeloutputModel.ModelOutput).filter(modeloutputModel.ModelOutput.mdo_model_id == mdo_id).first()
    if not db_modeloutput:
        raise HTTPException(status_code=404, detail="Model Output not found")
    db.delete(db_modeloutput)
    db.commit()
    return {"detail": "Model Output deleted successfully"}

def get_modeloutput_by_modelid(db: Session, mdo_model_id: int):
    results = (
        db.query(
            modeloutputModel.ModelOutput.mdo_id,
            modeloutputModel.ModelOutput.mdo_model_id,
            modeloutputModel.ModelOutput.mdo_output_name,
            modeloutputModel.ModelOutput.mdo_status,
            modelModel.Model.mod_name.label("mdl_name")
        )
        .join(modelModel.Model, modeloutputModel.ModelOutput.mdo_model_id == modelModel.Model.mod_id, isouter=True)
        .filter(modeloutputModel.ModelOutput.mdo_model_id == mdo_model_id)
        .all()
    )

    if not results:
        raise HTTPException(status_code=404, detail="Data not found")

    return [
        {
            "mdo_id": row.mdo_id,
            "mdo_model_id": row.mdo_model_id,
            "mdo_output_name": row.mdo_output_name,
            "mdo_status": row.mdo_status,
            "mdl_name": row.mdl_name
        }
        for row in results
    ]
