import pygame as py
import math
from settings import *

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def player_movement(self):
        sin_pos = math.sin(self.angle)
        cos_pos = math.cos(self.angle)
        dx,dy=0,0
        speed = PLAYER_SPEED *  self.game.delta_time
        speed_sine = speed*sin_pos
        speed_cos = speed*cos_pos

        keys = py.key.get_pressed()
        if keys[py.K_w]:    #W key
            dx += speed_cos
            dy += speed_sine
        
        if keys[py.K_s]:   #S key
            dx += -speed_cos
            dy += -speed_sine

        if keys[py.K_a]:
            dx += speed_sine
            dy += -speed_cos

        if keys[py.K_d]:
            dx += -speed_sine
            dy += speed_cos
            
        self.x += dx
        self.y += dy

        if keys[py.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[py.K_RIGHT]:
            self.angle = PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    def update(self):
        self.player_movement()

    @property
    def position(self):
        return self.x, self.y
    
    @property
    def map_position(self):
        return int(self.x), int(self.y)