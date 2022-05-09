import pytube
import os
from pydub import AudioSegment

DOWNLOAD_PATH = "C:\\test_yt_dl\\Download"
SAVE_PATH = "C:\\test_yt_dl"  # to_do

filename = "Spring_Forest_Sounds_and_Relaxing_Bird_Singing_for_Sleeping"
mp4_file = os.path.join(DOWNLOAD_PATH, f"{filename}.mp4")

# Convert to mp3
given_audio = AudioSegment.from_file(mp4_file, format="mp4")

# Store as mp3
given_audio.export(f"{SAVE_PATH}/{filename}.mp3", format="mp3")


