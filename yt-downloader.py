from __future__ import unicode_literals
import youtube_dl

links = open("links.txt", "rb")

count=0
for l in links.readlines():
    link = l.rstrip()
    link = l.decode()
    count +=1
    print("\n" +str(count) + " Downloading: " +  link)
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
