import pygame_textinput
import pygame
pygame.init()

"""
# Create TextInput-object
textinput = pygame_textinput.TextInputVisualizer()

screen = pygame.display.set_mode((1000, 200))
clock = pygame.time.Clock()

#random.randint(x, y)



while True:
    screen.fill((225, 225, 225))

    events = pygame.event.get()

    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    screen.blit(textinput.surface, (10, 10))

    for event in events:
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()
    clock.tick(30)

"""

import random
import pygame
import pygame_menu
import time

screen_width = 200
screen_height = 500

done = False
White = (255, 255, 255)
Grey = (179, 179, 179)
Black = (17, 17, 17)
Green = (30, 215, 96)

pygame.init()
pygame.display.set_caption('Dungeon Dice')
FPS = 60
screen = pygame.display.set_mode((screen_width, screen_height))
width = screen.get_width()
height = screen.get_height()
rollsound = pygame.mixer.Sound("sounds/roll.mp3")
mouse = pygame.mouse.get_pos()
font = pygame.font.SysFont('Calibri', 12)
screen.fill(Black)

SONG_END = pygame.USEREVENT + 1


def roll(faces):
    global value
    result_output.set_title(f'Rolling D{faces}...')
    value = random.randint(1, faces)
    channel = pygame.mixer.Sound.play(rollsound, maxtime=1)
    channel.set_endevent(SONG_END)


def roll_done():
    global value
    result_output.set_title(str(value))


menu = pygame_menu.Menu('Dungeon Dice', screen_width, screen_height, theme=pygame_menu.themes.THEME_DEFAULT)

for die_size in [4, 6, 8, 10, 12, 20, 100]:
    menu.add.button(f'D{die_size}', lambda faces=die_size: roll(faces))

menu.add.button('Quit', pygame_menu.events.EXIT)

result_output = menu.add.label('Result', label_id='result')

# menu.mainloop(screen)  # removed this
# new main loop follows:
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        elif event.type == SONG_END:
            roll_done()
    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)
    pygame.display.update()

