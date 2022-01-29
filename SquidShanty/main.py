import pygame
import os


from menu.py import *


pygame.font.init()
pygame.mixer.init()

# Window Constants
WIDTH, HEIGHT = 1000,600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Squid Shanty")

#In Game Constants
FPS=60
INITIAL_SEA_VEL = 5
sea_vel = INITIAL_SEA_VEL
BULLET_VEL = 7
MAX_BULLETS = 5




#Images

#Color Definitions
RED=(110, 7, 7)
BLUE=(29, 30, 51)
KHAKI=(201, 182, 149)
BROWN=(56, 37, 30)
DARK_BROWN=(31, 18, 14)



#Functions

def main():

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
