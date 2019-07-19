import pygame, random

class coinItem(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('coin.png')
        scale = (40)
        self.image = pygame.transform.smoothscale(self.image, (scale, scale))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(-6, 0)

    def update(self):
        self.rect.move_ip(self.speed)
