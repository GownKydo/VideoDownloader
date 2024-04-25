from packages import DownloadVideo, DownloadPlaylist, DownloadAudio
from yt_dlp import YoutubeDL

def menu():
    print("1. Download Video")
    print("2. Download Playlist")
    print("3. DOwnload Only Audio")
    print("4. Exit")

def QualityVideo(url):
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

def main():
    band = bool = True

    while band:
        menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            DownloadVideo.main()
            QualityVideo()

        elif choice == 2:
            DownloadPlaylist.main()
            QualityVideo()

        elif choice == 3:
            DownloadAudio.main()

        elif choice == 4:
            break
        else:
            print("Invalid choice!")

if __name__ == '__main__':
    main()
