from yt_dlp import YoutubeDL
from option_generator import get_option
from exceptions import VideoTooBigError
from tools import human_size


def download(url):

    with YoutubeDL({"format": "mp4"}) as ydl:
        info = ydl.extract_info(url, download=False)
        filename, options = get_option(info)

    video_size = info["filesize_approx"]
    if video_size > 1024000000:
        raise VideoTooBigError(
            f"Sorry! The video is too big! ({human_size(video_size)})"
        )

    with YoutubeDL(options) as ydl:
        ydl.download(url)

    streamlined_info = {
        "title": info["title"],
        "thumbnail": info["thumbnail"],
        "original_url": info["original_url"],
        "description": info["description"][:100],
        "duration_string": info["duration_string"]
    }

    return filename, streamlined_info
