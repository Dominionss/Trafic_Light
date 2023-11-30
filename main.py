import pygame
from traffic_light import TrafficLight

pygame.init()

WIDTH, HEIGHT = 768, 768

MAP = pygame.image.load("images/crossroads.jpg")
MAP = pygame.transform.scale(MAP, (WIDTH, HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))

traffic_light_1 = TrafficLight(175, 110)
traffic_light_2 = TrafficLight(510, 170)
traffic_light_3 = TrafficLight(100, 450)
traffic_light_4 = TrafficLight(460, 500)
TrafficLights = [traffic_light_1, traffic_light_2, traffic_light_3, traffic_light_4]

dragging = False
selected_TL = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if event.button == 1:
                for traffic_light in TrafficLights:
                    if traffic_light.hitbox.collidepoint(mouse_x, mouse_y):
                        selected_TL = traffic_light
                        dragging = True
                        traffic_light.hitboxColor = "green"

    pygame.display.update()
    screen.blit(MAP, (0, 0))

    for traffic_light in TrafficLights:
        traffic_light.draw(screen)

