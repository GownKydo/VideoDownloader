import sys
sys.path.append('/path/to/root_directory')

from packages import DownloadVideo, DownloadPlaylist, DownloadAudio

def menu():
    print("1. Download Video")
    print("2. Download Playlist")
    print("3. Download Only Audio")
    print("4. Exit")

def main():
    while True:
        menu()
        choice = input("[*] Enter your choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("[!] Please enter a valid number.")
            continue

        if choice == 1:
            url = input("[*] Enter the video URL: ")
            DownloadVideo.download_video(url)

        elif choice == 2:
            url = input("[*] Enter the playlist URL: ")
            DownloadPlaylist.download_playlist(url)

        elif choice == 3:
            url = input("[*] Enter the audio URL: ")
            DownloadAudio.download_audio(url)

        elif choice == 4:
            print("[!] Goodbye!")
            break
        else:
            print("[!] Invalid choice!")

if __name__ == '__main__':
    main()
