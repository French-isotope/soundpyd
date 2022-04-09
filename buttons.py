# Default button images/pygame.Surfaces.
IMAGE_NORMAL_COLOR = 'white on dodgerblue1'
IMAGE_HOVER_COLOR = 'white on lightskyblue'
IMAGE_DOWN_COLOR = 'white on aquamarine1'

TYPO_DEFAULT_SIZE = 20

BASE_URL = "C:/projects/soundpyd"
SOUNDS_DIR = f"{BASE_URL}/sounds"


buttons_needed = [
    {
        "name": "growl",
        "coords": (400, 300),
        "color": IMAGE_NORMAL_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/MSE.mp3",
    },
    {
        "name": "war",
        "coords": (300, 300),
        "color": IMAGE_NORMAL_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/FSW.mp3",
    },
    {
        "name": "cavern",
        "coords": (200, 300),
        "color": IMAGE_NORMAL_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/SC.mp3",
    },
    {
        "name": "house_with_fire",
        "coords": (000, 300),
        "color": IMAGE_NORMAL_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/house_with_fire.mp3",
    },
    {
        "name": "joy_festival",
        "coords": (400, 0),
        "color": IMAGE_NORMAL_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/joy_festival.mp3",
    },
]