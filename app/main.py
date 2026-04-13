# Entry point of the FastAPI application; initializes app and includes all routes
from fastapi import FastAPI
from app.routes.tool_routes import router
from app.config import APP_TITLE, APP_DESCRIPTION, APP_VERSION

app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION
)

app.include_router(router)