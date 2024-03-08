from pydantic import BaseModel
import bson
from typing import Optional


class GetSmartphone(BaseModel):
    _id: bson.ObjectId
    title: str
    price: int

    class Meta:
        from_attributes = True


class CreateSmartphone(BaseModel):
    title: str
    price: int

    class Meta:
        from_attributes = True


class UpdateSmartphone(BaseModel):
    title: str = None
    price: int = None

    class Meta:
        from_attributes = True


class DeleteSmartphone(BaseModel):
    _id: bson.ObjectId

    class Meta:
        from_attributes = True
