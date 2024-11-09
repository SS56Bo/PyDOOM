import pygame as py
import math
from settings import *

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def player_movement(self):
        pass

    def update(self):
        self.player_movement()