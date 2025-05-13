import pygame
from screen import screen, update
from loop import quit_condition
from puzzle import Puzzle


def main():
    puzzle = Puzzle.create_puzzle(5, 5)

    run = True
    while run:
        screen.fill("#000000")

        run = quit_condition()

        puzzle.draw(screen)
        puzzle.update()

        update()


if __name__ == "__main__":
    pygame.init()
    main()
