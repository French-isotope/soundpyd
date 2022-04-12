import pygame

# Default button images/pygame.Surfaces.
TEXT_COLOR = 'white'

# Screen dimensions
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600

TYPO_DEFAULT_SIZE = 20

BASE_URL = "C:/projects/soundpyd"
SOUNDS_DIR = f"{BASE_URL}/sounds"
IMG_DIR = f"{BASE_URL}/img_resized"


COLOR_SOUND_ON = pygame.Color(0, 255, 0, 255)
COLOR_SOUND_OFF = pygame.Color(255, 0, 0, 255)
REQUIRED_WIDTH = 105
REQUIRED_HEIGHT = 85
BORDER = 5

REQUIRED_SIZE = (REQUIRED_WIDTH, REQUIRED_HEIGHT)


pygame.init()
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption("Soundpyd")

the_buttons = [
    {
        "name": "cavern",
        "color": TEXT_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/birds.mp3",
        "img": f"{IMG_DIR}/cavern_rs.png",
        "nb_loop": 20,
    },
    {
        "name": "house_fire",
        "color": TEXT_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/thunder.mp3",
        "img": f"{IMG_DIR}/house_fire_rs.png",
        "nb_loop": 2,
    },
    {
        "name": "house_fire2",
        "color": TEXT_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/door_squeak.mp3",
        "img": f"{IMG_DIR}/house_fire_rs.png",
    },
    {
        "name": "house_fire4",
        "color": TEXT_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/stream.mp3",
        "img": f"{IMG_DIR}/house_fire_rs.png",
    },
    {
        "name": "cavern1",
        "color": TEXT_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/door_squeak.mp3",
        "img": f"{IMG_DIR}/cavern_rs.png",
    },
    {
        "name": "house_fire1",
        "color": TEXT_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/stream.mp3",
        "img": f"{IMG_DIR}/house_fire_rs.png",
    },
    {
        "name": "house_fire21",
        "color": TEXT_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/birds.mp3",
        "img": f"{IMG_DIR}/house_fire_rs.png",
    },
    {
        "name": "house_fire41",
        "coords": (10, 700),
        "color": TEXT_COLOR,
        "size": TYPO_DEFAULT_SIZE,
        "url": f"{SOUNDS_DIR}/birds.mp3",
        "img": f"{IMG_DIR}/house_fire_rs.png",
    },
]


def init_sound(url):
    return pygame.mixer.Sound(f"{url}")


def init_image(url):
    return pygame.image.load(f'{url}').convert_alpha()


def toggle_sound(is_playing, soundname, sound, channel, fade_time=4000, nb_loop=0):
    if is_playing:
        # pygame.mixer.Sound.fadeout(sound, fade_time)
        channel.fadeout(fade_time)
        print(f"Stop sound : {soundname}")
        return False
    elif not is_playing:
        print(f"Play sound : {soundname}")
#        pygame.mixer.Sound.play(sound, fade_ms=fade_time, loops=nb_loop)
        channel.play(sound, fade_ms=fade_time, loops=nb_loop)
        return True
    else:
        return is_playing


def create_button(coords, size, color, img, screen):
    rect = pygame.Rect(coords, size)
    pygame.draw.rect(screen, color, rect)
    screen.blit(img, img.get_rect(center=rect.center))
    return rect


def update_button(rect, color, img, screen):
    pygame.draw.rect(screen, color, rect)
    screen.blit(img, img.get_rect(center=rect.center))
    return rect


def first_image_on_x(index):
    return index == 0


def image_will_be_out_of_screen(pos_x, width, border, screen_width):
    return (pos_x + width + border) > screen_width


def create_sound_channel(id_channel):
    return pygame.mixer.Channel(id_channel)


def set_max_channels_number(number):
    pygame.mixer.set_num_channels(number)


def menu(buttons_wanted):
    """ This is the menu that waits you to click the buttons to start playing sounds"""

    is_playing = dict()
    sounds = dict()
    images = dict()
    buttons = dict()
    channels = dict()

    x_index = 0
    y_index = 0

    pos_y = BORDER
    pos_x = BORDER

    set_max_channels_number(len(buttons_wanted))

    for index, b in enumerate(buttons_wanted):
        b_name = b["name"]
        is_playing[b_name] = False
        sounds[b_name] = init_sound(b["url"])
        images[b_name] = init_image(b["img"])
        channels[b_name] = create_sound_channel(index)

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

        #init all buttons
        buttons[b_name] = create_button((pos_x, pos_y), REQUIRED_SIZE, COLOR_SOUND_OFF, images[b_name], screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for index, b in enumerate(buttons_wanted):
                    b_name = b["name"]
                    sound = sounds[b_name]
                    button = buttons[b_name]
                    channel = channels[b_name]
                    if "nb_loop" in b:
                        nb_loop = b["nb_loop"]
                    else:
                        nb_loop = 0

                    if button.collidepoint(pygame.mouse.get_pos()):
                        is_playing[b_name] = toggle_sound(is_playing[b_name], b_name, sound, channel, nb_loop=nb_loop)
                        if is_playing[b_name]:
                            buttons[b_name] = update_button(button, COLOR_SOUND_ON, images[b_name], screen)
                        else:
                            buttons[b_name] = update_button(button, COLOR_SOUND_OFF, images[b_name], screen)

            elif event.type == pygame.MOUSEMOTION:
                for b in buttons:
                    pass

            elif event.type == pygame.QUIT:
                pygame.quit()

        for channel in channels:
            print(f"channel is busy : {channel}")
#            if channel.get_busy():
#                print(f"channel is busy : {channel}")
 #           else:
 #               print(f"channel is NOT busy : {channel}")

        pygame.display.update()


if __name__ == "__main__":
    menu(the_buttons)
