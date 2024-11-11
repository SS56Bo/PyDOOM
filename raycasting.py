import pygame as py
import math
from settings import *

class RayCasting:
    def __init__(self, game):
        self.game = game

    def ray_cast(self):
        ray_angle = self.game.player.angle - HALF_FOV + 0.001
        print(ray_angle)
        for ray in range(NUM_RAYS):
            ray_angle+=DELTA_ANGLE

    def update_ray(self):
        self.ray_cast()