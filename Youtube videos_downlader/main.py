from pytube import YouTube
url = input("Enter your url here ")
yt = YouTube(url)

streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
for stream in streams:
    print(stream)

stream.download(output_path='C:/Users/sande/Downloads', filename='video.mp4')
print("Downlad Completed ")