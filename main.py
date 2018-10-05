import sys
import pygame

from starfield import StarField
from fps import FPS


def run_main():
    size = width, height = 1280, 720
    speed = [2, 2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    sf = StarField(size)
    fps = FPS()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(black)

        sf.do_things(screen)
        fps.show_fps(screen)

        pygame.display.flip()


if __name__ == '__main__':
    run_main()
