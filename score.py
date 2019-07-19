import pygame

class scoreCounter(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((1, 10000))
        self.image.set_alpha(0)
        self.image.fill((0,0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(-6, 0)



    def update(self):
        self.rect.move_ip(self.speed)
