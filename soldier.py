import pygame
import consts
import game_field
import screen


def create_soldier(soldier_width, soldier_length):
    soldier_ = pygame.image.load("soldier.png")
    soldier_size = (soldier_width, soldier_length)
    soldier = pygame.transform.scale(soldier_, soldier_size)
    return soldier


def display_solider():
    screen_ = game_field.display_flag()
    soldier = create_soldier(consts.SOLDIER_WIDTH, consts.SOLDIER_LENGTH)
    x = 0
    y = 0
    init_pos = (x, y)
    screen_.blit(soldier, init_pos)
    pygame.display.update()
    return screen_


def move_up(soldier_y):
    soldier_y -= 20
    return soldier_y


def move_down(soldier_y):
    soldier_y += 20
    return soldier_y


def move_left(soldier_x):
    soldier_x += 20
    return soldier_x


def move_right(soldier_x):
    soldier_x -= 20
    return soldier_x
