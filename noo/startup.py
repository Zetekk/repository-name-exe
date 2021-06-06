import pygame, os, random
import game_module as gm
from pygame.locals import *
os.environ['SDL_VIDEO_CENTERED'] = '1'          #centrowanie okna
pygame.init()

# ustawinia ekranu i gry
screen = pygame.display.set_mode(gm.SIZESCREEN)
clock = pygame.time.Clock()
window_open = True
def update_startup():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                import main
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
while window_open:
    pygame.display.flip()
    clock.tick(30)
    screen.blit(gm.BACKGROUND, (0,0))
    update_startup()
pygame.quit()