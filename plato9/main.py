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
    "green":pygame.Rect(0,0, 20, 20),
    "pink":pygame.Rect(0,0, 20, 20)
}


# FUNCTIONS

def draw_window(WIN, STARS, pos1):
    WIN.blit(BG,(0,0))


    # GREEN MOVEMENT
    #if STARS["green"].x + STARS["green"].width > 0:
    STARS["green"].y = 250 + 15 * math.sin(pos1*math.pi/15) + 150 * math.sin(pos1*math.pi/150) + 0.2*pos1
    STARS["green"].x = pos1

    # PINK MOVEMENT
    STARS["pink"].y = 200 + 100 * math.sin(pos1*math.pi/40)
    STARS["pink"].x = WIN_WIDTH-( 100 + 100 * math.cos(pos1*math.pi/40) + pos1)




    pos1 += 1 

    pygame.draw.rect(WIN, COLOR["GREEN"], STARS["green"])
    pygame.draw.rect(WIN, COLOR["PINK"], STARS["pink"])
    pygame.display.update()
    return pos1





def main():

    clock = pygame.time.Clock()
    run = True
    global pos1
    pos1=0


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
