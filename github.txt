import pygame
import pygame_textinput
import random
import json
from configparser import ConfigParser
import math

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

COLOR_DICE_ZONE = pygame.Color(146, 146, 146, 0)

REQUIRED_WIDTH = int(parser.get('BUTTONS', 'REQUIRED_WIDTH'))
REQUIRED_HEIGHT = int(parser.get('BUTTONS', 'REQUIRED_HEIGHT'))
BORDER = int(parser.get('BUTTONS', 'BORDER'))


dices_str = parser.get('BUTTONS', 'DICES')

if dices_str == "False" or dices_str == "":
    DICES = False
else:
    DICES = True

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

all_dices = ["C:\projects\soundpyd\dices\d2.png",
         "C:\projects\soundpyd\dices\d3.png",
         "C:\projects\soundpyd\dices\d4.png",
         "C:\projects\soundpyd\dices\d6.png",
         "C:\projects\soundpyd\dices\d8.png",
         "C:\projects\soundpyd\dices\d10.png",
         "C:\projects\soundpyd\dices\d12.png",
         "C:\projects\soundpyd\dices\d20.png",
         "C:\projects\soundpyd\dices\d100.png",
         "C:\projects\soundpyd\dices\d_perso.png"]



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
    pygame.draw.rect(screen, color, rect, width=1)
    return rect


def create_dice(pos_x, pos_y, screen, rect_w, rect_h, filename):
    # (A, B, C)
    #      A
    #  C
    #      B
    rect_color = (90, 90, 90)
    buttons_color = (120, 120, 120)
    x_shift_1 = pos_x + (rect_w / 2) - BORDER*2
    x_shift_2 = pos_x + (rect_w / 2) + BORDER*2
    triangle_w = 16
    triangle_h = 16
    high_y = rect_w - BORDER
    low_y = high_y + triangle_h
    middle_y = high_y + triangle_h/2
    # text setting
    rect = pygame.Rect((pos_x, pos_y), (rect_w, rect_h))
    pygame.draw.rect(screen, rect_color, rect)

    # Blit image of the dice
    picture = pygame.image.load(filename)
    picture = pygame.transform.scale(picture, (rect_w / 1.5, rect_w / 1.5))
    center_rect = picture.get_rect(center=rect.center)
    screen.blit(picture, (center_rect.left, center_rect.top - 15))

    pos_x_a1 = x_shift_1
    pos_y_a1 = pos_y + high_y
    pos_x_b1 = x_shift_1
    pos_y_b1 = pos_y + low_y
    pos_x_c1 = x_shift_1 - triangle_w
    pos_y_c1 = pos_y + middle_y
    center_x1 = pos_x_c1 + (pos_x_a1 - pos_x_c1) / 2 + 2
    center_y1 = pos_y_c1 - 2
    font_obj = pygame.font.Font("C:\Windows\Fonts\impact.ttf", 20)

    less_arrow = pygame.draw.polygon(screen, buttons_color, points=[(pos_x_a1, pos_y_a1), (pos_x_b1, pos_y_b1), (pos_x_c1, pos_y_c1)])
    # draw the text onto the surface
    text_surface_obj = font_obj.render('-', True, rect_color)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (center_x1, center_y1)
    screen.blit(text_surface_obj, text_rect_obj)

    pos_x_a2 = x_shift_2
    pos_y_a2 = pos_y + high_y
    pos_x_b2 = x_shift_2
    pos_y_b2 = pos_y + low_y
    pos_x_c2 = x_shift_2 + triangle_w
    pos_y_c2 = pos_y + middle_y
    center_x2 = pos_x_a2 - (pos_x_a2 - pos_x_c2) / 2 - 3
    center_y2 = pos_y_c2
    font_obj = pygame.font.Font("C:\Windows\Fonts\impact.ttf", 16)

    more_arrow = pygame.draw.polygon(screen, buttons_color, points=[(pos_x_a2, pos_y_a2), (pos_x_b2, pos_y_b2), (pos_x_c2, pos_y_c2)])
    # draw the text onto the surface
    text_surface_obj = font_obj.render('+', True, rect_color)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (center_x2, center_y2)
    screen.blit(text_surface_obj, text_rect_obj)

    # Square between triangles
    size_square = pos_x_a2 - pos_x_a1 - 5
    size_square2 = pos_y_b1 - pos_y_a1
    print(f"la size {size_square} {size_square2}")
    rect = pygame.Rect((pos_x_a1 + 3, pos_y_a1 + 1), (size_square, size_square2))
    pygame.draw.rect(screen, (120, 120, 120), rect)



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

        if DICES:
            rect_w = ((SCREEN_WIDTH - BORDER * ( 4 + len(all_dices) - 1 ) ) / (len(all_dices)))
#            print(len(all_dices))
            print(rect_w)
            rect_h = rect_w * 1.20
            print(rect_h)
            shift_dice = rect_w + BORDER

            create_dice_zone((BORDER, SCREEN_HEIGHT - DICE_HEIGHT), (SCREEN_WIDTH - BORDER*2, DICE_HEIGHT - BORDER), COLOR_DICE_ZONE, screen)

            for index, dice in enumerate(all_dices):
                create_dice(BORDER * 2 + shift_dice * index, screen_height + BORDER, screen, rect_w, rect_h, dice)


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
