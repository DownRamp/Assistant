from pytube import YouTube

# where to save
SAVE_PATH = "E:/"  # to_do

# link of the video to be downloaded
link = "https://www.youtube.com/watch?v=qCX2DPsHbM4"

try:
    yt = YouTube(link)
except:
    print("Connection Error")  # to handle exception

try:
    # downloading the video
    yt.streams.filter(progressive=True, file_extension='mp4')\
        .order_by('resolution').desc().first().download()
except:
    print("Some Error!")

print('Task Completed!')
