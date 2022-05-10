import pygame
import pygame_textinput
import random
import json
from configparser import ConfigParser


parser = ConfigParser()
parser.read('config.ini')

# Default button images/pygame.Surfaces.
TEXT_COLOR = 'white'

# Screen dimensions
SCREEN_WIDTH = int(parser.get('SCREEN', 'WIDTH'))
SCREEN_HEIGHT = int(parser.get('SCREEN', 'HEIGHT'))

DICE_HEIGHT = 200

if SCREEN_WIDTH < 800 or SCREEN_HEIGHT < 600:
    print("\nError: Screen is too little, minimum is 800*600\n")
    exit(1)


TYPO_SIZE = int(parser.get('TEXT', 'SIZE'))

COLOR_SOUND_ON = pygame.Color(0, 255, 0, 255)
COLOR_SOUND_OFF = pygame.Color(255, 0, 0, 255)
COLOR_OVER = pygame.Color(0, 125, 125, 255)

COLOR_DICE_ZONE = pygame.Color(46, 46, 46, 0)

REQUIRED_WIDTH = int(parser.get('BUTTONS', 'REQUIRED_WIDTH'))
REQUIRED_HEIGHT = int(parser.get('BUTTONS', 'REQUIRED_HEIGHT'))
BORDER = int(parser.get('BUTTONS', 'BORDER'))


DICES = bool(parser.get('BUTTONS', 'DICES'))

if DICES:
    print("Dices are activated")


REQUIRED_SIZE = (REQUIRED_WIDTH, REQUIRED_HEIGHT)


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Soundpyd")

# Opening JSON file
file = open(f"./config.json")

# returns JSON object as datastructure
the_buttons = json.load(file)

random_boxes = [{"type":"d3"}, {"type":"d4"}, {"type":"d6"}, {"type":"d8"}, {"type":"d10"}, {"type":"d12"}, {"type":"d14"}, {"type":"d16"}, {"type":"d20"}, {"type":"d24"}, {"type":"d30"}, {"type":"d60"}, {"type":"d100"}]

def init_sound(url):
    return pygame.mixer.Sound(f"{url}")


def init_image(url):
    return pygame.image.load(f'{url}').convert_alpha()


def toggle_sound(is_playing, soundname, sound, channel, fade_time=4000, nb_loop=0):
    if is_playing:
        channel.fadeout(fade_time)
        print(f"Stop sound : {soundname}")
        return False
    elif not is_playing:
        print(f"Play sound : {soundname}")
        channel.play(sound, fade_ms=fade_time, loops=nb_loop)
        return True
    else:
        return is_playing


def create_button(coords, size, color, img, screen, text=""):
    rect = pygame.Rect(coords, size)
    pygame.draw.rect(screen, color, rect)
    screen.blit(img, img.get_rect(center=rect.center))
    if len(text) > 0:
        font = pygame.font.SysFont('Arial', 20)
        screen.blit(font.render(f"{text}", True, (255, 0, 0)), img.get_rect(center=rect.center))
    return rect


def update_button(rect, color, img, screen, text=""):
    pygame.draw.rect(screen, color, rect)
    screen.blit(img, img.get_rect(center=rect.center))
    if len(text) > 0:
        font = pygame.font.SysFont('Arial', 20)
        screen.blit(font.render(f"{text}", True, (255,0,0) ), img.get_rect(center=rect.center))
    return rect


def create_dice_zone(coords, size, color, screen):
    rect = pygame.Rect(coords, size)
    pygame.draw.rect(screen, color, rect)
    return rect


def create_dice(pos_x, pos_y, screen):
    # (A, B, C)
    #      A
    #  C
    #      B
    rect_w = 80
    rect_h = 100
    x_shift_1 = pos_x + (rect_w / 2) - BORDER*2
    x_shift_2 = pos_x + (rect_w / 2) + BORDER*2
    triangle_w = 16
    triangle_h = 16
    high_y = 80 - BORDER
    low_y = high_y + triangle_h
    middle_y = high_y + triangle_h/2

    rect = pygame.Rect((pos_x, pos_y,), (rect_w, rect_h))
    pygame.draw.rect(screen, (100, 70, 70), rect)
    pygame.draw.polygon(surface=screen, color=(150, 150, 0), points=[(x_shift_1, pos_y + high_y), (x_shift_1, pos_y + low_y), (x_shift_1 - triangle_w, pos_y + middle_y)])
    pygame.draw.polygon(surface=screen, color=(150, 150, 0), points=[(x_shift_2, pos_y + high_y), (x_shift_2, pos_y + low_y), (x_shift_2 + triangle_w, pos_y + middle_y)])


def update_rand_textbox(rect, color, img, screen, text=""):
    pygame.draw.rect(screen, color, rect)
    screen.blit(img, img.get_rect(center=rect.center))
    if len(text) > 0:
        font = pygame.font.SysFont('Arial', 20)
        screen.blit(font.render(f"{text}", True, (255,0,0) ), img.get_rect(center=rect.center))
    return rect


def first_image_on_x(index):
    return index == 0


def image_will_be_out_of_screen(width, border, x_index, screen_width):
    return (border + (x_index * width) + (x_index * border) + width) > screen_width


def create_sound_channel(id_channel):
    return pygame.mixer.Channel(id_channel)


def set_max_channels_number(number):
    pygame.mixer.set_num_channels(number)


def menu(buttons_wanted, dices, screen_height):
    """ This is the menu that waits you to click the buttons to start playing sounds"""

    is_playing = dict()
    sounds = dict()
    images = dict()
    buttons = dict()
    channels = dict()

    x_index = 0
    y_index = 0

    pos_x = BORDER
    pos_y = BORDER

    # Create one channel for each sound to play
    set_max_channels_number(len(buttons_wanted))

    for index, b in enumerate(buttons_wanted):
        b_name = index
        if "name" in b:
            button_title = b["name"]
        else:
            button_title = ""
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

            elif not first_image_on_x(x_index) and image_will_be_out_of_screen(REQUIRED_WIDTH, BORDER, x_index, SCREEN_WIDTH):
                pos_x = BORDER
                x_index = 1
                y_index += 1

            else:
                pos_x = BORDER + (x_index * REQUIRED_WIDTH) + (x_index * BORDER)
                x_index += 1

            if y_index > 0:
                pos_y = BORDER + (y_index * REQUIRED_HEIGHT) + (y_index * BORDER)


        #init all buttons
        buttons[b_name] = create_button((pos_x, pos_y), REQUIRED_SIZE, COLOR_SOUND_OFF, images[b_name], screen, f"{button_title}")

        create_dice_zone((BORDER, SCREEN_HEIGHT - DICE_HEIGHT), (SCREEN_WIDTH - BORDER*2, DICE_HEIGHT - BORDER), COLOR_DICE_ZONE, screen)
        create_dice(BORDER * 2, screen_height + BORDER, screen)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for index, b in enumerate(buttons_wanted):
                    b_name = index
                    if "name" in b:
                        button_title = b["name"]
                    else:
                        button_title = ""
                    sound = sounds[b_name]
                    button = buttons[b_name]
                    channel = channels[b_name]
                    playing = channel.get_busy()

                    if "nb_loop" in b:
                        nb_loop = b["nb_loop"]
                    else:
                        nb_loop = 0

                    if button.collidepoint(pygame.mouse.get_pos()):
                        toggle_sound(playing, button_title, sound, channel, nb_loop=nb_loop)
                        if playing:
                            buttons[b_name] = update_button(button, COLOR_SOUND_ON, images[b_name], screen, f"{button_title}")
                        else:
                            buttons[b_name] = update_button(button, COLOR_SOUND_OFF, images[b_name], screen, f"{button_title}")
                    pygame.display.update()

            elif event.type == pygame.MOUSEMOTION:
                for index, b in enumerate(buttons_wanted):
                    b_name = index
                    if "name" in b:
                        button_title = b["name"]
                    else:
                        button_title = ""
                    button = buttons[b_name]
                    channel = channels[b_name]
                    playing = channel.get_busy()

                    if button.collidepoint(pygame.mouse.get_pos()) and not playing:
                        buttons[b_name] = update_button(button, COLOR_OVER, images[b_name], screen, f"{button_title}")
                    elif button.collidepoint(pygame.mouse.get_pos()) and playing:
                        buttons[b_name] = update_button(button, COLOR_SOUND_ON, images[b_name], screen, f"{button_title}")

                pygame.display.update()

            elif event.type == pygame.QUIT:
                pygame.quit()

        for index, b in enumerate(buttons_wanted):
            b_name = index
            if "name" in b:
                button_title = b["name"]
            else:
                button_title = ""
            button = buttons[b_name]
            channel = channels[b_name]

            if not channel.get_busy() and not button.collidepoint(pygame.mouse.get_pos()):
                buttons[b_name] = update_button(button, COLOR_SOUND_OFF, images[b_name], screen, f"{button_title}")

            elif channel.get_busy() and not button.collidepoint(pygame.mouse.get_pos()):
                buttons[b_name] = update_button(button, COLOR_SOUND_ON, images[b_name], screen, f"{button_title}")

            elif channel.get_busy() and button.collidepoint(pygame.mouse.get_pos()):
                buttons[b_name] = update_button(button, COLOR_SOUND_ON, images[b_name], screen, f"{button_title}")


        pygame.display.update()


if __name__ == "__main__":

    if DICES:
        height_screen = SCREEN_HEIGHT - DICE_HEIGHT
    else:
        height_screen = SCREEN_HEIGHT

    menu(the_buttons, DICES, height_screen)
