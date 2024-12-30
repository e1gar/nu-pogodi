import pygame
from Player import Player
from vodka import Vodka
from random import randint

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 400)

def parse_position(pos, axis):
    """Parses position from a string representation."""
    if axis == "x":
        return int(pos.split(",")[0][1:])
    elif axis == "y":
        return int(pos.split(",")[1][:-1])
    else:
        raise ValueError("Axis must be 'x' or 'y'")

width, height = 1200, 710
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

background = pygame.image.load('screen_screen.png')

player = Player()
vodkas = [Vodka(i + 1) for i in range(4)]
current_active_vodka = randint(0, 3)

running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.USEREVENT:
            vodkas[current_active_vodka].t = True

    mouse_x, mouse_y = pygame.mouse.get_pos()

    player.left = mouse_x < 500
    player.up = mouse_y < 250

    player.update()

    for i, vodka in enumerate(vodkas):
        if i == current_active_vodka:
            if vodka.next == 5:  # Если Vodka закончила появляться
                current_active_vodka = randint(0, 3)
                vodka.next = 0
            vodka.update()

    screen.blit(player.image, player.rect)

    for i, vodka in enumerate(vodkas):
        if i == current_active_vodka:  # Рисуем только активную Vodka
            for idx, visible in enumerate(vodka.vid):
                if visible:
                    screen.blit(vodka.image[idx], vodka.rect[idx])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
