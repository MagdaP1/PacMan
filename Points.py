import pygame


class Points(pygame.sprite.Sprite):
    size = 8

    def __init__(self, position, super_point=False):
        super().__init__()
        self.super_point = super_point
        self.image = pygame.image.load("textures/point.png")
        if super_point :
            self.image = pygame.transform.scale(self.image, (15, 15))
        else:
            self.image = pygame.transform.scale(self.image, (Points.size, Points.size))
        self.point = self.image.get_rect()
        self.point.x, self.point.y = position

    def check_pos(self, player):

        if (
                self.point.x + self.image.get_width() > player.pacman.x and player.pacman.x + player.image.get_width() > self.point.x) and (
                self.point.y + self.image.get_height() > player.pacman.y and player.pacman.y + player.image.get_height() > self.point.y):
            return True
        return False

    def moves(self, player):
        if self.check_pos(player):
            if self.super_point:
                return 10, True
            return 10, False
        return 0, False