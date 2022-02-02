from random import Random
from typing import Sequence
import pygame
import os
import random

RN = random.randint(1,4)
RN2 = random.randint(1,1)

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")
#pygame.display.
            
WHITE = (255,255,255)
BLACK = (0,0,0)

BORDER = pygame.Rect(WIDTH/2, 0, 10, HEIGHT)

FPS = 60
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
RANDOM_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_random.png'))
RANDOM_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RANDOM_SPACESHIP_IMAGE, (RN2,RN2)),90)

def draw_window(red, yellow, random):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x, red.y))
    WIN.blit(RANDOM_SPACESHIP,(random.x, random.y))
    pygame.display.update() 

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d]:
        yellow.x += VEL
    if keys_pressed[pygame.K_w]:
        yellow.y  -= VEL
    if keys_pressed[pygame.K_s]:
        yellow.y  += VEL


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT]:
        red.x += VEL
    if keys_pressed[pygame.K_UP]:
        red.y  -= VEL
    if keys_pressed[pygame.K_DOWN]:
        red.y  += VEL

def main():
    red = pygame.Rect(720, 210, SPACESHIP_WIDTH, SPACESHIP_WIDTH)
    yellow = pygame.Rect(120, 210, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    random = pygame.Rect(RN, RN, SPACESHIP_WIDTH, SPACESHIP_WIDTH)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        
        draw_window(red,yellow,random)


    pygame.quit()

if __name__=="__main__":
    main()
