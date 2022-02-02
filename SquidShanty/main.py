import pygame
import os


from menu import *
from gameplay import *

pygame.font.init()
pygame.mixer.init()

# Window Constants
WIN_WIDTH, WIN_HEIGHT = 1000,600
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Squid Shanty")


# Menu Elements and Triggers from the Buttons
MENU_BUTTONS={
"START" : pygame.Rect(WIN_WIDTH//2 - 75, WIN_HEIGHT*1//4, 150, 80),
"QUIT" : pygame.Rect(WIN_WIDTH//2 - 75, WIN_HEIGHT*3//4, 150, 80),
"OPTIONS" : pygame.Rect(WIN_WIDTH//2 - 75, WIN_HEIGHT*2//4, 150, 80),
"TO_GAME" : pygame.USEREVENT + 100,
"TO_CHARS" : pygame.USEREVENT + 101,
"TO_LEAD" : pygame.USEREVENT + 102
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
    "LIGHTBLUE": (0, 95, 115),
    "KHAKI":(201, 182, 149),
    "BROWN":(56, 37, 30),
    "DARK_BROWN":(31, 18, 14)
}

# Game Assets

# CHARACTERS
CHARS_WIDTH, CHARS_HEIGHT = 100, 100

CHARS_IMGS = {
    "CROOK" : pygame.image.load(os.path.join('Assets', 'Crook.png'))
}

CHARS= {
"CROOK" : pygame.transform.scale(CHARS_IMGS["CROOK"],(CHARS_WIDTH,CHARS_HEIGHT))
}


SEA_WIDTH, SEA_HEIGHT = 335, 50

#ASSETS={
#    "SEA": 
#}
GAME_ELEMENTS={
            "sea1" : pygame.Rect(0,WIN_HEIGHT - SEA_HEIGHT, SEA_WIDTH, SEA_HEIGHT),
            "sea2" : pygame.Rect(333,WIN_HEIGHT - SEA_HEIGHT, SEA_WIDTH, SEA_HEIGHT),
            "sea3" : pygame.Rect(666,WIN_HEIGHT - SEA_HEIGHT, SEA_WIDTH, SEA_HEIGHT),
            "sea4" : pygame.Rect(WIN_WIDTH,WIN_HEIGHT - SEA_HEIGHT, SEA_WIDTH, SEA_HEIGHT)
            }




# Functions
def main():

    menu_selected=0
    mode="menu"

    char= pygame.Rect(100, WIN_HEIGHT +10 - CHARS_HEIGHT - GAME_ELEMENTS["sea1"].height, CHARS_WIDTH, CHARS_HEIGHT)
    



    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        

        if mode == "menu":
            draw_window_menu(WIN, COLOR, MENU_BUTTONS, menu_selected)
            menu_selected = handle_menu(event, MENU_BUTTONS,  menu_selected)
            
            if event.type == MENU_BUTTONS["TO_GAME"]:
                mode = "game"

        if mode == "game":
            
            elements_movement(GAME_ELEMENTS, sea_vel, WIN_WIDTH, WIN_HEIGHT)

            draw_window_game(WIN, WIN_WIDTH, WIN_HEIGHT, COLOR, GAME_ELEMENTS, CHARS, char)
    
    main()


if __name__ == "__main__":
    main()