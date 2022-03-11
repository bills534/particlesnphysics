import pygame
import math

FPS = 120
time_increment = (1/FPS)
class Particle:
    def __init__(self, x=0, y=0, angle=0, power=0, color=(0,0,0), size=0):
        self.x = x
        self.y = y
        self.angle = angle
        self.power = power
        self.time = time_increment
        self.color = color
        self.size = size
        self.current_position = [0,0]  # used to report the current position and remove particles that are outside the window.
        self.x_velocity = math.sin(math.radians(self.angle)) * self.power
        self.y_velocity = math.cos(math.radians(self.angle)) * self.power

    def update(self):
        # setting velocity to the x/y
        self.x += self.x_velocity
        self.y -= self.y_velocity
        self.current_position = [self.x, self.y]
        
        # updating velocity based on math
        # self.x_velocity += math.sin(math.radians(self.angle)) * self.velocity
        self.y_velocity -= 9.8/80 # gravity?
        self.time += time_increment

    def draw(self, screen):
        border_thickness = 2
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, border_thickness)