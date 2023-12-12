import pygame
import time


class TrafficLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 153
        self.height = 153
        self.image = pygame.image.load("images/light/traffic_light.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.propertyOfHitbox = {"x1": self.x + 37, "y1": self.y + 20, "x2": self.width - 74, "y2": self.height - 50}
        self.hitbox = pygame.Rect(self.propertyOfHitbox["x1"], self.propertyOfHitbox["y1"],
                                  self.propertyOfHitbox["x2"], self.propertyOfHitbox["y2"])
        self.hitboxColor = "purple"
        self.state = "default"
        self.selected = False
        self.timer = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(screen, self.hitboxColor, self.hitbox, 2)

    def update(self):
        if self.state == "default":
            self.image = pygame.image.load("images/light/traffic_light.png")
        elif self.state == "red":
            self.image = pygame.image.load("images/light/traffic_light_red.png")
        elif self.state == "yellow":
            self.image = pygame.image.load("images/light/traffic_light_yellow.png")
        elif self.state == "green":
            self.image = pygame.image.load("images/light/traffic_light_green.png")
        elif self.state == "off":
            self.image = pygame.image.load("images/light/traffic_light_off.png")
        elif self.state == "red_and_yellow":
            self.image = pygame.image.load("images/light/traffic_light_red_and_yellow.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def change_state(self, new_state):
        self.state = new_state

    def work_process(self):
        self.timer += 0.02
        print(self.timer)

        if int(self.timer) == 0:
            self.change_state("green")
        elif int(self.timer) >= 30 and int(self.timer) < 40:
            if int(self.timer) % 2 == 0:
                self.change_state("off")
            else:
                self.change_state("green")
        elif int(self.timer) == 40:
            self.change_state("yellow")
        elif int(self.timer) == 45:
            self.change_state("red")
        elif int(self.timer) == 75:
            self.change_state("red_and_yellow")
        elif int(self.timer) == 80:
            self.timer = 0

