import pygame


class Button:
    def __init__(self, x, y, type_of_button):
        self.x = x
        self.y = y
        self.size = 60
        self.type_of_button = type_of_button
        self.hitbox = pygame.Rect(x, y, self.size, self.size)
        if type_of_button == "pause":
            self.image = pygame.image.load(f"images/buttons/{type_of_button}_pressed.png")
            self.pressed = True
        else:
            self.image = pygame.image.load(f"images/buttons/{type_of_button}_not_pressed.png")
            self.pressed = False
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        if self.pressed:
            self.image = pygame.image.load(f"images/buttons/{self.type_of_button}_pressed.png")
        else:
            self.image = pygame.image.load(f"images/buttons/{self.type_of_button}_not_pressed.png")
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
