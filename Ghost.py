import pygame
from math import inf
import random


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
        self.state_move = False
        self.number_of_moves = 0

    def rotation(self, direction):
        angle = direction - self.prev_dir
        self.image = pygame.transform.rotate(self.image, angle)
        self.prev_dir = direction

    def chasing_red(self, borders, player_cords, dt):
        speeds = [[0, - self.speed / dt], [- self.speed / dt, 0], [0, self.speed / dt], [self.speed / dt, 0]]
        directions = []
        if (not self.prev_move == speeds[0]) and self.check_col(borders, speeds[0]):
            x = player_cords[0] - self.ghost.x
            y = player_cords[1] - (self.ghost.y - self.speed / dt)
            dst = x ** 2 + y ** 2
            directions.append(dst)
        else:
            directions.append(inf)
        if (not self.prev_move == speeds[1]) and self.check_col(borders, speeds[1]):
            x = player_cords[0] - (self.ghost.x - self.speed / dt)
            y = player_cords[1] - self.ghost.y
            dst = x ** 2 + y ** 2
            directions.append(dst)
        else:
            directions.append(inf)
        if (not self.prev_move == speeds[2]) and self.check_col(borders, speeds[2]):
            x = player_cords[0] - self.ghost.x
            y = player_cords[1] - (self.ghost.y + self.speed / dt)
            dst = x ** 2 + y ** 2
            directions.append(dst)
        else:
            directions.append(inf)
        if (not self.prev_move == speeds[3]) and self.check_col(borders, speeds[3]):
            x = player_cords[0] - (self.ghost.x + self.speed / dt)
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

    def moves(self, borders, player_cords, dt):

        if not self.state:
            self.state_move = True
            if self.color == "red":
                self.chasing_red(borders, player_cords, dt)
        else:
            if self.color == "red" and self.state_move:
                self.ghost.x += self.prev_move[0]
                self.ghost.y += self.prev_move[1]
                self.state_move = False
            elif self.color == "red":
                self.run(borders)

    def run(self, borders):
        if self.number_of_moves == 0:
            self.number_of_moves += 1
            speeds = [[0, - self.speed / 2], [- self.speed / 2, 0], [0, self.speed / 2], [self.speed / 2, 0]]

            while True:
                n = random.randint(0, 3)
                if self.check_col(borders, speeds[n]) and (self.prev_move[0]*8 != speeds[n][0] or self.prev_move[1]*8 != speeds[n][1]):
                    print(self.prev_move[0] * 8)
                    print(speeds[n][0])
                    self.ghost.x += speeds[n][0] / 8
                    self.ghost.y += speeds[n][1] / 8
                    break
            self.prev_move = [speeds[n][0], speeds[n][1]]
        else:
            self.number_of_moves += 1
            if self.number_of_moves == 8:
                self.number_of_moves = 0
            self.ghost.x += self.prev_move[0] / 8
            self.ghost.y += self.prev_move[1] / 8

    def check_col(self, borders, speeds):
        for border in borders:
            if (self.ghost.x + speeds[
                0] + self.image.get_width() > border.x and border.x + border.width > self.ghost.x + speeds[0]) and (
                    self.ghost.y + speeds[
                1] + self.image.get_height() > border.y and border.y + border.height > self.ghost.y + speeds[1]):
                return False
        return True
