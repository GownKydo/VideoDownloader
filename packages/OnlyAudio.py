from yt_dlp import YoutubeDL

def main():
    url = input("Enter the URL: ")
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

    print("Downloaded successfully!")

if __name__ == '__main__':
    main()
