import pygame

class Particle:
    def __init__(self, x, y, angle, velocity, color, size):
        self.x = x
        self.y = y
        self.angle = angle
        self.velocity = velocity
        self.color = color
        self.size = size

    def update(self):
        pass

    def draw(self, screen):
        border_thickness = 2
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, border_thickness)