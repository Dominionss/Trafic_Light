import pygame


class TrafficLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 153
        self.height = 153
        self.image = pygame.image.load("images/light/traffic_light.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(screen, "purple", self.hitbox, 2)
