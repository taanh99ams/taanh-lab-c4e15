from youtube_dl import YoutubeDL


# Download two videos from Youtube
dl = YoutubeDL()
dl.download(["https://www.youtube.com/watch?v=ZhKnSp2cX98","https://www.youtube.com/watch?v=8MPbR6Cbwi4"])

# Search and then download an audio from Youtube videos
options = {
    "format": "bestaudio/audio"
}


dl = YoutubeDL(options)
dl.download(["https://www.youtube.com/watch?v=by3yRdlQvzs"])

#Search according to key words
options = {
    "default_search": "ytsearch",
    "max_downloads": 1
}
dl = YoutubeDL(options)
dl.download(["Mơ Vũ Cát Tường"])

# Search and then download an audio from Youtube video
options = {
    "format": "bestaudio/audio",
    "default_search": "ytsearch",
    "max_downloads": 1
}

dl = YoutubeDL(options)
dl.download(["We are young"])
