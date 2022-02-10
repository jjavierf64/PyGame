import pygame 


WIDTH, HEIGHT = 1400, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BLUE = (255,255,255) 
BLUE_BLOX = pygame.Rect (75, 100, 150, 80)

def draw_window(WIN,BLUE,BLUE_BOX):

   pygame.draw.rect(WIN, BLUE,BLUE_BLOX)
   WIN.blit(BLUE_BLOX (10, 30))
   pygame.display.update() 


def main():
   run = True
   while run:
      for event in pygame.event.get():    
         if event.type == pygame.QUIT:
            run = False

   pygame.quit()


if __name__=="__main__":
    main()