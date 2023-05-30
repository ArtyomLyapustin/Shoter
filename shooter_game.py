#from pygame import *
#from random import *
#
#mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.set_volume(0.01)
#mixer.music.play()
#fire = mixer.Sound('fire.ogg')
#fire.set_volume(0.1)
#
#
#class GameSprite(sprite.Sprite):
#   def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
#       super().__init__()
#       self.image = transform.scale(image.load(player_image), (size_x, size_y))
#       self.speed = player_speed
#       self.rect = self.image.get_rect()
#       self.rect.x = player_x
#       self.rect.y = player_y
#       self.size_x = size_x
#       self.size_y = size_y
#   def reset(self):
#       window.blit(self.image, (self.rect.x, self.rect.y))
#
#class Player(GameSprite):
#    def update(self):
#        keys = key.get_pressed()
#        if keys[K_LEFT] and self.rect.x > 5:
#            self.rect.x -= self.speed
#        if keys[K_RIGHT] and self.rect.x < 700 - 70:
#            self.rect.x += self.speed
#    def fire(self):
#        bullet = Bullet("bullet.png", self.rect.centerx - 10, self.rect.top, -15,20,20)
#        bullets.add(bullet)
#        fire.play()
#
#lost = 0
#
#class Enemy(GameSprite):
#   def update(self):
#      self.rect.y += self.speed
#      global lost
#      if self.rect.y > 500:
#         self.rect.x = randint(80, 700 - 70)
#         self.rect.y = -200
#         lost = lost + 1
#         self.speed = randint(1 , 3)
#
#class Bullet(GameSprite):
#   def update(self):
#      self.rect.y += self.speed
#      if self.rect.y < -50:
#         self.kill()
#
#window = display.set_mode((700, 500))
#display.set_caption("Shooter")
#
#game = True
#clock = time.Clock()
#FPS = 24
#
#background = transform.scale(image.load("galaxy.jpg"), (700, 500))
#ship = Player("rocket.png", 312, 400, 5,70,90)
#
#monsters = sprite.Group()
#for i in range(1,6):
#    monster = Enemy('ufo.png',randint(80, 700 - 80), -200, randint(1, 3),90,70)
#    monsters.add(monster)
#
#font.init()
#font2 = font.Font(None, 36)
#
#bullets = sprite.Group()
#
#score = 0
#goal = 10
#max_lost = 20
#
#finish = False
#run = True 
#while run:
#   for e in event.get():
#       if e.type == QUIT:
#           run = False
#       elif e.type == KEYDOWN:
#            if e.key == K_SPACE:
#                ship.fire()
#   if not finish:
#       window.blit(background,(0,0))
#       text = font2.render("Счет: " + str(score), 1, (255, 255, 255))
#       window.blit(text, (10, 20))
#       text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
#       window.blit(text_lose, (10, 50))
#       win = font2.render('YOU WIN!', True, (255, 255, 255))
#       lose = font2.render('YOU LOSE!', True, (180, 0, 0))
#       ship.update()
#       monsters.update()
#       ship.reset()
#       bullets.update()
#       bullets.draw(window)
#       collides = sprite.groupcollide(monsters, bullets, True, True)
#       for c in collides:
#           score = score + 1
#           monster = Enemy('ufo.png',randint(80, 700 - 80), -200, randint(1, 3),90,70)
#           monsters.add(monster)
#       if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
#           finish = True 
#           window.blit(lose, (200, 200))
#       if score >= goal:
#           finish = True
#           window.blit(win, (200, 200))
#       monsters.draw(window)
#       display.update()
#       clock.tick(FPS)

from pygame import *
from random import *

mixer.init()
mixer.music.load('space.ogg')
mixer.music.set_volume(0.01)
mixer.music.play()
fire = mixer.Sound('fire.ogg')
fire.set_volume(0.1)


class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
       self.size_x = size_x
       self.size_y = size_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - 70:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx - 10, self.rect.top, -15,20,20)
        bullets.add(bullet)
        fire.play()

lost = 0

class Enemy(GameSprite):
   def update(self):
      self.rect.y += self.speed
      global lost
      if self.rect.y > 500:
         self.rect.x = randint(80, 700 - 70)
         self.rect.y = -200
         lost = lost + 1
         self.speed = randint(1 , 3)

class Enemy_Asteroid(GameSprite):
   def update(self):
      self.rect.y += self.speed
      if self.rect.y > 500:
         self.rect.x = randint(80, 700 - 70)
         self.rect.y = randint(-100000, -1000)
         self.speed = randint(3 , 5)


class Bullet(GameSprite):
   def update(self):
      self.rect.y += self.speed
      if self.rect.y < -50:
         self.kill()

window = display.set_mode((700, 500))
display.set_caption("Shooter")

game = True
clock = time.Clock()
FPS = 24

background = transform.scale(image.load("galaxy.jpg"), (700, 500))
ship = Player("rocket.png", 312, 400, 5,70,90)

asteroids = sprite.Group()

for i in range(1,6):
    asteroid = Enemy_Asteroid('asteroid.png',randint(80, 700 - 80), randint(-10000, -1000), randint(4, 6),randint(90, 150),randint(90, 150))
    asteroids.add(asteroid)

monsters = sprite.Group()
for i in range(1,6):
    monster = Enemy('ufo.png',randint(80, 700 - 80), randint(-500, -200), randint(1, 3),90,70)
    monsters.add(monster)

font.init()
font2 = font.SysFont('Comic Sans MS', 36)

bullets = sprite.Group()

score = 0
goal = 100
max_lost = 20

finish = False
run = True 
while run:
   for e in event.get():
       if e.type == QUIT:
           run = False
       elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()
   if not finish:
       window.blit(background,(0,0))
       text = font2.render("Счет: " + str(score), 1, (255, 255, 255))
       window.blit(text, (10, 20))
       text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
       window.blit(text_lose, (10, 50))
       win = font2.render('YOU WIN!', True, (255, 255, 255))
       lose = font2.render('YOU LOSE!', True, (180, 0, 0))
       asteroids.update()
       asteroids.draw(window)
       ship.update()
       monsters.update()
       ship.reset()
       bullets.update()
       bullets.draw(window)
       collides1 = sprite.groupcollide(monsters, bullets, True, True)
       collides2 = sprite.groupcollide(asteroids, bullets, True, True)
       for c in collides1:
           score = score + 1
           monster = Enemy('ufo.png',randint(80, 700 - 80), -200, randint(1, 3),90,70)
           monsters.add(monster)
       for c in collides2:
           asteroid = Enemy_Asteroid('asteroid.png',randint(80, 700 - 80), randint(-100000, -1000), randint(4, 6),randint(90, 150),randint(90, 150))
           asteroids.add(asteroid)
       if sprite.spritecollide(ship, monsters, False) or lost >= max_lost or sprite.spritecollide(ship, asteroids, False):
           finish = True 
           window.blit(lose, (200, 200))
       if score >= goal:
           finish = True
           window.blit(win, (200, 200))
       monsters.draw(window)
       display.update()
       clock.tick(FPS)