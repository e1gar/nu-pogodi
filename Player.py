import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.left, self.x = True, 600

        self.file = "left_t40.png"

    def update(self):
        if self.left == True:
            self.file = "left_t40.png"
            self.x = 600
        else:
            self.file = "right_t40.png"
            self.x = 600

        self.image = pygame.image.load(self.file).convert_alpha()
        self.rect = self.image.get_rect(center=(self.x, 350))
