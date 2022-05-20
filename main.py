import pygame
import sys
from settings import HEIGHT, WIDTH
from Player import Player
from Borders import Borders
from Points import Points


def main():
    pygame.init()
    resolution = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(resolution)
    bg = pygame.image.load("textures/background.png")
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
    pacman = Player(4, (20, 20))
    borders = [
        Borders(1280, 20, 0, 0),
        Borders(1280, 20, 0, 700),
        Borders(20, 316, 0, 0),
        Borders(20, 316, 1260, 0),
        Borders(20, 316, 0, 390),
        Borders(20, 316, 1260, 390),
        # pierwszy rzad
        Borders(74, 54, 56, 58),
        Borders(95, 54, 171, 58),
        Borders(30, 95, 304, 19),
        Borders(96, 54, 374, 58),
        Borders(74, 54, 510, 58),
        Borders(34, 298, 623, 19),
        Borders(74, 54, 697, 58),
        Borders(96, 54, 811, 58),
        Borders(30, 95, 945, 19),
        Borders(96, 54, 1015, 58),
        Borders(74, 54, 1150, 58),
        # drugi rzad
        Borders(74, 29, 56, 150),
        Borders(29, 168, 170, 150),
        Borders(164, 29, 238, 150),
        Borders(29, 168, 441, 150),
        Borders(74, 29, 510, 150),
        Borders(74, 29, 698, 150),
        Borders(29, 168, 810, 150),
        Borders(164, 29, 879, 150),
        Borders(29, 168, 1082, 150),
        Borders(74, 29, 1150, 150),
        # trzeci rzad
        Borders(130, 97, 0, 220),
        Borders(74, 30, 195, 219),
        Borders(31, 70, 305, 178),
        Borders(74, 30, 370, 219),
        Borders(261, 99, 510, 219),
        Borders(74, 30, 833, 219),
        Borders(31, 70, 946, 178),
        Borders(74, 30, 1015, 219),
        Borders(130, 97, 1150, 220),
        # czwarty rzad
        Borders(130, 97, 0, 358),
        Borders(29, 98, 170, 358),
        Borders(164, 29, 238, 428),
        Borders(29, 98, 442, 358),
        Borders(261, 97, 510, 358),
        Borders(29, 98, 810, 358),
        Borders(164, 29, 879, 428),
        Borders(29, 98, 1083, 358),
        Borders(130, 97, 1150, 358),
        # piaty rzad
        Borders(74, 29, 58, 496),
        Borders(95, 29, 171, 496),
        Borders(31, 70, 305, 455),
        Borders(96, 29, 374, 496),
        Borders(74, 29, 509, 496),
        Borders(38, 298, 622, 455),
        Borders(74, 29, 698, 496),
        Borders(96, 29, 811, 496),
        Borders(31, 70, 944, 455),
        Borders(96, 29, 1014, 496),
        Borders(74, 29, 1150, 496),
        # szosty rzad
        Borders(55, 29, 20, 565),
        Borders(30, 75, 101, 520),
        Borders(164, 29, 238, 565),
        Borders(30, 75, 509, 520),
        Borders(124, 29, 579, 565),
        Borders(30, 75, 741, 520),
        Borders(164, 29, 879, 565),
        Borders(30, 75, 1150, 520),
        Borders(55, 29, 1210, 565),
        # siodmy rzad
        Borders(208, 29, 58, 634),
        Borders(30, 75, 170, 565),
        Borders(30, 75, 305, 590),
        Borders(209, 29, 374, 634),
        Borders(30, 75, 441, 565),
        Borders(209, 29, 699, 634),
        Borders(30, 75, 810, 565),
        Borders(30, 75, 947, 590),
        Borders(209, 29, 1015, 634),
        Borders(30, 75, 1081, 565),

    ]
    points = [Points((50, 35)),
              Points((70, 35)),
              Points((90, 35)),
              Points((110, 35)),
              Points((130, 35)),
              Points((150, 35)),
              Points((170, 35)),
              Points((190, 35)),]
    while True:
        # obsluga zdarzen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

        pacman.moves(borders)
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        screen.blit(pacman.image, pacman.pacman)

        for border in borders:
            pygame.draw.rect(screen, (9, 9, 123), border.border)
        for point in points:
            score = point.moves(pacman)
            if score > 0:
                points.remove(point)
                pacman.increase_score(score)
            screen.blit(point.image, point.point)
        write_text(f'Score: {pacman.score}',80,10,30,screen)
        pygame.display.flip()


def write_text(string, coordx, coordy, fontSize, screen):
    font = pygame.font.Font('textures/BarlowCondensed-Black.ttf', fontSize)
    text = font.render(string, True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    screen.blit(text, textRect)
    pygame.display.update()


main()
