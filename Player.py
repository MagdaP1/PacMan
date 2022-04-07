import pygame
from settings import HEIGHT, WIDTH


class Player(pygame.sprite.Sprite):
    """ Class represents a player"""

    def __init__(self, speed, position):
        super().__init__()
        self.image = pygame.image.load("textures/pacman.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.pacman = self.image.get_rect()
        self.pacman.x, self.pacman.y = position
        self.score = 0
        self.state = False
        self.speed = speed

    def moves(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.pacman.x += self.speed
        if keys[pygame.K_DOWN]:
            self.pacman.y += self.speed
        if keys[pygame.K_UP]:
            self.pacman.y -= self.speed
        if keys[pygame.K_LEFT]:
            self.pacman.x -= self.speed

        if self.pacman.x > WIDTH:
            self.pacman.x = 0
        elif self.pacman.x < 0:
            self.pacman.x = WIDTH
        if self.pacman.y > HEIGHT - 46:
            self.pacman.y = HEIGHT - 46
        elif self.pacman.y < 16:
            self.pacman.y = 16
