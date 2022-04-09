import pygame

# Default button images/pygame.Surfaces.
IMAGE_NORMAL_COLOR = 'white on dodgerblue1'
IMAGE_HOVER_COLOR = 'white on lightskyblue'
IMAGE_DOWN_COLOR = 'white on aquamarine1'

# Screen dimensions
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600

TYPO_DEFAULT_SIZE = 20

BASE_URL = "C:/projects/soundpyd"
SOUNDS_DIR = f"{BASE_URL}/sounds"
IMG_DIR = f"{BASE_URL}/img_resized"


pygame.init()
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption("Soundpyd")

the_buttons = [
    {
        "name": "cavern",
        "coords": (200, 300),
        "color": IMAGE_NORMAL_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/SC.mp3",
        "img": f"{IMG_DIR}/cavern_rs.png",
    },
]


def create_sound(url):
    return pygame.mixer.Sound(f"{url}")


def toggle_sound(b, is_playing, soundname, sound, fade_time=4000):
    if b.collidepoint(pygame.mouse.get_pos()) and is_playing:
        pygame.mixer.Sound.fadeout(sound, fade_time)
        print(f"Stop sound : {soundname}")
        return False
    elif b.collidepoint(pygame.mouse.get_pos()) and not is_playing:
        print(f"Play sound : {soundname}")
        pygame.mixer.Sound.play(sound, fade_ms=fade_time)
        return True
    else:
        return is_playing


def menu(buttons):
    """ This is the menu that waits you to click the buttons to start playing sounds"""

    sounds = dict()
    is_playing = dict()

    for b in buttons:
        b_name = b["name"]
        is_playing[b_name] = False
        sounds[b_name] = create_sound(b["url"])
        print(is_playing[b_name])

    while True:
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                for b in buttons:
                    pass

            elif event.type == pygame.MOUSEMOTION:
                for b in buttons:
                    pass

            elif event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()


if __name__ == "__main__":
    menu(the_buttons)
