import pygame
from settings import HEIGHT, WIDTH

class Borders(pygame.sprite.Sprite):
    def __init__(self, size_x, size_y, x, y):
        super().__init__()
        self.border = pygame.Rect(x, y, size_x, size_y)
        self.x = x
        self.y = y
        self.width = size_x
        self.height = size_y
