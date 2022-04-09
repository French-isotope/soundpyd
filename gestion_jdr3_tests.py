import pygame

# Default button images/pygame.Surfaces.
IMAGE_NORMAL_COLOR = 'white on dodgerblue1'
IMAGE_HOVER_COLOR = 'white on lightskyblue'
IMAGE_DOWN_COLOR = 'white on aquamarine1'

# Screen dimensions
SCREEN_HEIGHT = 840
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
        "color": IMAGE_NORMAL_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/SC.mp3",
        "img": f"{IMG_DIR}/cavern_rs.png",
    },
    {
        "name": "house_fire",
        "color": IMAGE_NORMAL_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/house_with_fire.mp3",
        "img": f"{IMG_DIR}/house_fire_rs.png",
    },
    {
        "name": "house_fire2",
        "color": IMAGE_NORMAL_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/house_with_fire.mp3",
        "img": f"{IMG_DIR}/house_fire_rs.png",
    },
    {
        "name": "house_fire4",
        "color": IMAGE_NORMAL_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/house_with_fire.mp3",
        "img": f"{IMG_DIR}/house_fire_rs.png",
    },
    {
        "name": "cavern1",
        "color": IMAGE_NORMAL_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/SC.mp3",
        "img": f"{IMG_DIR}/cavern_rs.png",
    },
    {
        "name": "house_fire1",
        "color": IMAGE_NORMAL_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/house_with_fire.mp3",
        "img": f"{IMG_DIR}/house_fire_rs.png",
    },
    {
        "name": "house_fire21",
        "color": IMAGE_NORMAL_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/house_with_fire.mp3",
        "img": f"{IMG_DIR}/house_fire_rs.png",
    },
    {
        "name": "house_fire41",
        "coords": (10, 700),
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


def button(coords, size, ic, ac, img, index, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = pygame.Rect(coords, size)

    on_button = rect.collidepoint(mouse)
    if on_button:
        pygame.draw.rect(screen, ac, rect)
#        screen.blit(imgon, imgon.get_rect(center = rect.center))
    else:
        pygame.draw.rect(screen, ic, rect)
        font = pygame.font.Font(None, 40)
        text = font.render(index, True, pygame.Color(0, 255, 0, 255))
        text_rect = text.get_rect(center=rect.center)
        screen.blit(img, img.get_rect(center=rect.center))
        screen.blit(text, text_rect)

    if on_button:
        if click[0] == 1 and action!= None:
            if action == "continue":
                print("cool !")


#image_on = pygame.image.load(f'{BASE_URL}/img_resized/swamps_rs.png').convert_alpha()

SOUND_ON = pygame.Color(0, 255, 0, 255)
SOUND_OFF = pygame.Color(255, 0, 0, 255)
REQUIRED_WIDTH = 105
REQUIRED_HEIGHT = 85
BORDER = 5


REQUIRED_SIZE = (REQUIRED_WIDTH, REQUIRED_HEIGHT)


def first_image_on_x(index):
    return index == 0


def image_will_be_out_of_screen(pos_x, width, border, screen_width):
    return (pos_x + width + border) > screen_width


def menu(buttons):
    """ This is the menu that waits you to click the buttons to start playing sounds"""

    sounds = dict()
    is_playing = dict()

    x_index = 0
    y_index = 0

    pos_y = BORDER
    pos_x = BORDER

    for index, b in enumerate(buttons):
        b_name = b["name"]
        is_playing[b_name] = False
        sounds[b_name] = create_sound(b["url"])
        image = pygame.image.load(f'{b["img"]}').convert_alpha()

        if "coords" in b:
            (pos_x, pos_y) = b["coords"]

        else:
            if first_image_on_x(x_index):
                pos_x = BORDER
                x_index += 1

            elif not first_image_on_x(x_index) and image_will_be_out_of_screen(pos_x, REQUIRED_WIDTH, BORDER, SCREEN_WIDTH):
                pos_x = BORDER
                x_index = 0
                y_index += 1

            else:
                pos_x = BORDER + (x_index * REQUIRED_WIDTH) + (x_index * BORDER)
                x_index += 1

            if y_index > 0:
                pos_y = BORDER + (y_index * REQUIRED_HEIGHT) + (y_index * BORDER)


        button((pos_x, pos_y), REQUIRED_SIZE, SOUND_ON, SOUND_OFF, image, str(index),"continue")

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
