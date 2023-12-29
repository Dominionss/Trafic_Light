import pygame


class Field:
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def place(self, screen):
        pygame.draw.rect(screen, "pink", pygame.Rect(self.x, self.y, self.width, self.height), 2)
