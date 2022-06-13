import pygame
import sys
from settings import HEIGHT, WIDTH, borders, points
from Player import Player
from Ghost import Ghost
from Button import Button

clock = pygame.time.Clock()
dt = clock.tick(60)
time = 0
pygame.init()
resolution = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(resolution)
backg = pygame.image.load("textures/gameover.jpg")
backg = pygame.transform.scale(backg, (WIDTH, HEIGHT))
start_backg = pygame.image.load("textures/start.webp")
start_backg = pygame.transform.scale(start_backg, (WIDTH, HEIGHT))
pacman = Player(32, (32, 32))
ghosts = [Ghost(32, (304, 320), "textures/ghost1.png", "red"),
           Ghost(32, (944, 304), "textures/ghost2.png", "red"),
           Ghost(32, (640, 336), "textures/ghost3.png", "red")
          ]
final_score = 0

button1 = Button(
    "Play",
    (550, 150),
    font=100,
    bg="black",
)


def main():
    is_played = False
    while True:
        # obsluga zdarzen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)
            if not is_played:
                is_played = button1.click(event)

        if is_played:
            play()
        else:
            screen.fill((0, 0, 0))
            screen.blit(start_backg, (0, 0))

            screen.blit(button1.surface, (button1.x, button1.y))
            pygame.display.flip()
        lives, ghost = pacman.ghosts_interaction(ghosts)
        if lives <= 0 or final_score == 6430:
            break
        if ghost:
            ghosts.remove(ghost)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)
        screen.fill((0, 0, 0))
        screen.blit(backg, (0, 0))
        write_text(f'Score: {pacman.score}', 600, 200, 90, screen)
        pygame.display.flip()


def play():
    global time
    pacman.moves(borders, dt)

    screen.fill((0, 0, 0))

    screen.blit(pacman.image, pacman.pacman)

    for border in borders:
        pygame.draw.rect(screen, (9, 9, 123), border.border)
    for point in points:
        score, state = point.moves(pacman)
        if state:
            for x in ghosts:
                x.state = True
                x.image = pygame.image.load("textures/dg.png")
                x.image = pygame.transform.scale(x.image, (32, 32))
            pacman.state = True

        if score > 0:
            points.remove(point)
            final_score = pacman.increase_score(score)
        screen.blit(point.image, point.point)
    time += 1
    if time > 600:
        time = 0
        while len(ghosts) < 3:
            ghosts.append(Ghost(32, (944, 304), "textures/ghost2.png", "red"))
        for y, x in enumerate(ghosts):
            x.state = False
            x.image = pygame.image.load(f'textures/ghost{y+1}.png')
            x.image = pygame.transform.scale(x.image, (32, 32))
        pacman.state = False
    for x in ghosts:
        screen.blit(x.image, x.ghost)
        x.moves(borders, [pacman.pacman.x, pacman.pacman.y], dt)
    pacman.print_lives(screen)
    write_text(f'Score: {pacman.score}', 80, 10, 30, screen)

    pygame.display.flip()


def write_text(string, coordx, coordy, fontSize, screen):
    font = pygame.font.Font('textures/BarlowCondensed-Black.ttf', fontSize)
    text = font.render(string, True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    screen.blit(text, textRect)
    pygame.display.update()


main()
