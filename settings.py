# Python file containing all game settings and global variables
import pygame
from required import *

# Screen variables
WIDTH = 700
HEIGHT = 450

# COLORS
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
yellow = 255, 255, 0

#player
scale = .4

# Game
fps = 60
gameRun = True
vector = pygame.math.Vector2
clock = pygame.time.Clock()
tileWidth = 100
tileHeight = 60

playerGroup = SpriteGroup()
