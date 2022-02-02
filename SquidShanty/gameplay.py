import pygame
# Assets

def elements_movement(GAME_ELEMENTS, sea_vel, WIN_WIDTH, WIN_HEIGHT):
    # Move Sea
    GAME_ELEMENTS["sea1"].x -= sea_vel
    GAME_ELEMENTS["sea2"].x -= sea_vel
    GAME_ELEMENTS["sea3"].x -= sea_vel
    GAME_ELEMENTS["sea4"].x -= sea_vel

    # Respawn Sea
    if GAME_ELEMENTS["sea1"].x + GAME_ELEMENTS["sea1"].width < 0:
        GAME_ELEMENTS["sea1"].x = WIN_WIDTH - 5


    if GAME_ELEMENTS["sea2"].x + GAME_ELEMENTS["sea2"].width < 0:
        GAME_ELEMENTS["sea2"].x = WIN_WIDTH - 5


    if GAME_ELEMENTS["sea3"].x + GAME_ELEMENTS["sea3"].width < 0:
        GAME_ELEMENTS["sea3"].x = WIN_WIDTH - 5


    if GAME_ELEMENTS["sea4"].x + GAME_ELEMENTS["sea4"].width < 0:
        GAME_ELEMENTS["sea4"].x = WIN_WIDTH - 5


def draw_window_game(WIN, COLOR, GAME_ELEMENTS):
    WIN.fill(COLOR["RED"])
    

    pygame.draw.rect(WIN, COLOR["BLUE"], GAME_ELEMENTS["sea1"])
    pygame.draw.rect(WIN, COLOR["LIGHTBLUE"], GAME_ELEMENTS["sea2"])
    pygame.draw.rect(WIN, COLOR["BLUE"], GAME_ELEMENTS["sea3"])
    pygame.draw.rect(WIN, COLOR["LIGHTBLUE"], GAME_ELEMENTS["sea4"])


    pygame.display.update()