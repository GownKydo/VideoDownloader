from packages import DownloadVideo, DownloadPlaylist, DownloadAudio

def menu():
    print("1. Download Video")
    print("2. Download Playlist")
    print("3. DOwnload Only Audio")
    print("4. Exit")

def main():
    band = bool = True

    while band:
        menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            DownloadVideo.main()

        elif choice == 2:
            DownloadPlaylist.main()

        elif choice == 3:
            DownloadAudio.main()

        elif choice == 4:
            break
        else:
            print("Invalid choice!")

if __name__ == '__main__':
    main()
