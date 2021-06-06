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
        self.press_w = False
        self.press_a = False
        self.press_s = False
        self.press_d = False
        self.direction_pressed = 0
        self.lifes = 3
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def turn_right(self):
        self.movement_x = 12

    def turn_left(self):
        self.movement_x = -12

    def turn_up(self):
        self.movement_y = -12

    def turn_down(self):
        self.movement_y = 12
    def stop_x(self):
        self.movement_x = 0
    def stop_y(self):
        self.movement_y = 0

    def shoot(self):
        bullet = Bullet(gm.BULLET,self.direction_pressed, self.rect.centerx, self.rect.centery)
        self.level.set_of_bullets.add(bullet)
    #  def shoot_right(self):
    #    bullet = Bullet(gm.BULLET,  self.rect.centerx, self.rect.centery)
     #   self.level.set_of_bullets.add(bullet)
   # def shoot_left(self):
   #     bullet = Bullet(gm.BULLET,  self.rect.centerx, self.rect.centery)
   #     self.level.set_of_bullets.add(bullet)
   # def shoot_up(self):
   #     bullet = Bullet(gm.BULLET,   self.rect.centerx, self.rect.centery)
   #     self.level.set_of_bullets.add(bullet)
   # def shoot_down(self):
   #     bullet = Bullet(gm.BULLET,  self.rect.centerx, self.rect.centery)
    #    self.level.set_of_bullets.add(bullet)

#self.press_w, self.press_s,self.press_d, self.press_a,
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
        shooty = False
        timer = 0
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

                if event.key == pygame.K_d:
                    self.press_d = True
                    self.press_a = False
                    self.direction_pressed += 10
                    #self.shoot_right()
                    #self.shoot()
                    shooty = True
                if event.key == pygame.K_w:
                    self.press_w = True
                    self.press_s = False
                    self.direction_pressed += 1
                    #self.shoot_up()
                    #self.shoot()
                    shooty = True
                if event.key == pygame.K_s:
                    self.press_s = True
                    self.press_w = False
                    self.direction_pressed -= 1
                   # self.shoot_down()
                    #self.shoot()
                    shooty = True
                if event.key == pygame.K_a:
                    self.press_a = True
                    self.press_d = False
                    self.direction_pressed -= 10
                    #self.shoot_left()
                    #self.shoot()
                    shooty = True
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

                if event.key == pygame.K_d:
                    self.press_d = False
                    self.direction_pressed -= 10
                if event.key == pygame.K_w:
                    self.press_w = False
                    self.direction_pressed -= 1

                if event.key == pygame.K_s:
                    self.press_s = False
                    self.direction_pressed += 1

                if event.key == pygame.K_a:
                    self.press_a = False
                    self.direction_pressed += 10
            #print(self.direction_pressed)
            if shooty == True:
                #if timer ==0:
                    #timer+=10
                if self.direction_pressed == 0:
                    timer =0
                else:
                    self.shoot()

            #timer -=1
            shooty = False

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, direction_pressed, rect_center_x, rec_center_y):
        super().__init__()
        self.image= image
        self.rect = self.image.get_rect()
        self.direction_pressed = direction_pressed
        self.rect.center = [rect_center_x, rec_center_y]
    def update(self):
        if self.direction_pressed == 10:
            self.rect.x +=15
        if self.direction_pressed == 1:
            self.rect.y -= 15
        if self.direction_pressed == 11:
            self.rect.y -= 15
            self.rect.x += 15
        if self.direction_pressed == 9:
            self.rect.x += 15
            self.rect.y += 15
        if self.direction_pressed == -10:
            self.rect.x -=15
        if self.direction_pressed == -1:
            self.rect.y += 15
        if self.direction_pressed == -11:
            self.rect.y += 15
            self.rect.x -= 15
        if self.direction_pressed == -9:
            self.rect.x -= 15
            self.rect.y -= 15
class Level:
    def __init__(self, player):
        self.player = player
        self.set_of_bullets = pygame.sprite.Group()

    def draw(self, surface):
        self.set_of_bullets.draw(surface)

        for i in range(player.lifes - 1):
            surface.blit(gm.HEART, [20 + i * 40, 15])
    def update(self):
        self.set_of_bullets.update()
        self.delete_bullet()

    def delete_bullet(self):

        for b in self.set_of_bullets:
            if b.rect.left >gm.WIDTH or b.rect.right <0:
                b.kill()

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
    current_level.draw(screen)
    player.update()
    current_level.update()

    #aktualizacja okna pygame
    pygame.display.flip()
    clock.tick(30)


pygame.quit()