from __future__ import unicode_literals
import youtube_dl

links = open("links.txt", "rb")

for l in links.readlines():
    link = l.rstrip()
    link = l.decode()
    data = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '128',
                }],
            }
    with youtube_dl.YoutubeDL(data) as yt:
        yt.download([link])

