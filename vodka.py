import pygame

class Vodka(pygame.sprite.Sprite):
    def __init__(self, index):
        super().__init__()
        self.file = "vodka10.png"
        self.t = False
        self.next = 0
        self.vid = [False] * 5
        self.vid[0] = True
        self.x = [0] * 5
        self.y = [0] * 5

        # Define positions
        for i in range(5):
            offset = 25 * i
            slope = 13 * i
            if index == 1:
                self.x[i] = 351 + offset
                self.y[i] = 271 + slope
            elif index == 2:
                self.x[i] = 351 + offset
                self.y[i] = 361 + slope
            elif index == 3:
                self.x[i] = 811 - offset
                self.y[i] = 275 + slope
            elif index == 4:
                self.x[i] = 811 - offset
                self.y[i] = 365 + slope

        # Load and rotate images
        self.image = [pygame.image.load(self.file).convert_alpha() for _ in range(5)]
        angle = -30 if index < 3 else 30
        self.image = [pygame.transform.rotate(self.image[i], angle * i) for i in range(5)]

        self.rect = [self.image[i].get_rect(center=(self.x[i], self.y[i])) for i in range(5)]

    def update(self):
        if self.t:
            self.vid[self.next] = False
            self.next += 1
            if self.next < 5:
                self.vid[self.next] = True
            self.t = False
