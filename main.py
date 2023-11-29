import pygame
from traffic_light import TrafficLight

pygame.init()

WIDTH, HEIGHT = 768, 768

MAP = pygame.image.load("images/crossroads.jpg")
MAP = pygame.transform.scale(MAP, (WIDTH, HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))

TrafficLights = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    pygame.display.update()
    screen.blit(MAP, (0, 0))

