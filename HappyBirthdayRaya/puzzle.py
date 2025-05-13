import base64
from io import BytesIO
from os import path
from datetime import datetime
from typing import List, Tuple
from random import randint
from pygame import image, Surface, font, transform, Rect, key, K_s, SRCALPHA
from piece import Piece
from screen import SCREEN_WIDTH, SCREEN_HEIGHT, screen, update


class Puzzle:
    def __init__(self, pieces: List[Piece], rows: int, cols: int) -> None:
        pieces[-1].image.fill("#6A3E19")
        self.pieces = pieces
        self.answer = pieces.copy()
        self.cols = cols
        self.rows = rows
        self.moves_to_solve: int = 0
        self.start_time: datetime = datetime.now()
        self.end_time: datetime = datetime.now()
        self.solved = True
        self.shuffling = False

    @classmethod
    def create_puzzle(cls, rows: int, cols: int) -> object:
        piece_width = SCREEN_WIDTH / cols
        piece_height = SCREEN_HEIGHT / rows
        pieces = []

        img = cls.load_image()

        for row in range(rows):
            for col in range(cols):
                x, y = col * piece_width, row * piece_height

                piece = img.subsurface(Rect((x, y), (piece_width, piece_height)))

                piece = Piece(piece, piece_width, piece_height)
                pieces.append(piece)

        return cls(pieces, rows, cols)

    def shuffle_pieces(self, moves: int = 5000) -> None:
        self.shuffling = True
        for _ in range(moves):
            blank_row, blank_col = self.find_blank()

            neighbors = []
            if blank_row > 0:
                neighbors.append((blank_row - 1, blank_col))
            if blank_row < self.rows - 1:
                neighbors.append((blank_row + 1, blank_col))
            if blank_col > 0:
                neighbors.append((blank_row, blank_col - 1))
            if blank_col < self.cols - 1:
                neighbors.append((blank_row, blank_col + 1))

            random_neighbor = neighbors[randint(0, len(neighbors) - 1)]
            random_neighbor_row, random_neighbor_col = random_neighbor

            self.swap(self.get_index(blank_row, blank_col), self.get_index(random_neighbor_row, random_neighbor_col),
                      blank_col * self.pieces[0].width, blank_row * self.pieces[0].height,
                      random_neighbor_col * self.pieces[0].width, random_neighbor_row * self.pieces[0].height)

        self.shuffling = False

    @staticmethod
    def load_image() -> Surface:
        try:
            with open(path.join("assets", "encoded_image.txt"), "r") as file:
                image_str = base64.b64decode(file.read())

            img = image.load(BytesIO(image_str))
            img = transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))

            return img
        except FileNotFoundError:
            text_font = font.Font(None, 32)

            return text_font.render("No such path found!", True, "red", "black")

    def get_index(self, row: float, col: float) -> int:
        return int(col + row + ((self.rows - 1) * row))

    def swap(self, f_idx: int, s_idx: int, f_x: float, f_y: float, s_x: float, s_y: float) -> None:
        placeholder_surf = Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        surf = self.pieces[f_idx].image.copy()
        rect = self.pieces[f_idx].image.get_rect(topleft=(f_x, f_y))
        self.moves_to_solve += 1

        self.pieces[f_idx].image.fill("#6A3E19")
        if not self.shuffling:
            self.draw(placeholder_surf)

            while rect.x > s_x:
                screen.blit(placeholder_surf, (0, 0))

                rect.x -= 1

                screen.blit(surf, rect)

                update()

            while rect.x < s_x:
                screen.blit(placeholder_surf, (0, 0))

                rect.x += 1

                screen.blit(surf, rect)

                update()

            while rect.y > s_y:
                screen.blit(placeholder_surf, (0, 0))

                rect.y -= 1

                screen.blit(surf, rect)

                update()

            while rect.y < s_y:
                screen.blit(placeholder_surf, (0, 0))

                rect.y += 1

                screen.blit(surf, rect)

                update()

        self.pieces[f_idx].image = surf

        self.pieces[f_idx], self.pieces[s_idx] = self.pieces[s_idx], self.pieces[f_idx]

    def draw(self, surf: Surface) -> None:
        for col in range(self.cols):
            for row in range(self.rows):
                piece = self.pieces[self.get_index(row, col)]
                x, y = col * piece.width, row * piece.height

                surf.blit(piece.image, (x, y))

    def update(self) -> None:
        if self.pieces == self.answer:
            text_font = font.Font(None, 75)

            if not self.solved:
                self.end_time = datetime.now()
                self.solved = True

            display_surf = Surface((SCREEN_WIDTH, SCREEN_HEIGHT), SRCALPHA)
            display_surf.fill((0, 0, 0, 128))

            if self.moves_to_solve:
                text = text_font.render("You solved the puzzle!", True, "white")
                text_moves = text_font.render(f"Moves: {self.moves_to_solve}", True, "white")
                text_time = text_font.render(f"Time: {str(self.end_time - self.start_time).split('.', 2)[0]}",
                                             True, "white")

                display_surf.blit(text,
                                  (SCREEN_WIDTH / 2 - text.get_width() / 2,
                                   SCREEN_HEIGHT / 2 - 5 * text.get_height()))
                display_surf.blit(text_moves,
                                  (SCREEN_WIDTH / 2 - text_moves.get_width() / 2,
                                   SCREEN_HEIGHT / 2 - 4 * text_moves.get_height()))
                display_surf.blit(text_time,
                                  (SCREEN_WIDTH / 2 - text_time.get_width() / 2,
                                   SCREEN_HEIGHT / 2 + 5 * text_time.get_height()))
            
            text_start = text_font.render("Press S to start", True, "white")
            display_surf.blit(text_start,
                              (SCREEN_WIDTH / 2 - text_start.get_width() / 2,
                               SCREEN_HEIGHT / 2 + 4 * text_start.get_height()))

            screen.blit(display_surf, (0, 0))
            update()

            if key.get_pressed()[K_s]:
                self.shuffle_pieces()
                self.moves_to_solve = 0
                self.start_time = datetime.now()
                self.solved = False

            return

        for col in range(self.cols):
            for row in range(self.rows):
                piece = self.pieces[self.get_index(row, col)]
                x, y = col * piece.width, row * piece.height

                if piece.is_clicked(x, y):
                    if piece.image == self.answer[-1].image:
                        continue

                    blank_row, blank_col = self.find_blank()
                    blank_x, blank_y = blank_col * piece.width, blank_row * piece.height

                    if blank_row != row and blank_col != col:
                        continue

                    if abs(blank_row - row) != 1 and abs(blank_col - col) != 1:
                        continue

                    self.swap(self.get_index(row, col), self.get_index(blank_row, blank_col), x, y, blank_x, blank_y)

    def find_blank(self) -> Tuple[float, float]:
        for col in range(self.cols):
            for row in range(self.rows):
                piece = self.pieces[self.get_index(row, col)]

                if piece.image == self.answer[-1].image:
                    return row, col

        return 0, 0
