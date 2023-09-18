import pygame


def create_soldier(soldier_width, soldier_length):
    soldier_ = pygame.image.load("soldier.png")
    soldier_size = (soldier_width, soldier_length)
    soldier = pygame.transform.scale(soldier_, soldier_size)
    return soldier

