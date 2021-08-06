import pygame
import pygame.display

pygame.init()

WIDTH, HEIGHT = int(pygame.display.Info().current_w*.75), int(pygame.display.Info().current_h*.75)
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        WIN.fill((255,255,255))

    pygame.quit()

if __name__ == "__main__":
    main()