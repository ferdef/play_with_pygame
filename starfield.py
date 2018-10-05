import sys
import random
import pygame

COLORS = [
    (150, 150, 150, 255),
    (210, 210, 210, 255),
    (255, 255, 255, 255)
]


class StarField:
    def __init__(self, size):
        self.size = size
        self.stars = []
        for counter in range(500):
            new_star = [random.randint(1, size[0]),
                        random.randint(1, size[1]),
                        random.randint(0, 2)]
            self.stars.append(new_star)

    def do_things(self, screen):
        for star in self.stars:
            star[0] += (star[2] + 1)
            if star[0] > self.size[0]:
                star[0] = 0
            screen.set_at((star[0], star[1]), COLORS[star[2]])
