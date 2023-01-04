from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static/stylesheets"), name="static")

templates = Jinja2Templates(directory="static/templates")

@app.get("/item/{item_id}")
async def read_item(request: Request, item_id: str):
    return templates.TemplateResponse('item.html', {"request": request, "item_id": item_id})

@app.get("/item")
async def read_all(request: Request):
    return templates.TemplateResponse('base.html', {"request": request})