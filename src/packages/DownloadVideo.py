from yt_dlp import YoutubeDL
import os

def download_video(url):
    print("[*] Fetching available formats...")
    
    try:
        with YoutubeDL() as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [info_dict])

            if not formats:
                print("[!] No available formats found.")
                return

            for f in formats:
                print(f"{f['format_id']}: {f['format_note']} - {f.get('resolution', 'Unknown resolution')}")

            while True:
                fmt = input("[*] Enter format id (or 'q' to quit): ")

                if fmt == 'q':
                    print("[*] Exiting...")
                    return

                # Check if the selected format is in the list
                if any(f['format_id'] == fmt for f in formats):
                    break
                else:
                    print("Invalid format id. Please try again.")

            ydl_opts = {
                'format': fmt,
                'outtmpl': os.path.join('videos', '%(title)s.%(ext)s')
            }

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            print("[*] Downloaded successfully!")

    except Exception as e:
        print(f"[!] An error occurred: {e}")