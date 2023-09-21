import uuid

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl

app = FastAPI()

urls_db = {}


class URL(BaseModel):
    original_url: HttpUrl


@app.post("/url")
async def create_url_shortener(url: URL):
    url_id = str(uuid.uuid4())[:6]
    urls_db[url_id] = url.original_url
    return {"short_url": f"http://localhost:8000/redirect/{url_id}", "original_url": url.original_url}


@app.get("/redirect/{url_id}")
async def redirect_url(url_id: str):
    if url_id in urls_db:
        target_url = urls_db[url_id]
        return RedirectResponse(target_url)
    else:
        raise HTTPException(status_code=404, detail="URL not found")


