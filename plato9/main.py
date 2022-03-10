import pygame
import os

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

def draw_window(WIN, STARS):
    WIN.blit(BG,(0,0))


    pygame.draw.rect(WIN, COLOR["GREEN"], STARS["green"])
    pygame.display.update()






def main():

    clock = pygame.time.Clock()
    run = True
    while run:
        event_list = pygame.event.get()

        
        clock.tick(FPS)
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        draw_window(WIN, STARS)


    main()


if __name__ == "__main__":
    main()
