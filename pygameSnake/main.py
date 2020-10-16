from apple import *
from snake import *
from Part import *
import random

pygame.init()
pygame.font.init()
STAT_FONT = pygame.font.SysFont('comicsans', 25)


def draw(win, score, apple, snake):
    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - text.get_width() - PIXEL_BOARDER, 10))
    apple.draw(win)
    snake.draw(win)

    pygame.display.update()


def collision(obj1, obj2):
    return obj1.get_x() == obj2.get_x() and obj1.get_y() == obj2.get_y()


# assures number is on the set scale for the map
def clamp_num(num):
    while num % BLOCK_SIZE != 0:
        num += 1
    return num


# TODO make sure it is not in the snake
def make_apple():
    x = clamp_num(int(random.randrange(0, WIN_WIDTH - BLOCK_SIZE)))
    y = clamp_num(int(random.randrange(0, WIN_HEIGHT - BLOCK_SIZE)))
    return Apple(x, y)


# Todo make sure snake doesn't go into itself
def take_input(keys_pressed, snake):
    if keys_pressed[pygame.K_UP]:
        snake.set_direction(UP)
    elif keys_pressed[pygame.K_DOWN]:
        snake.set_direction(DOWN)
    elif keys_pressed[pygame.K_LEFT]:
        snake.set_direction(LEFT)
    elif keys_pressed[pygame.K_RIGHT]:
        snake.set_direction(RIGHT)


def wall_collision(snake):
    return not ((0 > snake.get_x() or snake.get_x() == WIN_WIDTH) or (
            0 == snake.get_y() or snake.get_y() == WIN_HEIGHT))


def blank_scree(win):
    pygame.draw.rect(win, (0, 0, 0), (0, 0, WIN_WIDTH, WIN_HEIGHT))


def main():
    loop_count = 0
    score = 0
    apple = make_apple()
    snake = Snake(Part(SNAKE_START_X, SNAKE_START_Y))
    eaton = False

    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FRAME_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        take_input(pygame.key.get_pressed(), snake)
        if eaton:
            apple = make_apple()
            eaton = False
        # checks if apple is hit
        if collision(apple, snake):
            snake.add_part()
            eaton = True
            score += SCORE_INCREMENT
        # exit if you hit a wall or if snake hits self
        running = wall_collision(snake)
        # allows the game to take input at the framerate but only draw in the specified interval
        if loop_count % GAME_CLOCK_SPEED == 0:
            snake.move()
            draw(win, score, apple, snake)
        loop_count += 1
        if loop_count > 254:
            loop_count = 0
        blank_scree(win)

    pygame.quit()
    quit()


main()
