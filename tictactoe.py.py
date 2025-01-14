#gọi thư viện
import random
import sys
import pygame

pygame.init()

width = 300
height = 300
line_width = 7
board_rows = 3
board_cols = 3
square_size = 100
circle_radius = 30
circle_width = 7
cross_width = 12
space = 27

screen_coler = (28, 170, 156)
line_coler = (23, 145, 135)
circle_coler = (239, 231, 200)
cross_coler = (66, 66, 66)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic tac toe")
screen.fill(screen_coler)

list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

board = [[0 for i in range(board_cols)] for j in range(board_rows)]


def draw_lines():
    #vẽ hai đường ngang
    pygame.draw.line(screen, line_coler, (0, square_size), (width, square_size), line_width)
    pygame.draw.line(screen, line_coler, (0, 2 * square_size), (width, 2 * square_size), line_width)
    #vẽ hai đường dọc
    pygame.draw.line(screen, line_coler, (square_size, 0), (square_size, height), line_width)
    pygame.draw.line(screen, line_coler, (2 * square_size, 0), (2 * square_size, height),
                     line_width)


def draw_symbols():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:
                pygame.draw.line(
                    screen, cross_coler,
                    (col * square_size + space, row * square_size + square_size - space),
                    (col * square_size + square_size - space, row * square_size + space),
                    cross_width)

                pygame.draw.line(screen, cross_coler,
                                 (col * square_size + space, row * square_size + space),
                                 (col * square_size + square_size - space,
                                  row * square_size + square_size - space), cross_width)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, circle_coler,
                                   (int(col * square_size + square_size // 2),
                                    int(row * square_size + square_size // 2)), circle_radius,
                                   circle_width)


def draw_horizontal_winning_line(row, player):
    start_x = 0
    end_x = width
    y = row * square_size + square_size // 2
    color = cross_coler if player == 1 else circle_coler
    pygame.draw.line(screen, color, (start_x, y), (end_x, y), cross_width)


def draw_vertical_winning_line(col, player):
    start_y = 0
    end_y = height
    x = col * square_size + square_size // 2
    color = cross_coler if player == 1 else circle_coler
    pygame.draw.line(screen, color, (x, start_y), (x, end_y), cross_width)


def draw_desc_diagonal(player):
    color = cross_coler if player == 1 else circle_coler
    pygame.draw.line(screen, color, (0, 0), (width, height), cross_width)


def draw_asc_diagonal(player):
    color = cross_coler if player == 1 else circle_coler
    pygame.draw.line(screen, color, (0, height), (width, 0), cross_width)


def check_win(player):
    # kiểm tra hàng ngang
    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
    # kiểm tra hàng dọc
    for col in range(board_rows):
        if board[col][0] == player and board[col][1] == player and board[col][2] == player:
            draw_vertical_winning_line(col, player)
            return True
    # kiểm tra đường chéo
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        draw_asc_diagonal(player)
        return True
    return False


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    if board[row][col] == 0:
        return True

player = 1
game_over = False
draw_lines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = int(mouseY // square_size)
            clicked_col = int(mouseX // square_size)
            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                else:
                    player = player % 2 + 1
                draw_symbols()
        pygame.display.update()
