from yt_dlp import YoutubeDL

def download_video(url):
    print("[*] Fetching available formats...")
    
    with YoutubeDL() as ydl:
        try:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [info_dict])

            if not formats:
                print("[!] No available formats found.")
                return

            for f in formats:
                print(f"{f['format_id']}: {f['format_note']} - {f.get('resolution', 'Unknown resolution')}")

            fmt = input("[*] Enter format id: ")

            # Check if the selected format is in the list
            if not any(f['format_id'] == fmt for f in formats):
                print("Invalid format selected.")
                return

            ydl_opts = {
                'format': fmt,
                'outtmpl': 'videos/%(title)s.%(ext)s'
            }

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            print("[*] Downloaded successfully!")

        except Exception as e:
            print(f"[!] An error occurred: {e}")

