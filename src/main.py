from yt_dlp import YoutubeDL
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

    except Exception as e:
        print(f"\n[!] An error occurred: {e}")
