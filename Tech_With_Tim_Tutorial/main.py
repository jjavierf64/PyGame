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

            
WHITE = (255,255,255)
BLACK = (0,0,0)

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
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
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x, red.y))
    WIN.blit(RANDOM_SPACESHIP,(random.x, random.y))
    pygame.display.update() 

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL + 7 > 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width - 25 < BORDER.x:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL + 5 > 0:
        yellow.y  -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height + 10 < HEIGHT:
        yellow.y  += VEL


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL + 7 > BORDER.x + BORDER.width:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width - 25 < WIDTH:
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL + 5 > 0:
        red.y  -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height - 5 < HEIGHT:
        red.y  += VEL

def main():
    red = pygame.Rect(720, 210, SPACESHIP_WIDTH, SPACESHIP_WIDTH)
    yellow = pygame.Rect(120, 210, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    random = pygame.Rect(RN, RN, SPACESHIP_WIDTH, SPACESHIP_WIDTH)

    red_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height/2 - 2, 10, 5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + red.height/2 - 2, 10, 5)
                    red_bullets.append(bullet)
        
        
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        
        draw_window(red,yellow,random)


    pygame.quit()

if __name__=="__main__":
    main()
