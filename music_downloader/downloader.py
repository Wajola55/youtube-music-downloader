import sys
import re
from youtube_dl import YoutubeDL
from yt_dlp import YoutubeDL

def progress_hook(status):
    if status['status'] == 'downloading':
        downloaded_bytes = status.get('downloaded_bytes', 0)
        total_bytes = status.get('total_bytes', 0)
        
        if total_bytes > 0:
            progress_percent = downloaded_bytes / total_bytes * 100
            sys.stdout.write(f"\rProgress: {progress_percent:.2f}%")
            sys.stdout.flush()
    elif status['status'] == 'finished':
        print("\nDownload complete!")

def is_valid_youtube_url(url):
    youtube_pattern = re.compile(
        r'(https?://)?(www\.)?'
        r'(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
    )
    return bool(youtube_pattern.match(url.strip()))  



def download_audio(url, audio_format, progress_callback=None):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': audio_format,
            'preferredquality': '192',
        }],
        'outtmpl': 'downloaded_music/%(title)s.%(ext)s',
        'noplaylist': False,
        'progress_hooks': [progress_callback] if progress_callback else [],
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        # Check if the URL is a playlist
        if "_type" in info and info["_type"] == "playlist":
            for entry in info["entries"]:
                entry_url = entry["webpage_url"]
                ydl.download([entry_url])
        else:
            ydl.download([url])


