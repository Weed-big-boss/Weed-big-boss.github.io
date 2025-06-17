from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from page.page_router import router


app = FastAPI()


app.include_router(router)
