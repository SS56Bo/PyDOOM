import pygame as py
import math
from settings import *
from map import *

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

        self.collision_check(dx, dy)

        keys = py.key.get_pressed()
        if keys[py.K_w]:   #W key
            dx += speed_cos
            dy += speed_sine
        
        if keys[py.K_s]:   #S key
            dx += -speed_cos
            dy += -speed_sine

        if keys[py.K_a]:   #A key
            dx += speed_sine
            dy += -speed_cos

        if keys[py.K_d]:   #D key
            dx += -speed_sine
            dy += speed_cos
            
        self.collision_check(dx, dy)

        if keys[py.K_q]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[py.K_e]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    def draw_player(self):
        # py.draw.line(self.game.screen, 'purple', (self.x*100, self.y *100), (self.y *100+WIDTH*math.cos(self.angle), self.x *100+WIDTH*math.sin(self.angle)), 2)
        py.draw.circle(self.game.screen, 'gray', (self.x*100, self.y*100), 15)

    def update(self):
        self.player_movement()

    def collision_check(self, dx, dy):
        if self.wall_check(int(self.x+dx), int(self.y)):
            self.x+=dx
        if self.wall_check(int(self.x), int(self.y+dy)):
            self.y+=dy 

    def wall_check(self, x, y):
        return (x,y) not in self.game.map.world_map

    @property
    def position(self):
        return self.x, self.y
    
    @property
    def map_position(self):
        return int(self.x), int(self.y)