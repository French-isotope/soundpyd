import pytube
import requests
import os
from pydub import AudioSegment

# where to save
DOWNLOAD_PATH = "C:\\test_yt_dl\\Download"
SAVE_PATH = "C:\\test_yt_dl"  # to_do

# link of the video to be downloaded
url = "https://youtu.be/gcPSA3sUilc"
url = "https://youtu.be/b3kUHCpF7VI"

urls = ["https://www.youtube.com/watch?v=b3kUHCpF7VI",
        "https://youtu.be/S1ABDC7Tt1Y",
        "https://youtu.be/J1iRvyHWgdI",
        "https://www.youtube.com/watch?v=wjfNNXsaSBs",
        "https://www.youtube.com/watch?v=168NBT32f44",
        "https://youtu.be/F76nbf-o7RA",
        "https://youtu.be/oD9ZUXDEoyA",
        "https://youtu.be/jndrGgGqibI"]

urls = ["https://youtu.be/izGwDsrQ1eQ"]
urls = ["https://www.youtube.com/watch?v=BSFbKIW8HGs"]
# mountains
urls = ["https://www.youtube.com/watch?v=mtmB30Prqvs"]
urls = [        # footsteps in a dungeon
        "https://youtu.be/1s16cB1-PJ0",
        # footsteps in snow
        "https://youtu.be/8q48zF7ZhkU"
        # footsteps in forest
        "https://youtu.be/-f9MebkiwAY"
        # footsteps on ice
        "https://youtu.be/gkUP_u0PwuE"
        # Tavern ambience : 
        "https://www.youtube.com/watch?v=_4OfDN6X9oc"
        # Forest and birds:
        "https://youtu.be/xNN7iTA57jM",
        # Medieval fest :
        "https://www.youtube.com/watch?v=gcPSA3sUilc",
        # Port :
        "https://youtu.be/t0AmfPQMs4k",
        # Ambiance énervée
        "https://www.youtube.com/watch?v=UNibrdgIVSw",
        # Ambiance construction site
        "https://youtu.be/Ly9Ci1lTAnY",
        # Charpentier :
        "https://youtu.be/or7IiL1i5sE",
        # blacksmith
        "https://youtu.be/lxKVT1r4sgU",
        # Marketplace
        "https://youtu.be/x2UulCWGess",
        # Damp cavern
        "https://youtu.be/3Hwr_BaekgM",
        # Catacombs
        "https://youtu.be/WPpVMmTt74Q",
        # Dungeon
        "https://youtu.be/wScEFaoqwPM",
        # Horse and Cart on road
        "https://youtu.be/65TV8jhp9Ns",
        # Ship cabin
        "https://youtu.be/D4juEBifIMk",
        # Chambers Of Torture
        "https://youtu.be/PzYZQySL8Ac",
        # Thorny swamps
        "https://youtu.be/PWJCBbZOTiI",
        # Hell
        "https://youtu.be/JzVIkY5tKcE",
        # Cultists
        "https://youtu.be/rrE1EFE5MqI",
        # Birds
        "https://youtu.be/0NyQTqpsh_8",
        # Angry crowd
        "https://youtu.be/UNibrdgIVSw",
        # Underwater
        "https://youtu.be/aGmMjk6qipk",
        # Growling 1
        "https://youtu.be/-S_T5Xa0XtM",
        # Dragon roar
        "https://youtu.be/2adxFG82H70",
        # master boss dragon effect
        "https://youtu.be/FGjAH6pSaFc",
        # Dragon roar 2
        "https://youtu.be/-EkqIVRbdm4",
        # spider chasing
        "https://youtu.be/u9MdIrVDj1k"
        # crawling bugs
        "https://youtu.be/-oEkmzXVeaE",
        # Skinwalker
        "https://youtu.be/cpk5UyA2mSE",
        # Distant growling creature
        "https://youtu.be/_6j0_YQG0o8",
        # growling creature from subnautica
        "https://youtu.be/EpEQWefFa2w",
        # roar sound effect
        "https://youtu.be/n6q7Uaro_2k",
        # Mazellmi on yt
        # Banshee
        "https://youtu.be/P8kolyZmRN4",
        # Remain indoor sounds
        "https://youtu.be/arYMLcv49vE",
        # Growling
        "https://youtu.be/WpuQNXmHvSk",
        # scp1
        "https://youtu.be/17FEVgAQrdA",
        # Azatoth
        "https://youtu.be/m4_i41eAPw4",
        # SCP-2317-K sounds
        "https://youtu.be/apiiKUdXTL4",
        # Almataha-ha sounds
        "https://youtu.be/hrx7rCqjt_g",
        # Minos sound
        "https://youtu.be/dfdi_sHl_EE",
        # Day 2027 (misty guest 3) sounds
        "https://youtu.be/IC2e8YaTBcw",
        # Blue fog monster sounds
        "https://youtu.be/YDHhzs7xEdA",
        # Root head sounds
        "https://youtu.be/4_I3MWZ2igs",
        # La llorona sounds
        "https://youtu.be/El1OwjGSf3M",
        # Stick bug sounds
        "https://youtu.be/svpFV4sYiXU",
        # Gorefield
        "https://youtu.be/aFIZFy7np8Y",
        # country giant sounds (tall beeves)
        "https://youtu.be/wBe0Ti_L-Ts",
        # Golden shade sounds
        "https://youtu.be/5xdfrnmEiRg",
        # The shadow sounds
        "https://youtu.be/BxUVdBxJj0o",
        # SCP-3199 sounds
        "https://youtu.be/vyyoFTI4BH4",
        # The EEL PAS MAL ++
        "https://youtu.be/rlN7qlQVSIk",
        # Best of Gevaudan
        "https://youtu.be/60UReZiDax0",
        # Werewolf sounds
        "https://youtu.be/3bgSzrYpg4M",
        # SCP-610 Sounds
        "https://youtu.be/RhfAZmZlYCY",
        # Weavile sounds
        "https://youtu.be/L6AqEy5YSus",
        # The giant with red dots sounds
        "https://youtu.be/sadzwj5An4c",
        # Nurpo sounds
        "https://youtu.be/_LJvCHZU_mU",
        # Bridge worm sounds
        "https://youtu.be/Vuc14Aq7K-I",
        # Big Charlie sounds
        "https://youtu.be/Qfgn4ET7wNY",
        # Cartoon cat sound/voice v1.0 / voix distantes
        "https://youtu.be/JmiPxW0FW5M",

        # Soundbox
        # Dead Space monsters
        "https://youtu.be/iLCvsoliKlU",

        # others
        "https://www.youtube.com/watch?v=mtmB30Prqvs",
        "https://youtu.be/4ZowPmPCZ6I",
        "https://youtu.be/vplX-qr4AIE",
        "https://youtu.be/uNF2fi1eUXY",


        ]


for url in urls:

    # Target mp4 from youtube
    youtube = pytube.YouTube(url)
    print(youtube.streams)
    video = youtube.streams.get_by_itag(140)

    # get filename and download
    full_filename = video.default_filename
    filename = full_filename.split('.')[0].replace(' ','_')
    print(filename)
    mp4_file = os.path.join(DOWNLOAD_PATH, f"{filename}.mp4")
    video.download(filename=mp4_file)

    # Download yt thumbnails
    thumb_url = pytube.YouTube(f'{url}').thumbnail_url
    response = requests.get(thumb_url)
    file = open(f"{SAVE_PATH}\\Pictures\\{filename}.png", "wb")
    file.write(response.content)
    file.close()


    # Convert to mp3
    given_audio = AudioSegment.from_file(mp4_file, format="mp4")

    # Store as mp3
    given_audio.export(f"{SAVE_PATH}/{filename}.mp3", format="mp3")


