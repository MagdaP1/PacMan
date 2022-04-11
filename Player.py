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
        self.prev_dir = 0

    def rotation(self, direction):
        angle = direction - self.prev_dir
        self.image = pygame.transform.rotate(self.image, angle)
        self.prev_dir = direction

    def moves(self, borders):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if self.check_col(borders, self.speed, 0):
                self.pacman.x += self.speed
            self.rotation(0)
        if keys[pygame.K_DOWN]:
            if self.check_col(borders, 0, self.speed):
                self.pacman.y += self.speed
            self.rotation(270)
        if keys[pygame.K_UP]:
            if self.check_col(borders, 0, -self.speed):
                self.pacman.y -= self.speed
            self.rotation(90)
        if keys[pygame.K_LEFT]:
            if self.check_col(borders, -self.speed, 0):
                self.pacman.x -= self.speed
            self.rotation(180)

        if self.pacman.x > WIDTH:
            self.pacman.x = 0
        elif self.pacman.x < 0:
            self.pacman.x = WIDTH
        if self.pacman.y > HEIGHT - 46:
            self.pacman.y = HEIGHT - 46
        elif self.pacman.y < 16:
            self.pacman.y = 16

    def check_col(self, borders, speed_x, speed_y):
        for border in borders:
            if (self.pacman.x + speed_x + self.image.get_width() > border.x and border.x + border.width > self.pacman.x + speed_x) and (self.pacman.y + speed_y + self.image.get_height() > border.y and border.y + border.height > self.pacman.y + speed_y):
                return False
        return True
