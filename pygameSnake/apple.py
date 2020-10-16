from constants import *


class Apple:
    def __init__(self, x, y):
        self.image = APPLE_IMG
        self.x = x
        self.y = y

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.image)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
