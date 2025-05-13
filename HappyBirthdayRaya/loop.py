from pygame import QUIT, event as pg_event


def quit_condition() -> bool:
    for event in pg_event.get():
        if event.type == QUIT:
            return False

    return True
