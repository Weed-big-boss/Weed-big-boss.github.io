from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from page.page_router import router


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(router)
