from yt_dlp import YoutubeDL

def DownloadPlaylist():
    url = input("Enter the URL: ")

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'videos/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s'
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Downloaded successfully!")

if __name__ == '__main__':
    DownloadPlaylist()
