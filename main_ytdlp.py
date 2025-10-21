# Alternative version using yt-dlp for downloading videos

import yt_dlp

# Function to download video using yt-dlp

def download_video(url):
    ydl_opts = {'format': 'best'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage

download_video('https://www.tiktok.com/@example/video/123456789')