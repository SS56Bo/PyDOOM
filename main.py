import pygame as py
import sys
from settings import *
from map import *

#creating class
class Game:
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode(RES)
        self.clock = py.time.Clock()
        self.new_game()

    def new_game(self):
        self.map = Map(self)

    def update_game(self):
        py.display.flip()
        self.clock.tick(FPS)    #setting up FPS limit
        py.display.set_caption(f'{int(self.clock.get_fps())}')

    def draw_screen(self):
        self.screen.fill('black')
        self.map.draw_map()

    def check_events(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update_game()
            self.draw_screen()

if __name__ == '__main__':
    game = Game()
    game.run()