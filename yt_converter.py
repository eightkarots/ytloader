from pathlib import Path
import sys

from yt_dlp import YoutubeDL

# In a PyInstaller build, __file__ points to the temporary _MEI folder.
# Use the executable's directory so output stays beside the .exe.
if getattr(sys, "frozen", False):
    PROJECT_DIR = Path(sys.executable).resolve().parent
else:
    PROJECT_DIR = Path(__file__).resolve().parent
AUDIO_DIR = PROJECT_DIR / "audio downloads"
VIDEO_DIR = PROJECT_DIR / "video downloads"

AUDIO_DIR.mkdir(parents=True, exist_ok=True)
VIDEO_DIR.mkdir(parents=True, exist_ok=True)

while True:
    youtube_link = input("Enter link here (or 'q' to quit): ").strip()
    if not youtube_link:
        continue
    if youtube_link.lower() in {"q", "quit", "exit"}:
        break

    download_type = input("Download type (audio/a or video/v): ").strip().lower()

    if download_type in {"video", "v"}:
        ydl_opts = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
            "merge_output_format": "mp4",
            "outtmpl": str(VIDEO_DIR / "%(artist|uploader)s - %(title)s.%(ext)s"),
        }
    elif download_type in {"audio", "a"}:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": str(AUDIO_DIR / "%(artist|uploader)s - %(title)s.%(ext)s"),
        }
    else:
        print("Invalid type. Enter 'audio/a' or 'video/v'.")
        continue

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_link])
    except Exception as exc:
        print(f"Download failed: {exc}")
