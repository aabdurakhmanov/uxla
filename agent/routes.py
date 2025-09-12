from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from agent import commands
from pathlib import Path

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@router.get("/shutdown")
def shutdown_pc():
    commands.shutdown()
    return {"status": "Shutting down..."}

@router.get("/restart")
def restart_pc():
    commands.restart()
    return {"status": "Restarting..."}

@router.get("/sleep")
def sleep_pc():
    commands.sleep()
    return {"status": "Sleeping..."}

@router.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
