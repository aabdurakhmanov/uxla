from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from agent import routes
from pathlib import Path
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Remote PC Agent", version="1.0.0")

# Templates
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))

from fastapi.staticfiles import StaticFiles

# static papkani ulash
app.mount("/static", StaticFiles(directory=str(BASE_DIR/"static")), name="static")

# Routes
app.include_router(routes.router)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
