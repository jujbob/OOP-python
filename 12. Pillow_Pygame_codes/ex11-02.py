import pygame
import random
import sys
　
### 전역 변수부

monitor = None
colorList = ["red", "green", "blue", "black", "magenta", "orange", "gray"]

### 메인 코드부
pygame.init()
monitor = pygame.display.set_mode( (500, 700) )
color = random.choice(colorList)

turtle = pygame.image.load('turtle.png')
　
while  True :
     monitor.fill(color)
     monitor.blit(turtle, (200,300))
     pygame.display.update() 
