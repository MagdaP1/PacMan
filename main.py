import pygame
import sys
from settings import HEIGHT, WIDTH
from Player import Player


def main():
    pygame.init()
    resolution = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(resolution)
    bg = pygame.image.load("textures/background.png")
    bg = pygame.transform.scale(bg, (WIDTH,HEIGHT))
    pacman = Player(4, (20, 20))
    while True:
        # obsluga zdarzen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

        pacman.moves()
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        screen.blit(pacman.image, pacman.pacman)
        pygame.display.flip()


main()