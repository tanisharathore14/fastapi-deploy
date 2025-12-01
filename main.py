from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory='templates')


class HelloPayload(BaseModel):
    name: str = "World"


@app.get("/api/hello", response_class=JSONResponse)
async def get_hello():
    """
    GET endpoint that returns a simple JSON hello message.
    """
    return {"message": "Hello, World!"}


@app.post("/api/hello", response_class=JSONResponse)
async def post_hello(payload: HelloPayload):
    """
    POST endpoint that accepts JSON like {"name": "Alice"}
    and returns a greeting.
    """
    name = payload.name.strip() or "World"
    return {"message": f"Hello, {name}!"}


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    """
    Render an HTML page containing a small form that calls the POST endpoint.
    """
    return templates.TemplateResponse("index.html", {"request": request})
