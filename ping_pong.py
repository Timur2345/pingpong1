from pygame import *
from random import randint

window = display.set_mode((700,500))

display.set_caption('pingpong')
galaxy = transform.scale(image.load("galaxy.jpg"),(700,500))
speed_x = 3
speed_y = 3

clock = time.Clock()
FPS = 60
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,a,b):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(a,b))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    
class Player(GameSprite):  
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += 10
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= 10
class Player1(GameSprite):  
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += 10
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= 10


rocket=Player('racketki1.png',20,250,5,10,100)
rocket1=Player1('racketki2.png',650,250,5,10,100)
ball = GameSprite('ball.png',350,250,5,50,50)


finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.blit(galaxy,(0,0))
        
        ball.reset()
        ball.update()
        rocket.reset()
        rocket.update()
        rocket1.reset()
        rocket1.update() 
    if ball.rect.y > 500-50 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(rocket,ball) or sprite.collide_rect(rocket1,ball):   
        speed_x *= -1

                                                                      
    display.update()
