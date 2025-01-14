
import pygame
import random

pygame.init()

width = 400
height = 400
grid_size = 4
title_size = width // grid_size
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Matching Game")

number = list(range(1, 9)) * 2
random.shuffle(number)

grid = [[number[grid_size * row + col] for col in range(grid_size)] for row in range(grid_size)]
revealed = [[False] * grid_size for row in range(grid_size)]
choice_1 = None
choice_2 = None
game_over = False
wait_time = 0

def draw_number(number, rect):
    font = pygame.font.Font(None, 75)
    text = font.render(str(number), True, BLACK)
    text_rect = text.get_rect(center=rect.center)
    screen.blit(text, text_rect)

def draw_grid():
    screen.fill(WHITE)
    for row in range(grid_size):
        for col in range(grid_size):
            rect = pygame.Rect(col * title_size, row * title_size, title_size, title_size)
            if revealed[row][col]:
                draw_number(grid[row][col], rect)
            else:
                pygame.draw.rect(screen, CYAN, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)

def check_game_over():
    for row in range(grid_size):
        for col in range(grid_size):
            if not revealed[row][col]:
                return False
    return True  

running = True
while running:
    draw_grid()
    pygame.display.flip()

    if wait_time > 0 and pygame.time.get_ticks() > wait_time:
        row1, col1 = choice_1
        row2, col2 = choice_2
        if grid[row1][col1] != grid[row2][col2]:
            revealed[row1][col1] = False
            revealed[row2][col2] = False
        choice_1 = None
        choice_2 = None
        wait_time = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and wait_time == 0:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // title_size
            col = mouse_x // title_size

            if not revealed[row][col]:
                revealed[row][col] = True

                if choice_1 is None:
                    choice_1 = (row, col)
                else:
                    choice_2 = (row, col)
                    if grid[choice_1[0]][choice_1[1]] != grid[row][col]:
                        wait_time = pygame.time.get_ticks() + 500
                    else:
                        choice_1 = None
                        choice_2 = None

                game_over = check_game_over()

pygame.quit()
