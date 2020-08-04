import pygame
from paddle import Paddle
from ball import Ball

pygame.init()
Paddle.init() 
Ball.init() 

#define colors
BLACK = (0,0,0)
WHITE = (255,255,255)

size = (100,15)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

#adding paddles
paddleS = Paddle(WHITE, 100, 15)
paddleS.rect.x = 200
paddleS.rect.y = 30

paddleT = Paddle(WHITE, 200, 30)
paddleT.rect.x = 400
paddleT.rect.y = 60 
  
#adding the ball
ball = Ball(WHITE,10,10)  
ball.rect.x = 200
ball.rect.y = 125


#including sprites lists
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleS)
all_sprites_list.add(paddleT)
all_sprites_list.add(ball)

#The loop will carry on until user exits the game 
carryOn = True

#The clock will be used to control how fast the screen moves during the game
clock = pygame.time.Clock()

#adding score
scoreS = 0
scoreT = 0 


while carryOn:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      carryOn = False 
    elif event.type==pygame.KEYDOWN:
     if event.key==pygame.K_x:
        carryOn=False 

  keys = pygame.key.get_pressed()       
  if keys[pygame.K_w]:
    paddleS.moveup(5)
  if keys[pygame.K_s]:
      paddleS.movedown(5) 
  if keys[pygame.K_UP]:
    paddleT.moveup(5)   
  if keys[pygame.K_DOWN]:
    paddleT.movedown(5)

all_sprites_list.update()       

#ball movement
if ball.rect.x>=300:
  ball.velocity[0] = -ball.velocity[0]
if ball.rect.x<=0:
  ball.velocity[0] = -ball.velocity[0]  
if ball.rect.y>250:
  ball.velocity[1] = -ball.velocity[1]   
if ball.rect.y<0:
  ball.velocity[1] = -ball.velocity[1]  

#adding ball bounce and collisions
if pygame.sprite.collide_mask(ball, paddleS) or pygame.sprite.collide_mask(ball, paddleT):
  ball.bounce()
  

screen.fill(BLACK)
pygame.draw.line(screen, WHITE,[300,0], [300,200],5)   

all_sprites_list.draw(screen)

#adding score
font = pygame.font.Font(None, 54)
text = font.render(str(scoreS), 1, WHITE)
screen.blit(text,(250,10))
text = font.render(str(scoreT), 1, WHITE)
screen.blit(text, (420,10))

pygame.display.flip()
#add time frame for each game played
clock.tick(60)

pygame.quit()

