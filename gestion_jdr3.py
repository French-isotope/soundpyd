import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

# Default button images/pygame.Surfaces.
IMAGE_NORMAL_COLOR = 'white on dodgerblue1'
IMAGE_HOVER_COLOR = 'white on lightskyblue'
IMAGE_DOWN_COLOR = 'white on aquamarine1'

BASE_URL = "C:/projects/soundpyd/test_yt_dl"


buttons = [
    {
        "name": "growl",
        "coords": (400, 300),
        "color": IMAGE_NORMAL_COLOR,
        "size": 20,
        "playing": False,
        "url": f"{BASE_URL}/MSE.mp3",
#        "sound": pygame.mixer.Sound("C:/test_yt_dl/MSE.mp3")
    },
    {
        "name": "war",
        "coords": (300, 300),
        "color": IMAGE_NORMAL_COLOR,
        "size": 20,
        "playing": False,
        "url": f"{BASE_URL}/FSW.mp3",
#        "sound": pygame.mixer.Sound("C:/test_yt_dl/FSW.mp3")
    },
    {
        "name": "cavern",
        "coords": (200, 300),
        "color": IMAGE_NORMAL_COLOR,
        "size": 20,
        "playing": False,
        "url": f"{BASE_URL}/SC.mp3",
#        "sound": pygame.mixer.Sound("C:/test_yt_dl/SC.mp3")
    },
    {
        "name": "house_with_fire",
        "coords": (000, 300),
        "color": IMAGE_NORMAL_COLOR,
        "size": 20,
        "playing": False,
        "url": f"{BASE_URL}/house_with_fire.mp3",
#        "sound": pygame.mixer.Sound("C:/test_yt_dl/house_with_fire.mp3")
    },
    {
        "name": "joy_festival",
        "coords": (400, 0),
        "color": IMAGE_NORMAL_COLOR,
        "size": 20,
        "playing": False,
        "url": f"{BASE_URL}/joy_festival.mp3",
#        "sound": pygame.mixer.Sound("C:/test_yt_dl/joy_festival.mp3")
    },
]


def create_sound(url):
    return pygame.mixer.Sound(f"{url}")


def toggle_sound(is_playing, soundname, sound, fade_time=4000):
    if is_playing:
        pygame.mixer.Sound.fadeout(sound, fade_time)
        print(f"Stop sound : {soundname}")
        return False
    else:
        print(f"Let's go sound : {soundname}")
        pygame.mixer.Sound.play(sound, fade_ms=fade_time)
        return True


def button(screen, position, text, size, colors="white on blue"):
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
    print(screen.blit(text_render, (x, y)))
    return screen.blit(text_render, (x, y))


def action_on_click(b, var_button, sound, fade_time):
    if b.collidepoint(pygame.mouse.get_pos()):
        var_button["playing"] = toggle_sound(var_button["playing"], var_button["name"], sound, fade_time)
        return change_color_down(var_button)
    else:
        return b


def change_color_down(button_var):
    if button_var["playing"]:
        return button(screen, button_var["coords"], button_var["name"], button_var["size"], IMAGE_DOWN_COLOR)
    else:
        return button(screen, button_var["coords"], button_var["name"], button_var["size"], button_var["color"])


def change_color_over(b, button_var):
    if b.collidepoint(pygame.mouse.get_pos()) and not button_var["playing"]:
        return button(screen, button_var["coords"], button_var["name"], button_var["size"], IMAGE_HOVER_COLOR)
    elif not b.collidepoint(pygame.mouse.get_pos()) and not button_var["playing"]:
        return button(screen, button_var["coords"], button_var["name"], button_var["size"], button_var["color"])
    else:
        return b


def menu(buttons):
    """ This is the menu that waits you to click the buttons to start playing sounds"""

    buttons_states = dict()
    sounds = dict()

    for b in buttons:
        sounds[b["name"]] = create_sound(b["url"])

    for b in buttons:
        buttons_states[b["name"]] = button(screen, b["coords"], b["name"], b["size"], b["color"])

    while True:
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                for b in buttons:
                    buttons_states[b["name"]] = action_on_click(buttons_states[b["name"]], b, sounds[b["name"]], 4000)

            elif event.type == pygame.MOUSEMOTION:
                for b in buttons:
                    buttons_states[b["name"]] = change_color_over(buttons_states[b["name"]], b)

            elif event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()


if __name__ == "__main__":
    menu(buttons)

