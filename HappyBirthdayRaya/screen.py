from pygame import display

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 780
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

display.set_caption("Happy Birthday Raya :)")


def update() -> None:
    display.update()
