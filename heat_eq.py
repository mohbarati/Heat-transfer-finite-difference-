import numpy as np
import pygame
from pygame.locals import *


n = 60
wall_values = {"left wall": 100, "right wall": 100, "top wall": 100, "bottom wall": 100}
x_left_init = np.zeros(n) + wall_values["left wall"]
x_right_init = np.zeros(n) + wall_values["right wall"]
y_top_init = np.zeros(n) + wall_values["top wall"]
y_bottom_init = np.zeros(n) + wall_values["bottom wall"]


matrix_temp = np.ones((n, n))
matrix_temp[:, 0] = x_left_init
matrix_temp[:, -1] = x_right_init
matrix_temp[0, :] = y_top_init
matrix_temp[-1, :] = y_bottom_init


max_temp = np.amax(matrix_temp)
min_temp = np.amin(matrix_temp)


def color_map(temp, max_temp, min_temp):
    range_temp = max_temp - min_temp
    redish = round((temp - min_temp) / range_temp * 255)
    bluish = round((max_temp - temp) / range_temp * 255) / 2
    return (redish, 70, bluish)


def temperature(matrix_temp):
    # matrix_temp = np.copy(initial_matrix)
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            matrix_temp[i, j] = (
                1
                / 4
                * (
                    matrix_temp[i - 1, j]
                    + matrix_temp[i + 1, j]
                    + matrix_temp[i, j - 1]
                    + matrix_temp[i, j + 1]
                )
            )
    return matrix_temp


TILESIZE = 600 // n


def create_board_surf(matrix_temp):
    board_surf = pygame.Surface((600, 600))

    for j in range(n):
        for i in range(n):
            rect = pygame.Rect(i * TILESIZE, j * TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.rect(
                board_surf, color_map(matrix_temp[j, i], max_temp, min_temp), rect
            )
    return board_surf


pygame.init()
screen = pygame.display.set_mode((600, 600))
cont = True
while cont:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            cont = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            pass
        if e.type == pygame.MOUSEBUTTONUP:
            pass
    matrix_temp[:] = temperature(matrix_temp)
    screen.fill(pygame.Color("grey"))
    screen.blit(create_board_surf(matrix_temp), (0, 0))
    pygame.display.flip()

pygame.quit()
