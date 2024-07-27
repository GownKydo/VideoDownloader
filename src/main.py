from packages.youtube import DownloadAudio, DownloadPlaylist, DownloadVideo

import os
from time import sleep

def menu():
    print("""
    ##########################################
    #####                                #####
    #####   Tools for Download Videos    #####
    #####                                #####
    ##########################################

  -_-_-_-_-_--_-_-_-_-_--_-_-_-_-_--_-_-_-_-_-_

  [1] Youtube\t[2] Twitteer/X\t[3] Instagram

  [0] Exit
   \n""")

def second_menu():
    print("""\n
    1. Download Video.
    2. Download Only Audio.
    3. Download Playlist.
    4. Exit.
    """)


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
        
        if (choice == 1):
            second_menu()
            option = int(input("[*] Enter your choise: "))
            
            if (option == 1):
                url = input("[*] Enter the video URL: ")
                print()
                DownloadVideo.download_video(url)
                print()
            elif (option == 2):
                url = input("[*] Enter the video URL: ")
                print()
                DownloadAudio.download_audio(url)
                print()
            elif (option == 3):
                url = input("[*] Enter the video URL: ")
                print()
                DownloadPlaylist.download_playlist(url)
                print()
            else:
                print("Enter a Valid Option!\n")
        
        if (choice == 2):
            url = input("[*] Enter the video URL: ")
            DownloadVideo.download_video(url)
            print()
        
        if (choice == 3):
            print("Building . . ")
            sleep(3)

        if (choice == 4):
            print("\n\tGoog Bye! :)\n")
            sleep(3)
            break;

if __name__ == '__main__':
    main()
