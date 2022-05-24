import pygame
from math import inf


class Ghost(pygame.sprite.Sprite):

    def __init__(self, speed, position, image, color):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.ghost = self.image.get_rect()
        self.ghost.x, self.ghost.y = position
        self.state = False
        self.speed = speed
        self.prev_dir = 0
        self.color = color
        self.prev_move = None

    def rotation(self, direction):
        angle = direction - self.prev_dir
        self.image = pygame.transform.rotate(self.image, angle)
        self.prev_dir = direction

    def chasing_red(self, borders, player_cords):
        speeds = [[0, - self.speed], [- self.speed, 0], [0, self.speed],  [self.speed, 0]]
        directions = []
        if (not self.prev_move == speeds[0]) and self.check_col(borders, speeds[0]):
            x = player_cords[0] - self.ghost.x
            y = player_cords[1] - (self.ghost.y - self.speed)
            dst = x**2 + y**2
            directions.append(dst)
        else:
            directions.append(inf)
        if (not self.prev_move == speeds[1]) and self.check_col(borders, speeds[1]):
            x = player_cords[0] - (self.ghost.x - self.speed)
            y = player_cords[1] - self.ghost.y
            dst = x ** 2 + y ** 2
            directions.append(dst)
        else:
            directions.append(inf)
        if (not self.prev_move == speeds[2]) and self.check_col(borders, speeds[2]):
            x = player_cords[0] - self.ghost.x
            y = player_cords[1] - (self.ghost.y + self.speed)
            dst = x ** 2 + y ** 2
            directions.append(dst)
        else:
            directions.append(inf)
        if (not self.prev_move == speeds[3]) and self.check_col(borders, speeds[3]):
            x = player_cords[0] - (self.ghost.x + self.speed)
            y = player_cords[1] - self.ghost.y
            dst = x ** 2 + y ** 2
            directions.append(dst)
        else:
            directions.append(inf)

        smallest = min(directions)
        index = directions.index(smallest)
        self.prev_move = speeds[index]
        self.ghost.x += self.prev_move[0]
        self.ghost.y += self.prev_move[1]
        self.prev_move = [- self.prev_move[0], - self.prev_move[1]]

    def moves(self, borders, player_cords):

        if self.color == "red":

            self.chasing_red(borders, player_cords)

    def check_col(self, borders, speeds):
        for border in borders:
            if (self.ghost.x + speeds[0] + self.image.get_width() > border.x and border.x + border.width > self.ghost.x + speeds[0]) and (self.ghost.y + speeds[1] + self.image.get_height() > border.y and border.y + border.height > self.ghost.y + speeds[1]):
                return False
        return True
