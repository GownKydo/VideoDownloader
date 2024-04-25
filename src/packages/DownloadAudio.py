from yt_dlp import YoutubeDL

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': 'audio/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Audio downloaded successfully!")
