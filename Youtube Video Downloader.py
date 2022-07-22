import pytube

link = input("Enter url")
yt = pytube.YouTube(link)
yt.streams.first().download()
print('Downloaded', link)
