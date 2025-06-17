from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="", tags=[""])

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class = HTMLResponse)
async def auth_html(request: Request):
    query_params = request.query_params
    name = query_params.get("name")
    message = query_params.get("message")
    return templates.TemplateResponse(
        "main_page.html",
        {
            "request": request,
            "name": name,
            "message": message
        }
    )

