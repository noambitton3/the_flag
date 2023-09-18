import pygame
import consts

def create_soldier(soldier_width, soldier_length):
    soldier_ = pygame.image.load("soldier.png")
    soldier_size = (soldier_width, soldier_length)
    soldier = pygame.transform.scale(soldier_, soldier_size)
    return soldier

def display_solider(screen):
    soldier = create_soldier(consts.SOLDIER_WIDTH, consts.SOLDIER_LENGTH)
    x = 0
    y = 0
    init_pos = (x, y)
    screen.blit(soldier, init_pos)
    pygame.display.update()
    return screen