from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
from pathlib import Path


async def post_user(db: Session, raw_data: schemas.PostUser):
    name: str = raw_data.name
    last_name: str = raw_data.last_name

    import uuid

    try:
        user_id: str = str(uuid.uuid4())
        print(f"user_id: {user_id}")
    except Exception as e:
        raise HTTPException(500, str(e))

    record_to_be_added = {"name": name, "last_name": last_name}
    new_user = models.User(**record_to_be_added)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    add_a_records = new_user.to_dict()

    res = {
        "add_a_records": add_a_records,
    }
    return res
