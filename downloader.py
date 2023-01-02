from yt_dlp import YoutubeDL
from option_generator import get_option
from exceptions import VideoTooBigError


def download(url):

    with YoutubeDL() as ydl:
        info = ydl.extract_info(url, download=False)
        filename, options = get_option(info)


    if info['filesize_approx'] > 1024000000:
        raise VideoTooBigError("Sorry! The video is too big!")

    with YoutubeDL(options) as ydl:
        ydl.download(url)
    
    streamlined_info = {
        "title": info['title']
    }
    
    
    return filename, streamlined_info
