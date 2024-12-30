from Player import *
from vodka import *
from random import randint

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 400)

def Pos(pos, xy):
    pos_x, pos_y = "", ""
    bool_x, bool_y = False, False

    for i in range(len(pos)):
        if pos[i] == "(" and xy == "x":
            bool_x = True
        elif bool_x == True and pos[i] != "," and xy == "x":
            pos_x += pos[i]
        elif pos[i] == "," and xy == "x":
            bool_x = False
        elif pos[i] == " " and xy == "y":
            bool_y = True
        elif bool_y == True and pos[i] != ")" and xy == "y":
            pos_y += pos[i]
        elif pos[i] == ")" and xy == "y":
            bool_y = False

    if xy == "x":
        return int(pos_x)
    elif xy == "y":
        return int(pos_y)

width, height = 1200, 710
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

fon = pygame.image.load('screen_screen.png')

p = Player()
vodka = [Vodka(i + 1) for i in range(4)]
fal = randint(0, 3)

while True:
    screen.blit(fon, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.USEREVENT:
            for i in range(4):
                if fal == i:
                    vodka[i].t = True

    pos_x, pos_y = Pos(str(pygame.mouse.get_pos()), "x"), Pos(str(pygame.mouse.get_pos()), "y")

    if pos_x < 500:
        p.left = True
    else:
        p.left = False

    if pos_y < 250:
        p.up = True
    else:
        p.up = False

    p.update()

    for i in range(4):
        if fal == i:
            if vodka[i].next == 5:
                fal = randint(0, 3)
                vodka[i].next = 0

            vodka[i].update()

    screen.blit(p.image, p.rect)

    for i in range(5):
        for j in range(4):
            if vodka[j].vid[i] and fal == j:
                screen.blit(vodka[j].image[i], vodka[j].rect[i])

    pygame.display.flip()
    clock.tick(60)
