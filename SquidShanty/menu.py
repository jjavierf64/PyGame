import pygame



# Assets



def handle_menu(event, menu_selected):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN and menu_selected < 1:
            menu_selected += 1

        if event.key == pygame.K_UP and menu_selected > 0:
            menu_selected -= 1
    print(menu_selected)
    return menu_selected


def draw_window_menu(WIN, COLOR, MENU_BUTTONS, menu_selected=0):
    start_color = COLOR["KHAKI"]
    quit_color = COLOR["KHAKI"]
    if menu_selected == 0:
        start_color = COLOR["BROWN"]
    elif menu_selected == 1:
        quit_color = COLOR["BROWN"]
    
    WIN.fill(COLOR["BLUE"])
    
    pygame.draw.rect(WIN, start_color, MENU_BUTTONS["START"])
    pygame.draw.rect(WIN, quit_color, MENU_BUTTONS["QUIT"])
    pygame.display.update()