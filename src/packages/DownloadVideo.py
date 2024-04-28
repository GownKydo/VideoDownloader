from yt_dlp import YoutubeDL
from tarfile import ExtractError
from yt_dlp.utils import DownloadError
import os

def download_video(url):
    print("\n[*] Fetching video information...")
    
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join('videos', '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("\n[*] Downloaded successfully!")

    except DownloadError as de:
        print(f"[!] Failed to download the video: {de}")

    except ExtractError as ee:
        print(f"[!] Error extracting video information: {ee}")
        
    except Exception as e:
        print(f"[!] An unexpected error occurred: {e}")

