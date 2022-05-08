# importing the module
from pytube import YouTube
import pytube
import os


#from future import unicode_literals
#import youtube_dl

#ydl_opts = {    'format': 'bestaudio/best',    'postprocessors': [{        'key': 'FFmpegExtractAudio',        'preferredcodec': 'mp3',        'preferredquality': '192',    }],}
#ydl_opts = {}

#with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#    ydl.download(['https://www.youtube.com/watch?v=-8U4tTlG5n4&ab_channel=MichaelGhelfiStudios'])


# where to save
SAVE_PATH = "C:\\test_yt_dl"  # to_do

# link of the video to be downloaded
url = "https://youtu.be/gcPSA3sUilc"
url = "https://youtu.be/b3kUHCpF7VI"

yt = YouTube(url)

youtube = pytube.YouTube(url)

print(youtube.streams)

video = youtube.streams.get_by_itag(140)
full_filename = video.default_filename
filename = full_filename.split('.')[0].replace(' ','_')

mp4_file = os.path.join(SAVE_PATH, f"{filename}.mp4")
#mp4_file = os.path.join(SAVE_PATH, "D_Ambience_-_Full_Scale_War.mp4")

video.download(filename=mp4_file)

mp3_file = os.path.join(SAVE_PATH, f"{filename}.mp3")

cmd = "ffmpeg -i {} -vn {}".format(mp4_file, mp3_file)

os.system(cmd)

#os.system("afplay {}".format(mp3_file))
#video = VideoFileClip(os.path.join(SAVE_PATH, full_filename))
#video.audio.write_audiofile(os.path.join(SAVE_PATH, f"{filename}.mp3"))
