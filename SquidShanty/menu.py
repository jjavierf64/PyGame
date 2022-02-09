import numbers
from token import NUMBER
from typing import Set
import pygame
import os
import random
from main import *
pygame.mixer.init()


RN = random.randint(2,2)
#print(RN)

def handle_menu(event, MENU_BUTTONS, menu_selected):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN and menu_selected < 2:   #Change limit as menu options change
            menu_selected += 1
            PIP.play()

        if event.key == pygame.K_UP and menu_selected > 0:
            menu_selected -= 1
            PIP.play()
    
        if event.key == pygame.K_RETURN:
            if menu_selected == 0:
                pygame.event.post(pygame.event.Event(MENU_BUTTONS["TO_GAME"]))
                POP.play()
        
                
                

            if menu_selected == 1:
                POP.play()

            if menu_selected == 2:
                POP.play()
                if RN == 1:
                    QUIT_SOUND.play()
                if RN == 2:
                    QUIT_SOUND_2.play()
                pygame.display.update()
                pygame.time.delay(2000)
                pygame.quit()
                
    
    
    return menu_selected


def draw_window_menu(WIN, COLOR, MENU_BUTTONS, menu_selected, PATO_HITBOX, PATO_VEL, stop):
    start_color = COLOR["KHAKI"]
    quit_color = COLOR["KHAKI"]
    options_color = COLOR["KHAKI"]
    if menu_selected == 0:
        start_color = COLOR["BROWN"]
    if menu_selected == 1:
        options_color = COLOR["BROWN"]
    if menu_selected == 2:
        quit_color = COLOR["BROWN"]
        
    if RN == 1:
        WIN.blit(MENU,(0,0))
    if RN == 2:
        WIN.blit(MENU_2,(0,0))
        WIN.blit(PATO_IMAGEN,(PATO_HITBOX.x, PATO_HITBOX.y))
        

        
        
        if stop == 0:
            PATO_HITBOX.x += PATO_VEL
        if stop == 1:
            PATO_HITBOX.x -= PATO_VEL
    
              
    print(stop)
        
            


    pygame.draw.rect(WIN, start_color, MENU_BUTTONS["START"])
    pygame.draw.rect(WIN, quit_color, MENU_BUTTONS["QUIT"])
    pygame.draw.rect(WIN, options_color, MENU_BUTTONS["OPTIONS"])
    pygame.display.update()