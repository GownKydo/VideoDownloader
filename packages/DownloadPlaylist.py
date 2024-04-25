from yt_dlp import YoutubeDL

def download_playlist(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'playlists/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s'
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("[*] Playlist downloaded successfully!")
