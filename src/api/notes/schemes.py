from datetime import datetime

from pydantic import BaseModel, TypeAdapter


class CreateNoteSchema(BaseModel):
    text: str


class NoteSchema(BaseModel):
    text: str
    created_at: datetime


ListNoteSchema = TypeAdapter(list[NoteSchema])
