import pygame


class FPS:
    def __init__(self):
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 25)

    def show_fps(self, screen):
        fps = self.clock.get_fps()
        textsurface = self.myfont.render("FPS: {0:.2f}".format(fps),
                                         True,
                                         (255, 255, 255))
        screen.blit(textsurface, (0, 0))
        self.clock.tick(30)
