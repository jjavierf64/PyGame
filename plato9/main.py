import pygame
import os
import math

pygame.font.init()
pygame.mixer.init()


WIN_WIDTH, WIN_HEIGHT = 1000,600
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("plato9")


# INGAME CONSTANTS
FPS=60
BG = pygame.image.load(os.path.join('Assets', 'space2.png'))


# COLOR PALETTE
COLOR={
    "BLACK":(35, 37, 41),
    "PURPLE":(84, 0, 163),
    "DARK_PURPLE":(63, 17, 105),
    "PINK":(221, 115, 115),
    "GREEN":(82, 168, 36)
}

# ELEMENTS

STARS={
    "green":pygame.Rect(0,0, 20, 20)
}


# FUNCTIONS

def draw_window(WIN, STARS, pos1):
    WIN.blit(BG,(0,0))


    
    #if STARS["green"].x + STARS["green"].width > 0:

    pos2 = math.sin(pos1*math.pi/150)*150
    STARS["green"].y = 250 + math.sin(pos1*math.pi/15)*15 + pos2 + 0.25*pos1
    STARS["green"].x = pos1
    pos1 += 1 

    pygame.draw.rect(WIN, COLOR["GREEN"], STARS["green"])
    pygame.display.update()
    return pos1





def main():

    clock = pygame.time.Clock()
    run = True
    global pos1
    pos1=0
    global pos2
    pos2=0


    while run:
        event_list = pygame.event.get()

        
        clock.tick(FPS)
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        pos1 = draw_window(WIN, STARS, pos1)


    main()


if __name__ == "__main__":
    main()
