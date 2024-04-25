from packages import DownloadVideo
from packages import DownloadPlaylist
from packages import DownloadAudio

def menu():
    print("\n1. Download Video")
    print("2. Download Playlist")
    print("3. Download Only Audio")
    print("4. Exit\n")

def main():
    while True:
        menu()
        choice = input("\n[*] Enter your choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("\nt[!] Please enter a valid number!")
            continue

        if choice == 1:
            url = input("\n[*] Enter the video URL: ")
            DownloadVideo.download_video(url)

        elif choice == 2:
            url = input("\n[*] Enter the playlist URL: ")
            DownloadPlaylist.download_playlist(url)

        elif choice == 3:
            url = input("\n[*] Enter the audio URL: ")
            DownloadAudio.download_audio(url)

        elif choice == 4:
            print("\n\t[!] Goodbye!")
            break
        else:
            print("\n\t[!] Invalid choice!")

if __name__ == '__main__':
    main()
