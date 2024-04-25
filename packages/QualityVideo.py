from yt_dlp import YoutubeDL

def QualityVideo():
    url = input("Enter the URL: ")
    print("Fetching available formats...")
    
    with YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', [info_dict])

        for f in formats:
            print(f"{f['format_id']}: {f['format_note']}")

    fmt = input("Enter format id: ")

    ydl_opts = {
        'format': fmt,
        'outtmpl': 'videos/%(title)s.%(ext)s'
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Downloaded successfully!")

if __name__ == '__main__':
    QualityVideo()
