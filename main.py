import pygame
import random

pygame.init()

running = True

# screen parameters
WIDTH = 400
HEIGHT = 600
SCREEN_COLOR = "#3C3F41"

ROWS = 6
COLUMNS = 6
MINES = 4
FIELD = []

# cube parameters
CUBE_COLOR = "#D3D3D3"
CUBE_WIDTH = 0
CUBE_RADIUS = 4

pygame.display.set_caption("Minesweeper")
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def modify_cells(b_row, b_col):

    # row calc

    if (b_row > 0) and (b_row < ROWS - 1):
        if FIELD[b_row - 1][b_col] != -1:
            FIELD[b_row - 1][b_col] += 1
        if FIELD[b_row + 1][b_col] != -1:
            FIELD[b_row + 1][b_col] += 1
    if b_row == 0:
        if FIELD[b_row + 1][b_col] != -1:
            FIELD[b_row + 1][b_col] += 1
    if b_row == ROWS - 1:
        if FIELD[b_row - 1][b_col] != -1:
            FIELD[b_row - 1][b_col] += 1

    # col calc

    if (b_col > 0) and (b_col < COLUMNS - 1):
        if FIELD[b_row][b_col - 1] != -1:
            FIELD[b_row][b_col - 1] += 1
        if FIELD[b_row][b_col + 1] != -1:
            FIELD[b_row][b_col + 1] += 1
    if b_col == 0:
        if FIELD[b_row][b_col + 1] != -1:
            FIELD[b_row][b_col + 1] += 1
    if b_col == COLUMNS - 1:
        if FIELD[b_row][b_col - 1] != -1:
            FIELD[b_row][b_col - 1] += 1

    # diagonals

    if ((b_row > 0) and (b_row < ROWS - 1)) and ((b_col > 0) and (b_col < COLUMNS - 1)):
        if FIELD[b_row - 1][b_col - 1] != -1:
            FIELD[b_row - 1][b_col - 1] += 1
        if FIELD[b_row - 1][b_col + 1] != -1:
            FIELD[b_row - 1][b_col + 1] += 1
        if FIELD[b_row + 1][b_col - 1] != -1:
            FIELD[b_row + 1][b_col - 1] += 1
        if FIELD[b_row + 1][b_col + 1] != -1:
            FIELD[b_row + 1][b_col + 1] += 1

    # borders diagonals

    if (b_row == 0) and (b_col == 0):
        if FIELD[b_row + 1][b_col + 1] != -1:
            FIELD[b_row + 1][b_col + 1] += 1
    if (b_row == ROWS - 1) and (b_col == 0):
        if FIELD[b_row - 1][b_col + 1] != -1:
            FIELD[b_row - 1][b_col + 1] += 1
    if (b_col == COLUMNS - 1) and (b_row == 0):
        if FIELD[b_row + 1][b_col - 1] != -1:
            FIELD[b_row + 1][b_col - 1] += 1
    if (b_col == COLUMNS - 1) and (b_row == ROWS - 1):
        if FIELD[b_row - 1][b_col - 1] != -1:
            FIELD[b_row - 1][b_col - 1] += 1

    # middle diagonals

    if b_row == 0 and (b_col > 0 and (b_col < COLUMNS - 1)):
        if FIELD[b_row + 1][b_col - 1] != -1:
            FIELD[b_row + 1][b_col - 1] += 1
        if FIELD[b_row + 1][b_col + 1] != -1:
            FIELD[b_row + 1][b_col + 1] += 1
    if b_row == ROWS - 1 and (b_col > 0 and (b_col < COLUMNS - 1)):
        if FIELD[b_row - 1][b_col - 1] != -1:
            FIELD[b_row - 1][b_col - 1] += 1
        if FIELD[b_row - 1][b_col + 1] != -1:
            FIELD[b_row - 1][b_col + 1] += 1
    if b_col == 0 and (b_row > 0 and (b_row < ROWS - 1)):
        if FIELD[b_row - 1][b_col + 1] != -1:
            FIELD[b_row - 1][b_col + 1] += 1
        if FIELD[b_row + 1][b_col + 1] != -1:
            FIELD[b_row + 1][b_col + 1] += 1
    if b_col == COLUMNS - 1 and (b_row > 0 and (b_row < ROWS - 1)):
        if FIELD[b_row - 1][b_col - 1] != -1:
            FIELD[b_row - 1][b_col - 1] += 1
        if FIELD[b_row + 1][b_col - 1] != -1:
            FIELD[b_row + 1][b_col - 1] += 1


def create_field(rows, cols, mines):

    mine_positions = []

    for _ in range(rows):
        places = []
        for _ in range(cols):
            places.append(0)

        FIELD.append(places)

    while mines:
        r = random.randrange(rows)
        c = random.randrange(cols)
        temp_position = r, c

        if temp_position in mine_positions:
            continue

        mine_positions.append(temp_position)
        mines -= 1
        FIELD[r][c] = -1

    for r, c in mine_positions:
        modify_cells(r, c)


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill(SCREEN_COLOR)

    create_field(ROWS, COLUMNS, MINES)


    # RENDER YOUR GAME HERE

    pygame.display.flip()

    pygame.quit()

pygame.quit()

# pygame.draw.rect(screen, CUBE_COLOR, ((r, c), (30, 30)), width=CUBE_WIDTH, border_radius=CUBE_RADIUS)
# pygame.display.update()