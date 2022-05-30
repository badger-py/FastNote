from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field

import enums
from db import Base


class User(Base):
    __collectionname__ = "users"

    id: Optional[str] = Field(None, alias="_id")
    email: EmailStr
    name: str = Field(None, description="A name of user (name and surname)")
    password: str  # hashed
    is_active: bool = False  # after register user not verificated email


class Folder(Base):
    __collectionname__ = "folders"

    id: Optional[str] = Field(None, alias="_id")
    name: str
    color: enums.Color = enums.Color.grey


class NoteContentPart(BaseModel):
    # NOT A DB TABLE!
    number: int = 0  # to sort
    type: enums.NoteContentPartType
    data: List[str]


class Note(Base):
    __collectionname__ = "notes"

    id: Optional[str] = Field(None, alias="_id")
    title: str
    user: str  # user_id
    folder: str = None  # folder_id or None
    color: enums.Color = enums.Color.grey
    content: List[NoteContentPart] = []
