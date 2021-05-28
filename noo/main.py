import pygame, os, random
import game_module as gm
from pygame.locals import *
os.environ['SDL_VIDEO_CENTERED'] = '1'          #centrowanie okna
pygame.init()

# ustawinia ekranu i gry
screen = pygame.display.set_mode(gm.SIZESCREEN)
clock = pygame.time.Clock()


#pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())
motion = [0, 0]


class Player(pygame.sprite.Sprite):
    def __init__(self, file_image):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        self.level = None
        self.movement_x = 0
        self.movement_y = 0
        #self.player_local =(player.rect.bottom,player.rect.left)
        self.rect.x = 0
        self.rect.y = 0
        self.press_left = False
        self.press_right = False
        self.press_up = False
        self.press_down = False
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def turn_right(self):
        self.movement_x = 6

    def turn_left(self):
        self.movement_x = -6

    def turn_up(self):
        self.movement_y = -6

    def turn_down(self):
        self.movement_y = 6
    def stop_x(self):
        self.movement_x = 0
    def stop_y(self):
        self.movement_y = 0

    def update(self):
        self.rect.x += self.movement_x
        self.rect.y += self.movement_y
        #pygame.draw.rect(screen, player)
        if abs(motion[0]) < 0.01:
            motion[0] = 0
        if abs(motion[1]) < 0.01:
            motion[1] = 0
        self.rect.x += motion[0] * 10
        self.rect.y += motion[1] * 10

        for event in pygame.event.get():
            #if event.type == JOYBUTTONDOWN:
                #print(event)
                #if event.button == 0:
                 #   my_square_color = (my_square_color + 1) % len(colors)
            #if event.type == JOYBUTTONUP:
                #print(event)
            if event.type == JOYAXISMOTION:
                print(event)
                if event.axis < 0.2:
                    motion[event.axis] = event.value
            if event.type == JOYHATMOTION:
                print(event)
            if event.type == JOYDEVICEADDED:
                joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
                for joystick in joysticks:
                    print(joystick.get_name())
            if event.type == JOYDEVICEREMOVED:
                joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
                print(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.press_left = True
                    self.turn_left()

                if event.key == pygame.K_RIGHT:
                    self.press_right = True
                    self.turn_right()
                if event.key == pygame.K_UP:
                    self.press_up = True
                    self.turn_up()
                if event.key == pygame.K_DOWN:
                    self.press_down = True
                    self.turn_down()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if self.press_right:
                        self.turn_right()
                    else:
                        self.stop_x()
                    self.press_left = False
                if event.key == pygame.K_RIGHT:
                    if self.press_left:
                        self.turn_left()
                    else:
                        self.stop_x()
                    self.press_right = False
                if event.key == pygame.K_UP:
                    if self.press_down:
                        self.turn_down()
                    else:
                        self.stop_y()
                    self.press_up = False
                if event.key == pygame.K_DOWN:
                    if self.press_up:
                        self.turn_up()
                    else:
                        self.stop_y()
                    self.press_down = False




class Level:
    def __init__(self, player):
        self.player = player

class Level1(Level):
    def __init__(self, player):
        super().__init__(player)

player = Player(gm.PLAYER_SHIP)
player.rect.bottom = 350
player.rect.left = 100
current_level = Level1(player)
player.level = current_level

#głowna pętla gra
window_open = True
while window_open:
    #screen.fill(gm.LIGHTBLUE)
    screen.blit(gm.BACKGROUND, (0,0))

    #pętla zdarzeń
    #for event in pygame.event.get():
       # if event.type == pygame.QUIT:
        #    window_open = False
       # elif event.type == pygame.KEYDOWN:
       #     if event.key == pygame.K_ESCAPE:
       #         window_open = False

        #player.get_event(event)


    #rysowanie i aktualizacja obiektów
    player.draw(screen)
    #current_level.draw(screen)
    player.update()
    #current_level.update()

    #aktualizacja okna pygame
    pygame.display.flip()
    clock.tick(30)


pygame.quit()