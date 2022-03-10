import pygame
import math
from particle import Particle


# defining some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
LASER_RED = (235,5,5)

# inital pygame settings
WIDTH = 900
HEIGHT = 900
FPS = 60
BASE_START_POINT = [WIDTH // 2, HEIGHT - 20]

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


def main_game_loop():
    # list to hold all the active particles
    active_particles = []
    firing = False

    while True:

        # drawing a line from the base to the cursor for fun
        target_line = [(BASE_START_POINT[0], BASE_START_POINT[1]), pygame.mouse.get_pos()]

        # getting the angle from the base position to the cursor.
        cursor_position_x, cursor_position_y = pygame.mouse.get_pos()
        opposite_len = cursor_position_x - BASE_START_POINT[0] # x 
        adjacent_len = BASE_START_POINT[1] - cursor_position_y # y
        angle_to_cursor = math.degrees(math.atan(opposite_len/adjacent_len))

        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                quit()
            # When mouse is pressed down, start firing particles
            if e.type == pygame.MOUSEBUTTONDOWN:
                firing = True
            # on Mouseup stop firing
            if e.type == pygame.MOUSEBUTTONUP:
                firing = False

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    quit()
        
        # redraw screen to have a clean slate each frame
        screen.fill(BLACK)

        # if gun is active shoot off particles
        if firing:
            active_particles.append(Particle(BASE_START_POINT[0],BASE_START_POINT[1],angle=angle_to_cursor,velocity=10,color=WHITE,size=5))
        
        # handle particles that have left the screen, draw the ones that have not.
        for particle in active_particles:
            if particle_off_screen(particle.current_position):
                active_particles.remove(particle)
            else:
                particle.update()
                particle.draw(screen)
        

        pygame.draw.line(screen, LASER_RED, target_line[0], target_line[1])
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption(f'FPS = {round(clock.get_fps())}')


main_game_loop()
