from fastapi import FastAPI

from .auth.routers import router as users_router
from .notes.routers import router as notes_router


def create_app():
    app = FastAPI()

    app.include_router(notes_router)
    app.include_router(users_router)

    return app
