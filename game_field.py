import pygame
import random
import consts
from screen import *


def create_flag(flag_width, flag_length):
    flag_ = pygame.image.load("flag.png")
    flag_size = (flag_width, flag_length)
    flag = pygame.transform.scale(flag_, flag_size)
    return flag


def display_flag():
    screen = display_bushes()
    flag = create_flag(consts.FLAG_WIDTH, consts.FLAG_LENGTH)
    x = consts.SCREEN_WIDTH - consts.FLAG_WIDTH
    y = consts.SCREEN_LENGTH - consts.FLAG_LENGTH
    cord = (x, y)
    screen.blit(flag, cord)
    pygame.display.update()
    return screen


# supposed to show a net - not working
# def show_net(screen_, square):
#     screen_.screen.fill(consts.BLACK)
#     for x in range(consts.SCREEN_WIDTH):
#         for y in range(consts.SCREEN_LENGTH):
#             block = pygame.Rect(x * square, y * square, square, square)
#             pygame.draw.rect(screen_, consts.GREEN, block, 1)
#     pygame.display.flip()

def show_net(screen_):
    black_screen = screen_.screen.fill(consts.BLACK)
    # draw just the vertical lines
    for x in range(0, consts.SCREEN_WIDTH, SQUARE):
        start = x
        for y in range(0, consts.SCREEN_LENGTH, SQUARE):
            end = y
            pygame.draw.line(black_screen, consts.GREEN, (start, 0), (end, 500), 1)
    # draw the horizontal lines
    for y in range(0, consts.SCREEN_LENGTH, SQUARE):
        pygame.draw.line(black_screen, consts.GREEN, (0, y), (1000, y), 1)
    pygame.display.flip()
    return black_screen


# created game grid matrix with 0:
# need to show also the bombs and the soldier at night.
# also do not forget the time limit - just 1 second.


def create_game_grid(matrix):
    for row in range(25):
        row_list = []
        for col in range(50):
            row_list.append(0)
        matrix.append(row_list)
    return matrix


game_grid = []
game_grid = create_game_grid(game_grid)


def create_bomb():
    bomb_ = pygame.image.load("mine.png")
    bomb = pygame.transform.scale(bomb_, consts.BOMB_SIZE)
    return bomb


# returns the matrix with the bombs
def append_bomb(matrix):
    for i in range(20):
        row = random.randint(0, 25)
        col = random.randint(0, 50)
        matrix[row][col] = "bomb"
    return matrix


# we had an idea to find the soldier's location with the matrix. it is not working as we expected.
# def soldier_location(game_grid_):
#     game_grid = append_bomb(game_grid_)
#     for row in range(3):
#         if row == 2:
#             game_grid[row][0] = "L"
#             game_grid[row][1] = "L"
#         else:
#             game_grid[row][0] = "B"
#             game_grid[row][1] = "B"
#     return game_grid


def display_bomb(screen_):
    matrix = append_bomb(game_grid)
    net_screen = show_net(screen_)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            cell = matrix[row][col]
            if cell == "bomb":
                x = consts.SQUARE * col
                y = consts.SQUARE * row
                bomb = create_bomb()
                net_screen.blit(bomb, (x, y))
    return net_screen
