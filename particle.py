import pygame
import math

class Particle:
    def __init__(self, x=0, y=0, angle=0, velocity=0, color=(0,0,0), size=0):
        self.x = x
        self.y = y
        self.x_velocity = 0
        self.y_velocity = 0
        self.angle = angle
        self.velocity = velocity/100
        self.color = color
        self.size = size
        self.current_position = [0,0]

    def update(self):
        # setting velocity to the x/y
        self.x += self.x_velocity
        self.y -= self.y_velocity
        self.current_position = [self.x, self.y]
        
        # updating velocity based on math
        self.x_velocity += math.sin(math.radians(self.angle)) * self.velocity
        self.y_velocity += math.cos(math.radians(self.angle)) * self.velocity

    def draw(self, screen):
        border_thickness = 2
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, border_thickness)