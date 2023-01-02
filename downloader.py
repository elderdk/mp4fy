from yt_dlp import YoutubeDL
from option_generator import get_option


def download(url):

    with YoutubeDL() as ydl:
        info = ydl.extract_info(url, download=False)
        filename, options = get_option(info)

    with YoutubeDL(options) as ydl:
        ydl.download(url)
        
    return filename, info