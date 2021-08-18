import pytube

url = "https://www.youtube.com/watch?v=j1MbEYhYj_Y"
yt = pytube.YouTube(url)
video = yt.streams.get_highest_resolution()
video.download("")
