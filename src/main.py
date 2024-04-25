from yt_dlp import YoutubeDL

def main():
    # Ask the user for the URL
    url = input("Enter the URL: ")

    # Options for the downloader
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'videos/%(title)s.%(ext)s'
    }

    # Download the video
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Downloaded successfully!")

if __name__ == '__main__':
    main()
