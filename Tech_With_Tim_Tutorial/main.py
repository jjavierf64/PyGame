from random import Random
import pygame
import os
import random
RN = random.randint(1,4)
RN2 = random.randint(1,1)

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

WHITE = (255,255,255)

FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_WIDTH)),90)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_WIDTH)),270)
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


def main():
    red = pygame.Rect(720, 210, SPACESHIP_WIDTH, SPACESHIP_WIDTH)
    yellow = pygame.Rect(120, 210, SPACESHIP_WIDTH, SPACESHIP_WIDTH)
    random = pygame.Rect(RN, RN, SPACESHIP_WIDTH, SPACESHIP_WIDTH)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:
            yellow.x -= 1
        
        draw_window(red,yellow,random)


    pygame.quit()

if __name__=="__main__":
    main()