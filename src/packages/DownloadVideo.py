from yt_dlp import YoutubeDL
import os

def download_video(url):
    print("\n[*] Fetching available formats...")
    
    try:
        with YoutubeDL() as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [info_dict])

            if not formats:
                print("[!] No available formats found.")
                return

            print("[*] Available formats:")
            for f in formats:
                print(f"{f['format_id']}: {f['format_note']} - {f.get('resolution', 'Unknown resolution')}")

            fmt = None
            while True:
                fmt = input("\n[*] Enter format id (or 'q' to quit): ").strip()
                if fmt.lower() == 'q':
                    print("[*] Exiting...")
                    return

                if any(f['format_id'] == fmt for f in formats):
                    break
                print("[!] Invalid format id. Please try again.")

            ydl_opts = {
                'format': fmt,
                'outtmpl': os.path.join('videos', '%(title)s.%(ext)s')
            }

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            print("\n[*] Downloaded successfully!")

    except Exception as e:
        print(f"\n[!] An error occurred: {e}")
