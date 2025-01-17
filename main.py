from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os 
from fastapi.responses import FileResponse
from yt_dlp import YoutubeDL

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory="static"),name="static")

DOWNLOAD_DIR ="downloads/"

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

def downlaod_video(url:str):
    ydl_opts={
        "outtmpl":f"{DOWNLOAD_DIR}%(title)s.%(ext)s",
        "format":"best"
    }
    with YoutubeDL(ydl_opts) as ydl:
        info =ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/download/")
async def download(request:Request,url):
    try:
        file_path = downlaod_video(url)
        file_name = os.path.basename(file_path)
        return FileResponse(file_path,filename=file_name,media_type="application/octet-stream")
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error")