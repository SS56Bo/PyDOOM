import pygame as py
import sys
from settings import *

#creating a class
class Game:
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode(RES)