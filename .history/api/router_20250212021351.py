from fastapi import APIRouter

from api.routes import books

api_router = APIRouter()
api_router.include_router(books.router, prefix="api/v1/books", tags=["books"])
