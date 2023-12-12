import pygame
from button import Button


class Controller:
    def __init__(self, traffic_lights):
        self.traffic_lights = traffic_lights
        self.x = 0
        self.y = 0
        self.counter = 0
        self.width = 195
        self.height = 70
        self.body = pygame.Rect(self.x, self.y, self.width, self.height)
        self.state = "pause"
        self.pause_button = None
        self.play_1x_button = None
        self.play_2x_button = None
        self.buttons = []

    def draw(self, screen):
        pygame.draw.rect(screen, "blue", self.body, 5)
        for button in self.buttons:
            button.draw(screen)

    def place(self, x, y):
        self.x = x
        self.y = y
        self.body.x = x
        self.body.y = y
        self.pause_button = Button(self.body.x, self.body.y + 5, "pause")
        self.play_1x_button = Button(self.body.x + 65, self.body.y + 5, "play_1x")
        self.play_2x_button = Button(self.body.x + 130, self.body.y + 5, "play_2x")
        self.buttons = [self.pause_button, self.play_1x_button, self.play_2x_button]

    def start(self):
        self.traffic_lights[0].change_state("green")
        self.traffic_lights[0].timer = 0
        self.traffic_lights[1].change_state("green")
        self.traffic_lights[1].timer = 0
        self.traffic_lights[2].change_state("green")
        self.traffic_lights[2].timer = 0
        self.traffic_lights[3].change_state("green")
        self.traffic_lights[3].timer = 0

    def update(self):
        for button in self.buttons:
            button.update()

        if self.play_1x_button.pressed and self.counter == 0:
            self.counter += 1
            self.start()

    def click(self, mouse_x, mouse_y):
        for button in self.buttons:
            if button.hitbox.collidepoint(mouse_x, mouse_y):
                for butt in self.buttons:
                    butt.pressed = False
                button.pressed = True
                self.state = button.type_of_button
                print(self.state)
