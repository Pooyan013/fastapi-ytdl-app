from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
from fastapi.responses import FileResponse
from yt_dlp import YoutubeDL

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

DOWNLOAD_DIR = "downloads/"

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)


def download_video(url: str, format: str, quality: str, only_audio: bool = False, download_thumbnail: bool = False):
    ydl_opts = {
        "outtmpl": f"{DOWNLOAD_DIR}%(title)s.%(ext)s",
        "format": f"{quality}[ext={format}]",
        "noplaylist": False,
    }

    if only_audio:
        ydl_opts["format"] = "bestaudio/best"

    if download_thumbnail:
        ydl_opts["writethumbnail"] = True
        
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/download/")
async def download(request: Request, url: str, format: str, quality: str, only_audio: bool = False, download_thumbnail: bool = False):
    try:
        file_path = download_video(url, format, quality, only_audio, download_thumbnail)
        file_name = os.path.basename(file_path)
        return FileResponse(file_path, filename=file_name, media_type="application/octet-stream")
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error")