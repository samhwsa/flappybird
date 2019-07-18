import pygame, random

class coin(pygame.sprite.Sprite):

    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load('coin.png')
        scale = (40)
        self.image = pygame.transform.smoothscale(self.image, (scale, scale))
        self.rect = self.image.get_rect()
        self.rect.center = pos

        position = random.randint(0, int(screen_info.current_h))
        self.image = pygame.transform.position