import pygame
import os
import math
from random import choice


bottom_to_right = [(430, 729), (430, 533), (473, 475), (530, 430), (600, 420), (650, 416), (723, 415), (780, 414)]
bottom_to_left = [(430, 693), (430, 499), (427, 390), (397, 320), (290, 308), (178, 308), (25, 309), (-20, 308)]
bottom_to_top = [(430, 693), (430, 499), (430, 200), (430, 50), (430, -50)]
bottom = [bottom_to_left, bottom_to_top, bottom_to_right]

top_to_bottom = [(315, 56), (315, 271), (315, 509), (315, 696), (315, 820)]
top_to_left = [(315, 175), (283, 234), (180, 300), (100, 305), (17, 305)]
top_to_right = [(315, 102), (315, 211), (315, 329), (356, 425), (463, 415), (597, 415), (740, 415), (800, 415)]
top = [top_to_left, top_to_right, top_to_bottom]

left_to_top = [(150, 415), (278, 415), (392, 399), (425, 273), (425, 137), (425, 31), (425, -30)]
left_to_right = [(150, 415), (278, 415), (500, 415), (700, 415), (800, 415)]
left_to_bottom = [(163, 415), (270, 455), (320, 550), (318, 600), (315, 700), (315, 750), (315, 850)]
left = [left_to_top, left_to_right, left_to_bottom]

right_to_top = [(711, 307), (547, 307), (457, 231), (425, 69), (425, -50)]
right_to_bottom = [(611, 308), (466, 308), (356, 348), (315, 460), (315, 608), (315, 752), (315, 850)]
right_to_left = [(770, 308), (466, 308), (250, 308), (100, 308), (-100, 308)]
right = [right_to_top, right_to_bottom, right_to_left]

all_places = ["left", "right", "top", "bottom"]
all_paths = {"left": left, "right": right, "top": top, "bottom": bottom}
all_sides = {"left": (-30, 415, 270), "right": (770, 305, 90), "top": (315, -40, 180), "bottom": (430, 760, 0)}

cars_images = []
for car in os.listdir("images/cars"):
    cars_images.append(pygame.image.load("images/cars/" + car))


def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)


class Car:
    def __init__(self):
        self.width = 25
        self.height = 50
        self.image = cars_images[0]
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.velocity = 1
        self.rotation_vel = 2

        self.place = choice(all_places)
        self.start = all_sides[self.place]
        self.side = all_paths[self.place]
        self.path = choice(self.side)
        self.current_point = 0
        self.angle = self.start[2]
        self.x, self.y = self.start[0], self.start[1]
        self.hit_box = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        blit_rotate_center(screen, self.image, (self.x, self.y), self.angle)
        # self.draw_path(screen)

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
