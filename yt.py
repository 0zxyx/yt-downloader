from __future__ import unicode_literals
import youtube_dl

while True:
    link = str(input("Enter link: "))
    data = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '128',
                }],
            }
    try:
        with youtube_dl.YoutubeDL(data) as yt:
            yt.download([link])
    except:
        print("\n"  "We Couldn't Download: " + link)

