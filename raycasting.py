import pygame as py
import math
from settings import *

class RayCasting:
    def __init__(self, game):
        self.game = game

    def ray_cast(self):
        ox, oy = self.game.player.position
        x_map, y_map = self.game.player.map_position

        ray_angle = self.game.player.angle - HALF_FOV + 0.001
        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            #verticals
            x_vert, dx = (x_map+1, 1) if cos_a > 0 else (x_map-1e-6, -1)

            depth_vert = (x_vert-ox)/cos_a
            y_vert = oy+depth_vert*sin_a

            delta_depth = dx/cos_a
            dy = delta_depth*sin_a

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    break
                x_vert+=dx
                y_vert+=dy
                depth_vert+=delta_depth

            #horizontal
            y_hor, dy= (y_map+1,1) if sin_a>0 else (y_map-1e-6, -1)

            depth_hor = (y_hor-oy)/sin_a
            x_hor = ox+depth_hor*cos_a

            delta_depth = dy/sin_a
            dx= delta_depth*cos_a

            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    break
                x_hor+=dx
                y_hor+=dy
                depth_hor+=delta_depth

            #for setting a specified depth
            if depth_hor<depth_vert:
                depth=depth_hor
            else:
                depth=depth_vert

            #projection rendered
            proj_height = FIELD_VIEW/(depth+0.0001)

            #draw walls
            color = [255/(1+depth**5*0.00002)]*3
            py.draw.rect(self.game.screen, color, (ray*SCALE, HALF_HEIGHT-proj_height//2, SCALE, proj_height))

            #drawing lines for depth sensing
            #py.draw.line(self.game.screen, 'purple', (ox*100, oy *100), (ox*100+100*depth*cos_a, oy*100+100*depth*sin_a), 2)

            ray_angle+=DELTA_ANGLE

    def update_ray(self):
        self.ray_cast()