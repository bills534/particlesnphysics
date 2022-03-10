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
BASE_START_POINT = [WIDTH // 2, HEIGHT - 20]
print(BASE_START_POINT)
# initalize the pygame window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def particle_off_screen(position):
    posx = position[0]
    posy = position[1]
    if posx < 0 or posx > WIDTH:
        return True
    if posy < 0 or posy > HEIGHT:
        return True

    return False

# list to hold all the active particles
active_particles = []


def main_game_loop():
    start_angle = 0

    while True:
        # getting the angle from the base position to the cursor.
        cursor_position_x, cursor_position_y = pygame.mouse.get_pos()
        # more trigonometry, been literally 20+ years since ive used any of this
        opposite_len = cursor_position_x - BASE_START_POINT[0] # x 
        adjacent_len = BASE_START_POINT[1] - cursor_position_y # y
        angle_to_cursor = math.degrees(math.atan(opposite_len/adjacent_len))

        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                quit()
            # make a new particle every click
            if e.type == pygame.MOUSEBUTTONDOWN:
                # spawn a new particle with every click
                active_particles.append(Particle(BASE_START_POINT[0],BASE_START_POINT[1],angle=angle_to_cursor,velocity=10,color=WHITE,size=5))

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    quit()
        
        screen.fill(BLACK)

        
        for particle in active_particles:
            # clear out particles no longer on screen
            if particle_off_screen(particle.current_position):
                active_particles.remove(particle)
            else:
                particle.update()
                particle.draw(screen)

        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption(f'FPS = {round(clock.get_fps())}')


main_game_loop()
