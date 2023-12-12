import pygame
from traffic_light import TrafficLight
from controller import Controller

pygame.init()

WIDTH, HEIGHT = 768, 768

MAP = pygame.image.load("images/crossroads.jpg")
MAP = pygame.transform.scale(MAP, (WIDTH, HEIGHT))

logo = pygame.image.load("images/light/logo.png")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic Light on CrossRoad")
pygame.display.set_icon(logo)

traffic_light_1 = TrafficLight(175, 110)
traffic_light_2 = TrafficLight(510, 170)
traffic_light_3 = TrafficLight(100, 450)
traffic_light_4 = TrafficLight(460, 500)
TrafficLights = [traffic_light_1, traffic_light_2, traffic_light_3, traffic_light_4]

controller = Controller(TrafficLights)
controller.place(WIDTH - controller.width, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if event.button == 1:
                for traffic_light in TrafficLights:
                    if traffic_light.hitbox.collidepoint(mouse_x, mouse_y):
                        traffic_light.hitboxColor = "green"
                        traffic_light.selected = True
                controller.click(mouse_x, mouse_y)

            elif event.button == 3:
                for traffic_light in TrafficLights:
                    traffic_light.hitboxColor = "purple"
                    traffic_light.selected = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                for traffic_light in TrafficLights:
                    if traffic_light.selected:
                        traffic_light.change_state("red")
            elif event.key == pygame.K_2:
                for traffic_light in TrafficLights:
                    if traffic_light.selected:
                        traffic_light.change_state("yellow")
            elif event.key == pygame.K_3:
                for traffic_light in TrafficLights:
                    if traffic_light.selected:
                        traffic_light.change_state("green")

    pygame.display.update()
    screen.blit(MAP, (0, 0))
    controller.draw(screen)
    controller.update()

    for traffic_light in TrafficLights:
        traffic_light.draw(screen)
        traffic_light.update()
        if controller.state == "play_1x" or controller.state == "play_2x":
            traffic_light.work_process()
