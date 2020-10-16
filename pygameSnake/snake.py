from constants import *
import Part


def shift_next(part):
    if part.next is not None:
        part.set_direction(part.next.direction)


class Snake:
    parts = []
    direction = LEFT

    def __init__(self, head):
        self.head = head
        self.parts.append(head)

    # gives the length of the parts
    def get_length(self):
        return len(self.parts)

    def get_x(self):
        return self.head.x

    def get_y(self):
        return self.head.y

    # moves parts
    def move(self):
        for i in range(self.get_length()):
            # if the part is the head move it toward the current direction
            if i == 0:
                self.parts[i].move_head()
            # if not move it toward the next part
            else:
                self.parts[i].move_next()

    # adds a part
    def add_part(self):
        tail = self.parts[-1]
        x_off = 0
        y_off = 0

        if tail.direction == LEFT:
            x_off = BLOCK_SIZE
        elif tail.direction == RIGHT:
            x_off = -BLOCK_SIZE
        elif tail.direction == UP:
            y_off = BLOCK_SIZE
        else:
            y_off = -BLOCK_SIZE

        # we only have a head
        if self.get_length() == 1:
            # create a tail and add it to the snake
            self.parts.append(
                Part.Part(self.head.x + x_off, self.head.y + y_off, self.head, SNAKE_IMGS[2]))
        else:
            # set tail to body image
            tail.set_image(SNAKE_IMGS[0])
            self.parts.append(Part.Part(tail.x + x_off, tail.y + y_off, tail, SNAKE_IMGS[2]))

    # draws parts to the screen
    def draw(self, win):
        for part in self.parts:
            win.blit(part.image, (part.x, part.y))

    # updates the direction of the head
    def set_direction(self, direction):
        self.direction = direction
        self.head.direction = direction

    # check if the snake has hit itself
    # TODO correct to work
    def snake_collision(self):
        for part in self.parts:
            return part != self.head and (part.x == self.get_x and part.y == self.get_y())
