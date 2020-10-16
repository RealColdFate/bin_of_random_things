from constants import LEFT
from constants import RIGHT
from constants import UP
from constants import BLOCK_SIZE
from constants import SNAKE_IMGS


class Part:

    def __init__(self, x, y, next_part=None, image=SNAKE_IMGS[1]):
        self.x = x
        self.y = y
        self.image = image
        self.next = next_part
        if next_part is not None:
            self.direction = self.next.direction
            self.next_x = next_part.x
            self.next_y = next_part.y
        else:
            self.direction = LEFT

    def set_image(self, image):
        self.image = image

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    # moves the part to the next location
    def move_next(self):
        self.x = self.next_x
        self.y = self.next_y
        self.next_x = self.next.x
        self.next_y = self.next.y

    # moves the head
    def move_head(self):
        if self.direction == LEFT:
            self.x -= BLOCK_SIZE
        elif self.direction == RIGHT:
            self.x -= -BLOCK_SIZE
        elif self.direction == UP:
            self.y -= BLOCK_SIZE
        else:
            self.y += BLOCK_SIZE

    # TODO finish implementation
    # transforms image to the proper rotation
    def turn_image(self):
        if not self.x == self.next_x or self.y == self.next_y:
            self.image = SNAKE_IMGS[3]
        else:
            self.image = SNAKE_IMGS[0]
