import pygame
import os
import math


cars_images = []
for car in os.listdir("images/cars"):
    cars_images.append(pygame.image.load("images/cars/" + car))


class Car:
    def __init__(self, x, y):
        self.width = 25
        self.height = 50
        self.image = cars_images[0]
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.x, self.y = x, y

        self.path = [(442, 728), (442, 692), (441, 615), (463, 529), (513, 473), (563, 444), (613, 433), (676, 428), (736, 431), (758, 429)]
        self.current_point = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        pass

