from __future__ import unicode_literals
import youtube_dl
import glob

links = open("links.txt", "rb")
list1 = [] 
list2 = []

for l in links.readlines():
    link = l.rstrip()
    link = l.decode()
    vid =  link.split("=")[-1] #For Web Links
    #vid =  link.split("/")[-1] #For Mobile Links
    list1.append(vid)
list1 = [s.rstrip() for s in list1]


for mp3 in glob.glob("*.mp3"):
    vid = mp3.split('.mp3')[0]
    vid = vid[-11:]
    list2.append(vid)


count = -1
for link in list1:
    count += 1
    print(count + 1)
    if link not in list2:
        print("Downloading " + link)
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
    else:
        print("Already Downloaded" ,list1[count])

