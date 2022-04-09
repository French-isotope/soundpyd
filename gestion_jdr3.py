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

pygame.init()
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption("Soundpyd")

buttons = [
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


def text_button(screen, position, text, size, colors="white on blue"):
    fg, bg = colors.split(" on ")
    font = pygame.font.SysFont("Calibri", size)
    text_render = font.render(text, 1, fg)
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, bg, (x, y, w, h))
    #    print(screen.blit(text_render, (x, y)))
    return screen.blit(text_render, (x, y))


def action_on_click(b, button_var, is_playing):
    if b.collidepoint(pygame.mouse.get_pos()):
        return change_color_down(button_var, is_playing)
    else:
        return b


def change_color_down(button_var, is_playing):
    if is_playing:
        return text_button(screen, button_var["coords"], button_var["name"], button_var["size"], IMAGE_DOWN_COLOR)
    else:
        return text_button(screen, button_var["coords"], button_var["name"], button_var["size"], button_var["color"])


def change_color_over(b, button_var, is_playing):
    if b.collidepoint(pygame.mouse.get_pos()) and not is_playing:
        return text_button(screen, button_var["coords"], button_var["name"], button_var["size"], IMAGE_HOVER_COLOR)
    elif not b.collidepoint(pygame.mouse.get_pos()) and not is_playing:
        return text_button(screen, button_var["coords"], button_var["name"], button_var["size"], button_var["color"])
    else:
        return b


def image_button(x, y, image):
    rect = image.get_rect()
    #    pos = (x, y)
    screen.blit(image, rect.x, rect.y)


def menu(buttons):
    """ This is the menu that waits you to click the buttons to start playing sounds"""

    buttons_states = dict()
    sounds = dict()
    is_playing = dict()

    for b in buttons:
        b_name = b["name"]
        is_playing[b_name] = False
        buttons_states[b_name] = text_button(screen, b["coords"], b_name, b["size"], b["color"])
        sounds[b_name] = create_sound(b["url"])
        print(is_playing[b_name])

    while True:
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                for b in buttons:
                    b_name = b["name"]
                    b_state = buttons_states[b_name]
                    is_playing[b_name] = toggle_sound(b_state, is_playing[b_name], b_name, sounds[b_name], 4000)
                    buttons_states[b_name] = action_on_click(b_state, b, is_playing[b_name])

            elif event.type == pygame.MOUSEMOTION:
                for b in buttons:
                    b_name = b["name"]
                    buttons_states[b_name] = change_color_over(buttons_states[b_name], b, is_playing[b_name])

            elif event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()


if __name__ == "__main__":
    menu(buttons)
