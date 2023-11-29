import pygame


class TrafficLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 61
        self.height = 61
        self.image = pygame.image.load("images/light/traffic_light.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
