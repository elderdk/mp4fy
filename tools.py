def human_size(bytes, units=[" bytes", "KB", "MB", "GB", "TB", "PB", "EB"]):
    """Returns a human readable string representation of bytes

    https://stackoverflow.com/questions/1094841/get-human-readable-version-of-file-size
    """
    return str(bytes) + units[0] if bytes < 1024 else human_size(bytes >> 10, units[1:])


if __name__ == "__main__":
    print(human_size(1000000000))
