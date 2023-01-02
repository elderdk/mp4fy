def get_option(info):
    
    filename = "/tmp/" + info.get('title') + '.mp4'
    
    options = {
        "format": "mp4",
        "outtmpl": {'default': filename}
    }
    
    return filename, options