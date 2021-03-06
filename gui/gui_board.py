from tkinter import *
from res import resource_manager
from pieces import *
from player import Player
from random import randint

CHOOSE_PIECE = 0
SELECT_CELL = 1


class BoardButton(Button):
    def __init__(self, parent, x, y):
        super(BoardButton, self).__init__(parent)
        self.board = parent
        self.x = x
        self.y = y
        self['command'] = self.callback
        self['background'] = "#A0A0A0" if (x + y) % 2 == 0 else "#E0E0E0"
        self.piece = None
        self['image'] = resource_manager.images.empty
        self['width'] = 50
        self['height'] = 50

    def callback(self):
        state = self.board.state
        if state == CHOOSE_PIECE:
            pass
        if state == SELECT_CELL:
            pass
        print("Clicked a button " + str(self) + f" {self.x} {self.y}")

    def place_piece(self, piece):
        pass


class Board(Frame):
    def __init__(self, parent):  # defines empty board
        super(Board, self).__init__(parent)
        self.state = CHOOSE_PIECE
        self.player_playing = Player.WHITE
        self.buttons = []
        for y in range(0, 8):
            for x in range(0, 8):
                new_button = BoardButton(self, x, y)
                self.buttons.append(new_button)
                new_button.grid(column=x, row=y)
        self.place_starting_pieces()

    def place_starting_pieces(self):
        for x in range(8):
            self.get_button(x, 1).config(image=resource_manager.images.black_pawn)
            self.get_button(x, 6).config(image=resource_manager.images.white_pawn)

    def get_button(self, x: int, y: int):
        return self.buttons[x + y * 8]

    def save_board(self):
        pass
