import pygame
import math

from particle import Particle


# defining some colors
BLACK = (0,0,0)
WHITE = (255,255,255)


# inital pygame settings
WIDTH = 900
HEIGHT = 900
FPS = 60

# initalize the pygame window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


testpoint = Particle()

def main_game_loop():

    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    quit()
        
        screen.fill(BLACK)

        testpoint = Particle(50,50,0,0,WHITE,10)
        testpoint.update()
        testpoint.draw(screen)

        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption(f'FPS = {round(clock.get_fps())}')


main_game_loop()
