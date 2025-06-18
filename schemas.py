from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Course(BaseModel):
    id: int
    course_name: str
    course_price: str


class ReadCourse(BaseModel):
    id: int
    course_name: str
    course_price: str
    class Config:
        from_attributes = True


class User(BaseModel):
    id: int
    name: str
    last_name: str


class ReadUser(BaseModel):
    id: int
    name: str
    last_name: str
    class Config:
        from_attributes = True




class PostUser(BaseModel):
    name: str = Field(..., max_length=100)
    last_name: str = Field(..., max_length=100)

    class Config:
        from_attributes = True

