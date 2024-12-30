import pygame

class Vodka(pygame.sprite.Sprite):
    def __init__(self, nom):
        pygame.sprite.Sprite.__init__(self)

        self.file = "vodka10.png"

        self.x = [0 for i in range(5)]
        self.y = [0 for i in range(5)]

        self.vid = [False for i in range(5)]
        self.t, self.next = False, 0
        self.vid[0] = True

        for i in range(5):
            if nom == 1:
                self.x[i] = 341 + 10 + i *25
                self.y[i] = 281 - 10 + i * 13
            elif nom == 2:
                self.x[i] = 341 + 10 + i *25
                self.y[i] = 371 - 10 + i * 13
            elif nom == 3:
                self.x[i] = 811 - (10 + i *25)
                self.y[i] = 285 - 10 + i * 13
            elif nom == 4:
                self.x[i] = 811 - (10 + i *25)
                self.y[i] = 375 - 10 + i * 13

        self.image = [pygame.image.load(self.file).convert_alpha() for i in range(5)]
        if nom < 3:
            self.image = [pygame.transform.rotate(self.image[i], -30 * i) for i in range(5)]
        else:
            self.image = [pygame.transform.rotate(self.image[i], 30 * i) for i in range(5)]

        self.rect = [self.image[i].get_rect(center=(self.x[i], self.y[i])) for i in range(5)]

    def update(self):
        if self.t == True:
            self.vid[self.next] = False
            self.next += 1
            if self.next < 5:
                self.vid[self.next] = True

            self.t = False

