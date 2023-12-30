import pygame
import os
import math


bottom_to_right = [(430, 729), (430, 533), (473, 475), (530, 430), (600, 420), (650, 416), (723, 415), (780, 414)]
bottom_to_left = [(430, 693), (430, 499), (427, 390), (397, 320), (290, 308), (178, 308), (25, 309), (-20, 308)]
bottom_to_top = [(430, 693), (430, 499), (430, 200), (430, 50), (430, -50)]

cars_images = []
for car in os.listdir("images/cars"):
    cars_images.append(pygame.image.load("images/cars/" + car))


def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)


class Car:
    def __init__(self, x, y):
        self.width = 25
        self.height = 50
        self.image = cars_images[0]
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.x, self.y = x, y
        self.hit_box = pygame.Rect(self.x, self.y, self.width, self.height)
        self.velocity = 1
        self.rotation_vel = 3

        self.path = [(430, 693), (430, 499), (430, 200), (430, 50), (430, -50)]
        self.current_point = 0
        self.angle = 0

    def draw(self, screen):
        blit_rotate_center(screen, self.image, (self.x, self.y), self.angle)
        self.draw_path(screen)

    def draw_path(self, screen):
        for point in self.path:
            pygame.draw.rect(screen, "purple", pygame.Rect(point[0], point[1], 5, 5))

    def update(self):
        self.hit_box = pygame.Rect(self.x, self.y, self.width, self.height)
        self.move()

    def calculate_angle(self):
        target_x, target_y = self.path[self.current_point]
        x_diff = target_x - self.x
        y_diff = target_y - self.y

        if y_diff == 0:
            desired_radian_angle = math.pi / 2
        else:
            desired_radian_angle = math.atan(x_diff / y_diff)

        if target_y > self.y:
            desired_radian_angle += math.pi

        difference_in_angle = self.angle - math.degrees(desired_radian_angle)
        if difference_in_angle >= 180:
            difference_in_angle -= 360

        if difference_in_angle > 0:
            self.angle -= min(self.rotation_vel, abs(int(difference_in_angle)))
        else:
            self.angle += min(self.rotation_vel, abs(int(difference_in_angle)))

    def update_path_point(self):
        target = self.path[self.current_point]
        rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        if rect.collidepoint(*target):
            self.current_point += 1

    def move(self):
        if self.current_point >= len(self.path):
            return

        self.calculate_angle()
        self.update_path_point()
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.velocity
        horizontal = math.sin(radians) * self.velocity

        self.y -= vertical
        self.x -= horizontal
