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
        "coords": (35, 75),
        "color": IMAGE_NORMAL_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/SC.mp3",
        "img": f"{IMG_DIR}/cavern_rs.png",
    },
    {
        "name": "house_fire",
        "coords": (200, 300),
        "color": IMAGE_NORMAL_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/house_with_fire.mp3",
        "img": f"{IMG_DIR}/house_fire_rs.png",
    },
    {
        "name": "house_fire2",
        "coords": (200, 300),
        "color": IMAGE_NORMAL_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/house_with_fire.mp3",
        "img": f"{IMG_DIR}/house_fire_rs.png",
    },
    {
        "name": "house_fire4",
        "coords": (200, 300),
        "color": IMAGE_NORMAL_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/house_with_fire.mp3",
        "img": f"{IMG_DIR}/house_fire_rs.png",
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


#def button(x, y, w, h, peri_off, peri_on):

def button(coords, size, ic, ac, img, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = pygame.Rect(coords, size)
    on_button = rect.collidepoint(mouse)
    if on_button:
        pygame.draw.rect(screen, ac, rect)
#        screen.blit(imgon, imgon.get_rect(center = rect.center))
    else:
        pygame.draw.rect(screen, ic, rect)
        screen.blit(img, img.get_rect(center = rect.center))

    if on_button:
        if click[0] == 1 and action!= None:
            if action == "continue":
                print("cool !")


#image_on = pygame.image.load(f'{BASE_URL}/img_resized/swamps_rs.png').convert_alpha()

SOUND_ON = pygame.Color(0, 255, 0, 255)
SOUND_OFF = pygame.Color(255, 0, 0, 255)
REQUIRED_WIDTH = 105
REQUIRED_HEIGHT = 85

REQUIRED_SIZE = (REQUIRED_WIDTH, REQUIRED_HEIGHT)


def first_image_on_axe(index):
    return index == 0


def menu(buttons):
    """ This is the menu that waits you to click the buttons to start playing sounds"""

    sounds = dict()
    is_playing = dict()

    for index, b in enumerate(buttons):
        b_name = b["name"]
        is_playing[b_name] = False
        sounds[b_name] = create_sound(b["url"])
        image = pygame.image.load(f'{b["img"]}').convert_alpha()
        if first_image_on_axe(index):
            pos_x = 10 + ( index * REQUIRED_WIDTH )
        else:
            pos_x = 10 + (index * REQUIRED_WIDTH) + ( 10 * index )
        pos_y = 10

        button((pos_x, pos_y), REQUIRED_SIZE, SOUND_ON, SOUND_OFF, image, "continue")

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

#            background = pygame.Surface((50, 50))
#            screen.blit(background, [0, 0])


        pygame.display.update()


if __name__ == "__main__":
    menu(the_buttons)
