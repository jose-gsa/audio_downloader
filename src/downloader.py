import yt_dlp


def download_audio(url: str, output_path: str):

    ydl_opts = {
        "format": "bestaudio/best",  # best audio quality
        "postprocessors": [
            {  # FFmpeg config
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",  # define the final name
        "quiet": False,
        # 'noplaylist': True, Uncomment if you to download only 1 music
        "extractor_args": {"youtube": ["player_client=android"]},
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
