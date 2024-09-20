import aiohttp
from fastapi import APIRouter, Depends, status
from fastapi.responses import Response
from sqlalchemy import insert, select

from api.auth.dependencies import JWTBearer
from api.notes.schemes import CreateNoteSchema, ListNoteSchema, NoteSchema
from db.base import async_session
from db.models import Note

router = APIRouter(
    prefix="/notes",
    tags=["notes"],
)


@router.get("/")
async def get_notes_list(
    user=Depends(JWTBearer())
) -> list[NoteSchema]:
    async with async_session() as session:
        query = select(Note.text, Note.created_at).where(Note.user_id == user["user_id"])
        result = (await session.scalars(query)).all()
    return ListNoteSchema.validate_python(result)


@router.post("/")
async def create_note(
    data: CreateNoteSchema, user=Depends(JWTBearer())
):
    url = f'https://speller.yandex.net/services/spellservice.json/checkText?text={data.text.replace(' ', '+')}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            buf = await resp.json()

    if buf:
        for el in buf:
            before = data.text[: el["pos"]]
            after = data.text[el["len"] + el["pos"] :]
            data.text = before + el["s"][0] + after

    async with async_session() as session:
        query = insert(Note).values(text=data.text, user_id=user["user_id"])
        await session.execute(query)
        await session.commit()
    return Response(status_code=status.HTTP_201_CREATED)
