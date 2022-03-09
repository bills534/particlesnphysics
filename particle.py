import pygame

class Particle:
    def __init__(self, x=0, y=0, angle=0, velocity=0, color=(0,0,0), size=0):
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