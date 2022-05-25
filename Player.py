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
        self.lives = 3
        self.starting_position = position

    def print_lives(self, screen):
        images = [200, 250, 300]
        for x in range(self.lives):
            image = pygame.image.load("textures/heart.png")
            image = pygame.transform.scale(image, (30, 30))
            screen.blit(image, [images[x], 0])

    def ghost_col(self, ghosts):
        for ghost in ghosts:
            if (self.pacman.x + self.image.get_width() > ghost.ghost.x and ghost.ghost.x + ghost.ghost.width > self.pacman.x ) and (self.pacman.y + self.image.get_height() > ghost.ghost.y and ghost.ghost.y + ghost.ghost.height > self.pacman.y):
                return True
        return False

    def ghosts_interaction(self, ghosts):
        if self.ghost_col(ghosts):
            self.lives -= 1
            self.pacman.x, self.pacman.y = self.starting_position
        return self.lives

    def rotation(self, direction):
        angle = direction - self.prev_dir
        self.image = pygame.transform.rotate(self.image, angle)
        self.prev_dir = direction

    def moves(self, borders, dt):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if self.check_col(borders, self.speed*dt, 0):
                self.pacman.x += self.speed * dt
            self.rotation(0)
        if keys[pygame.K_DOWN]:
            if self.check_col(borders, 0, self.speed*dt):
                self.pacman.y += self.speed * dt
            self.rotation(270)
        if keys[pygame.K_UP]:
            if self.check_col(borders, 0, -self.speed*dt):
                self.pacman.y -= self.speed * dt
            self.rotation(90)
        if keys[pygame.K_LEFT]:
            if self.check_col(borders, -self.speed *dt, 0):
                self.pacman.x -= self.speed * dt
            self.rotation(180)

        if self.pacman.x > WIDTH:
            self.pacman.x = 0
        elif self.pacman.x < 0:
            self.pacman.x = WIDTH
        if self.pacman.y > HEIGHT - 50:
            self.pacman.y = HEIGHT - 50
        elif self.pacman.y < 24:
            self.pacman.y = 24

    def check_col(self, borders, speed_x, speed_y):
        for border in borders:
            if (self.pacman.x + speed_x + self.image.get_width() > border.x and border.x + border.width > self.pacman.x + speed_x) and (self.pacman.y + speed_y + self.image.get_height() > border.y and border.y + border.height > self.pacman.y + speed_y):
                return False
        return True

    def increase_score(self, points):
        self.score += points
        return self.score

