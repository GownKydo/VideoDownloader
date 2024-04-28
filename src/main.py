from packages import DownloadVideo
from packages import DownloadPlaylist
from packages import DownloadAudio

import os

def menu():
    print("\n1. Download Video")
    print("2. Download Playlist")
    print("3. Download Only Audio")
    print("4. Exit\n")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        menu()
        choice = input("\n[*] Enter your choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("\nt[!] Please enter a valid number!")
            continue

        if choice == 1:
            url = input("[*] Enter the video URL: ")
            DownloadVideo.download_video(url)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif choice == 2:
            url = input("[*] Enter the playlist URL: ")
            DownloadPlaylist.download_playlist(url)

        elif choice == 3:
            url = input("[*] Enter the audio URL: ")
            DownloadAudio.download_audio(url)

        elif choice == 4:
            print("\t[!] Goodbye!")
            break
        else:
            print("\n\t[!] Invalid choice!")

if __name__ == '__main__':
    main()
