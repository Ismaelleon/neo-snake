import pygame
from snake import Snake

pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Neo-Snake')

s = Snake(0, 0, 20)

def game_loop ():
    pygame.display.update()
        
    # Clean the window with a low-opacity rect
    clean_surface = pygame.Surface((500, 500), pygame.SRCALPHA)
    clean_surface.fill((0, 0, 0, 128))
    window.blit(clean_surface, (0, 0))

    s.render(window)
    s.keyboard_events()
    s.collisions()
    s.update()

if __name__ == '__main__':
    while True:
        game_loop()
