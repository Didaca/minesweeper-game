import pygame
import random

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
MINES = 10
FIELD = []

# Cube parameters
CUBE_COLOR = "#3C3F41"
CUBE_SIZE = WIDTH // COLUMNS
CUBE_RADIUS = 12
CUBE_BOMB = "bomb.png"
CUBE_NUMBERS_COLOR = {1: 'white', 2: 'green', 3: 'red', 4: 'blue',
                      5: 'purple', 6: 'yellow', 7: 'lightblue', 8: 'pink'}

# Game  GUI parameters
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


def create_screen():

    for ind1, r in enumerate(FIELD):
        for ind2, c in enumerate(r):
            x = ind1 * CUBE_SIZE
            y = ind2 * CUBE_SIZE

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


while running:

    if rerun:
        create_field(ROWS, COLUMNS, MINES)
        rerun = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill(SCREEN_COLOR)

    create_screen()
    # RENDER YOUR GAME HERE

    pygame.display.flip()

pygame.quit()
