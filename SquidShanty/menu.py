import pygame
import os

def handle_menu(event, MENU_BUTTONS, menu_selected):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN and menu_selected < 2:   #Change limit as menu options change
            menu_selected += 1

        if event.key == pygame.K_UP and menu_selected > 0:
            menu_selected -= 1
    
        if event.key == pygame.K_RETURN:
            if menu_selected == 0:
                pygame.event.post(pygame.event.Event(MENU_BUTTONS["TO_GAME"]))

            if menu_selected == 1:
                pygame.mixer.music.play(os.path.join('Assets' 'Blob.mp3'))


            if menu_selected == 2:
                pygame.quit()
    
    return menu_selected


def draw_window_menu(WIN, COLOR, MENU_BUTTONS, menu_selected):
    start_color = COLOR["KHAKI"]
    quit_color = COLOR["KHAKI"]
    options_color = COLOR["KHAKI"]
    if menu_selected == 0:
        start_color = COLOR["BROWN"]
    if menu_selected == 1:
        options_color = COLOR["BROWN"]
    if menu_selected == 2:
        quit_color = COLOR["BROWN"]
    
    WIN.fill(COLOR["BLUE"])
    
    pygame.draw.rect(WIN, start_color, MENU_BUTTONS["START"])
    pygame.draw.rect(WIN, quit_color, MENU_BUTTONS["QUIT"])
    pygame.draw.rect(WIN, options_color, MENU_BUTTONS["OPTIONS"])
    pygame.display.update()