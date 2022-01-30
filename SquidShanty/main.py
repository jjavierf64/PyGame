import pygame
import os


from menu import *


pygame.font.init()
pygame.mixer.init()

# Window Constants
WIDTH, HEIGHT = 1000,600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Squid Shanty")

# Menu Elements
MENU_BUTTONS={
"START" : pygame.Rect(WIDTH//2 - 75, HEIGHT*1//4, 150, 80),
"QUIT" : pygame.Rect(WIDTH//2 - 75, HEIGHT*3//4, 150, 80)
}

# InGame Constants
FPS=60
INITIAL_SEA_VEL = 5
sea_vel = INITIAL_SEA_VEL
BULLET_VEL = 7
MAX_BULLETS = 5


#Color Pallette
COLOR={
"RED":(110, 7, 7),
"BLUE":(29, 30, 51),
"KHAKI":(201, 182, 149),
"BROWN":(56, 37, 30),
"DARK_BROWN":(31, 18, 14)
}

# Initial Mode
mode="menu"

# Functions
def main(menu_selected = 0):

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        

        if mode=="menu":
            draw_window_menu(WIN, COLOR, MENU_BUTTONS, menu_selected)
            menu_selected = handle_menu(event, menu_selected)
    
    main()


if __name__ == "__main__":
    main()