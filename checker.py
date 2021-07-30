import glob

links = open("links.txt", "rb")
list1 = []
list2 = []

for l in links.readlines():
    link = l.rstrip()
    link = l.decode()
    vid =  link.split("=")[-1]
    #vid =  link.split("/")[-1]
    list1.append(vid)
list1 = [s.rstrip() for s in list1]


for file in glob.glob("*.mp3"):
    vid = file.split('.mp3')[0]
    vid = vid[-11:]
    list2.append(vid)


new_list = list(set(list1).difference(list2))

count = -1
for i in new_list:
    count += 1
    print(("https://www.youtube.com/watch?v=" + new_list[count]))
