import pygame
import random
from collections import deque

pygame.init()

running = True
rerun = True

# Screen parameters
WIDTH = 500
HEIGHT = 500
SCREEN_COLOR = "#D3D3D3"
SCREEN_IMAGE = "bomb32.png"

ROWS = 10
COLUMNS = 10
MINES = 8
FIELD = []
FIELD_LAYER = []
FIELD_LAYER_COLOR = "#325156"

# Cube parameters
CUBE_COLOR = "#3C3F41"
CUBE_SIZE = WIDTH // ROWS
CUBE_RADIUS = 12
CUBE_BOMB = "bomb.png"
CUBE_NUMBERS_COLOR = {1: 'white', 2: 'green', 3: 'red', 4: 'blue',
                      5: 'purple', 6: 'yellow', 7: 'lightblue', 8: 'pink'}

# Game GUI parameters
logo = pygame.image.load(SCREEN_IMAGE)
pygame.display.set_icon(logo)
pygame.display.set_caption("Minesweeper")

screen = pygame.display.set_mode([WIDTH, HEIGHT])

FONT = pygame.font.SysFont("Helvetica", 20)


def modify_cells(b_row, b_col):

    # row calc

    if b_row > 0:
        if FIELD[b_row - 1][b_col] != -1:
            FIELD[b_row - 1][b_col] += 1
    if b_row < ROWS - 1:
        if FIELD[b_row + 1][b_col] != -1:
            FIELD[b_row + 1][b_col] += 1

    # col calc

    if b_col > 0:
        if FIELD[b_row][b_col - 1] != -1:
            FIELD[b_row][b_col - 1] += 1
    if b_col < COLUMNS - 1:
        if FIELD[b_row][b_col + 1] != -1:
            FIELD[b_row][b_col + 1] += 1

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


def create_layer():

    for _ in range(ROWS):
        places = []
        for _ in range(COLUMNS):
            places.append(0)

        FIELD_LAYER.append(places)


def create_fields(rows, cols, mines):

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


def create_screen():

    for ind1, r in enumerate(FIELD):
        for ind2, c in enumerate(r):
            x = ind1 * CUBE_SIZE
            y = ind2 * CUBE_SIZE

            is_clicked = FIELD_LAYER[ind1][ind2] == 0

            if is_clicked:
                pygame.draw.rect(screen, FIELD_LAYER_COLOR, (x, y, CUBE_SIZE, CUBE_SIZE), border_radius=CUBE_RADIUS)
                pygame.draw.rect(screen, SCREEN_COLOR, (x, y, CUBE_SIZE, CUBE_SIZE), 1, border_radius=CUBE_RADIUS)
                continue
            else:
                pygame.draw.rect(screen, CUBE_COLOR, (x, y, CUBE_SIZE, CUBE_SIZE), border_radius=CUBE_RADIUS)
                pygame.draw.rect(screen, SCREEN_COLOR, (x, y, CUBE_SIZE, CUBE_SIZE), 1, border_radius=CUBE_RADIUS)

            if c < 0:
                bomb_in_cube = pygame.image.load(CUBE_BOMB)
                x_numInCube = bomb_in_cube.get_width()
                y_numInCube = bomb_in_cube.get_height()
                screen.blit(
                    bomb_in_cube,
                    (x + (CUBE_SIZE // 2 - x_numInCube / 2), y + (CUBE_SIZE // 2 - y_numInCube / 2))
                )

            if c > 0:
                number_in_cube = FONT.render(str(c), True, CUBE_NUMBERS_COLOR[c])
                x_numInCube = number_in_cube.get_width()
                y_numInCube = number_in_cube.get_height()
                screen.blit(
                    number_in_cube,
                    (x + (CUBE_SIZE // 2 - x_numInCube / 2), y + (CUBE_SIZE // 2 - y_numInCube / 2))
                )

    pygame.display.update()


def get_cell_around(r_point, c_point):
    all_around = []

    if r_point == 0 and c_point == 0:
        all_around.append([r_point, c_point + 1])
        all_around.append([r_point + 1, c_point + 1])
        all_around.append([r_point + 1, c_point])
    elif r_point == 0 and c_point == COLUMNS - 1:
        all_around.append([r_point, c_point - 1])
        all_around.append([r_point + 1, c_point - 1])
        all_around.append([r_point + 1, c_point])
    elif r_point == ROWS - 1 and c_point == COLUMNS - 1:
        all_around.append([r_point - 1, c_point])
        all_around.append([r_point - 1, c_point - 1])
        all_around.append([r_point, c_point - 1])
    elif r_point == ROWS - 1 and c_point == 0:
        all_around.append([r_point - 1, c_point])
        all_around.append([r_point - 1, c_point + 1])
        all_around.append([r_point, c_point + 1])
    elif (r_point > 0 and (r_point < ROWS - 1)) and c_point == 0:
        all_around.append([r_point - 1, c_point])
        all_around.append([r_point - 1, c_point + 1])
        all_around.append([r_point, c_point + 1])
        all_around.append([r_point + 1, c_point + 1])
        all_around.append([r_point + 1, c_point])
    elif r_point == 0 and (c_point > 0 and (c_point < COLUMNS - 1)):
        all_around.append([r_point, c_point - 1])
        all_around.append([r_point + 1, c_point - 1])
        all_around.append([r_point + 1, c_point])
        all_around.append([r_point + 1, c_point + 1])
        all_around.append([r_point, c_point + 1])
    elif (r_point > 0 and (r_point < ROWS - 1)) and c_point == COLUMNS - 1:
        all_around.append([r_point - 1, c_point])
        all_around.append([r_point - 1, c_point - 1])
        all_around.append([r_point, c_point - 1])
        all_around.append([r_point + 1, c_point - 1])
        all_around.append([r_point + 1, c_point])
    elif r_point == ROWS - 1 and (c_point > 0 and (c_point < COLUMNS - 1)):
        all_around.append([r_point, c_point - 1])
        all_around.append([r_point - 1, c_point - 1])
        all_around.append([r_point - 1, c_point])
        all_around.append([r_point - 1, c_point + 1])
        all_around.append([r_point, c_point + 1])
    elif (r_point > 0 and (r_point < ROWS - 1)) and (c_point > 0 and (c_point < COLUMNS - 1)):
        all_around.append([r_point, c_point - 1])
        all_around.append([r_point - 1, c_point - 1])
        all_around.append([r_point - 1, c_point])
        all_around.append([r_point - 1, c_point + 1])
        all_around.append([r_point, c_point + 1])
        all_around.append([r_point + 1, c_point + 1])
        all_around.append([r_point + 1, c_point])
        all_around.append([r_point + 1, c_point - 1])

    return all_around


def look_around(r_cell, c_cell):
    all_cells = deque(get_cell_around(r_cell, c_cell))
    opened = [[r_cell, c_cell]]

    while all_cells:
        r_c, c_c = all_cells[0]
        opened.append(all_cells[0])
        if FIELD[r_c][c_c] == 0:
            new_cell = get_cell_around(r_c, c_c)
            for cell in new_cell:
                if cell in opened:
                    continue
                all_cells.append(cell)
            FIELD_LAYER[r_c][c_c] = 1
            all_cells.popleft()
        else:
            FIELD_LAYER[r_c][c_c] = 1
            all_cells.popleft()


def get_coordinates(mouse):

    x_mouse, y_mouse = mouse

    row = x_mouse // CUBE_SIZE
    col = y_mouse // CUBE_SIZE

    return row, col


while running:

    if rerun:
        create_fields(ROWS, COLUMNS, MINES)
        create_layer()
        rerun = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            m_r, m_c = get_coordinates(mouse_position)

            if m_r >= ROWS or m_c >= COLUMNS:
                continue

            if FIELD[m_r][m_c] == 0:
                FIELD_LAYER[m_r][m_c] = 1
                look_around(m_r, m_c)
            elif FIELD[m_r][m_c] != -1:
                FIELD_LAYER[m_r][m_c] = 1

    screen.fill(SCREEN_COLOR)

    create_screen()
    # RENDER YOUR GAME HERE

    pygame.display.flip()

pygame.quit()
