import pygame
import random,math
import threading
import time
pygame.init()
clock = pygame.time.Clock()
width = 600
height = 600
screen = pygame.display.set_mode((width,height))

pygame.display.set_caption("Princess Jump")

#princess
princess_img = pygame.image.load("D:\SubDev\PygamSub\PrincessJump\gamepics\lumpy-space-princess.png")
princessX = 300
princessY = 300
p_speedX = 0
p_speedY = 0

def princess(x,y):
    screen.blit(princess_img,(x,y))
    

def random_food_generator():
    x = random.randrange(10,550)
    y = random.randrange(10,550)
    return x,y

run = True
#food image
food_img = pygame.image.load("D:\SubDev\PygamSub\PrincessJump\gamepics\overwatch64.png")
foodX,foodY = random_food_generator()

#icon
icon = pygame.image.load("D:\SubDev\PygamSub\PrincessJump\gamepics\lumpy-space-princess.png")
pygame.display.set_icon(icon)
#score
score_val = 0
scoreX = 10
scoreY = 10

score_font = pygame.font.Font("freesansbold.ttf",32)
def showscore(x,y):
    
    score = score_font.render("Score: " + str(score_val),True,(255,255,255))
    screen.blit(score,(x,y))

def princess_eating(pX,pY,fX,fY):
    distance = math.sqrt(math.pow(((pX+5)-(fX+5)),2)+math.pow(((pY+5)-(fY+5)),2))
    if distance <= 50:
        x,y = random_food_generator()
        global score_val
        score_val += 1
        return x,y,True
    else: 
        return fX,fY,False

start_time = pygame.time.get_ticks()
timefont = pygame.font.Font("freesansbold.ttf",32)
realScore = 0
def timer():
    seconds_passed = int((pygame.time.get_ticks() - start_time)/1000)
    timer_show = timefont.render("Time: " + str(seconds_passed),True,(255,255,255))
    screen.blit(timer_show ,(400,10))
    if seconds_passed >= 30:
        if seconds_passed == 30:
            global realScore
            realScore = score_val
            
        return realScore,True
    else:
        return None,False
gameover_font = pygame.font.Font("freesansbold.ttf",32)    
def gameover(real_score):
    game_over = gameover_font.render("YOUR SCORE: " + str(real_score),True,(0,255,0))
    screen.blit(game_over,(150,250))

    
while run:
    clock.tick(150)
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: 
                p_speedX = 5
            if event.key == pygame.K_LEFT:
                p_speedX = -5
            if event.key == pygame.K_UP: 
                p_speedY = -5
            if event.key == pygame.K_DOWN:
                p_speedY = 5               

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                p_speedX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:        
                p_speedY = 0        

    princessX += p_speedX
    princessY += p_speedY
    if princessX <= -48:
        princessX = 550
    elif princessX >= 590:
        princessX = 0
    if princessY <= -48:
        princessY = 550
    elif princessY >= 590:
        princessY = 0        
      
    princess(princessX,princessY)
    # p_speedX = 0     
    # p_speedY = 0     
    foodX,foodY,food_eaten = princess_eating(princessX,princessY,foodX,foodY)
    
    screen.blit(food_img,(foodX,foodY))
    showscore(scoreX,scoreY)
    real_score,game_over_time = timer()
    if game_over_time == True:
        gameover(real_score)
    else:
        pass
    pygame.display.update()   