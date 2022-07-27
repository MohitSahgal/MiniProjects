import pytube

print("Hello Darling")
link = input("Enter url")
yt = pytube.YouTube(link)
yt.streams.first().download()
print('Downloaded', link)
