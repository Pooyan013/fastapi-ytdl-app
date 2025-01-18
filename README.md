# YouTube Downloader with FastAPI

This project is a simple YouTube downloader API built using **FastAPI** and **yt-dlp**. It allows users to download YouTube videos, audio, and thumbnails in different formats and qualities.

## Features

- **Download videos**: Download YouTube videos in various formats and quality.
- **Download audio**: Download only the audio of the video in the best available quality.
- **Download thumbnail**: Option to download the video thumbnail.
- **Support for playlists**: Download all videos in a playlist.
- **Custom download directory**: All files are downloaded to a `downloads/` folder by default.

## Setup

### Requirements

- Python 3.8+
- FastAPI
- yt-dlp
- Uvicorn

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/YouTube-Downloader-FastAPI.git
   cd YouTube-Downloader-FastAPI
pip install -r requirements.txt
uvicorn main:app --reload
