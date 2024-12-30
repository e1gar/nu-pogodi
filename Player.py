import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.left = True
        self.x = 600
        self.file = "left_t40.png"
        self.image = pygame.image.load(self.file).convert_alpha()
        self.rect = self.image.get_rect(center=(self.x, 350))

    def update(self):
        self.file = "left_t40.png" if self.left else "right_t40.png"
        self.image = pygame.image.load(self.file).convert_alpha()
        self.rect = self.image.get_rect(center=(self.x, 350))
