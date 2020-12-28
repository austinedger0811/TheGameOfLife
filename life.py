import pygame
import random
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen_x = 800
screen_y = 800
width = 20
height = 20
margin = 1
x_size = screen_x // width
y_size = screen_y // height


def init_grid():
    return [[0 for x in range(x_size)] for y in range(y_size)]


def random_grid(grid):
    for x in range(x_size):
        for y in range(y_size):
            grid[x][y] = random.randint(0, 1)


def count_neighbours(grid, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            count += grid[x + i][y + j]
    return count - grid[x][y]


def print_grid(screen, grid):
    for x in range(x_size):
        for y in range(y_size):
            if grid[x][y] == 1:
                pygame.draw.rect(
                    screen, BLACK, (x * width, y * height, width, height))
            else:
                pygame.draw.rect(
                    screen, BLACK, (x * width, y * height, width, height), margin)


def update_grid(grid):
    next_grid = init_grid()
    for x in range(x_size):
        for y in range(y_size):
            if x == 0 or x == x_size - 1 or y == 0 or y == y_size - 1:
                next_grid[x][y] = 0
            else:
                count = count_neighbours(grid, x, y)
                value = grid[x][y]
                if value == 1 and (count == 2 or count == 3):
                    next_grid[x][y] = 1
                elif value == 0 and count == 3:
                    next_grid[x][y] = 1
                else:
                    next_grid[x][y] = 0

    return next_grid


# Initialise game engine
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("The Game of Life")
running = True
clock = pygame.time.Clock()
grid = init_grid()
random_grid(grid)

# Game loop
while running:

    # Check for exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    print_grid(screen, grid)
    next_grid = update_grid(grid)
    pygame.display.update()
    grid = next_grid
    clock.tick(10)

pygame.quit()
