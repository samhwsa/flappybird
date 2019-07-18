import sys, pygame, random,
from pygame.locals import *
from bird import *
from platforms import *


pygame.init()

screen_info = pygame.display.Info()
screen_size = (screen_info.current_w, screen_info.current_h)

size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

color = (30, 0, 0)
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (width, height))

#game variables
platforms = pygame.sprite.Group()
startPos = (width/8, height/2)
player = bird(startPos)
gapSize = 200
ticks = 0
loopCount = 0
score = 1

def lose():
    font = pygame.font.SysFont(None, 70)
    text.font.render("You Died!", True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (width/2, height/2)
    while True:
        clock.tick(60)
        screen.fill(color)
        screen.blit(text, text_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    platforms.empty()
                    return

def main():
    global Ticks, loopCount
    while True:
        clock.tick(60)
        if loopCount % 90 == 0:
            toppos = random.randint(0, height/2) - 400
            platforms.add(Platform((width + 100, toppos + gapSize + 800)))
            platforms.add(Platform((width + 100, toppos), True))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    platforms.empty()
                    return


if __name__=='__main__':
    main()