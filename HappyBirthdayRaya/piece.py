from pygame import Surface, mouse


class Piece:
    def __init__(self, image: Surface, width: float, height: float) -> None:
        self.image = image
        self.width = width
        self.height = height

    def is_clicked(self, x: float, y: float) -> bool:
        if not self.image.get_rect(topleft=(x, y)).collidepoint(mouse.get_pos()):
            return False

        if not mouse.get_pressed()[0]:
            return False

        return True
