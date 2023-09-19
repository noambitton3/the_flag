from consts import *
from screen import *


def create_flag(flag_width, flag_length):
    flag_ = pygame.image.load("flag.png")
    flag_size = (flag_width, flag_length)
    flag = pygame.transform.scale(flag_, flag_size)
    return flag


def display_flag():
    screen = display_bushes()
    flag = create_flag(FLAG_WIDTH, FLAG_LENGTH)
    x = SCREEN_WIDTH - FLAG_WIDTH
    y = SCREEN_LENGTH - FLAG_LENGTH
    cord = (x, y)
    screen.blit(flag, cord)
    pygame.display.update()
    return screen


# supposed to show a net - there is a problem
def show_net(screen, square):
    for x in range(SCREEN_WIDTH):
        for y in range(SCREEN_LENGTH):
            block = pygame.Rect(x * square, y * square, square, square)
            pygame.draw.rect(screen, GREEN, block, 1)
    pygame.display.flip()
    return


game_grid = []
# created game grid matrix with 0


def create_game_grid(matrix):
    for row in range(25):
        row_list = []
        for col in range(50):
            row_list.append(0)
        matrix.append(row_list)
    return matrix


game_grid = create_game_grid(game_grid)

# need to show also the bombs and the soldier at night.
# also do not forget the time limit - just 1 second.


def create_bomb():
    bomb_ = pygame.image.load("mine.png")
    bomb = pygame.transform.scale(bomb_, BOMB_SIZE)
    return bomb


def append_bomb(matrix):
    for i in range(20):
        row = random.randint(0, 25)
        col = random.randint(0, 50)
        matrix[row][col] = "bomb"
    return matrix


def display_bomb(matrix, screen_):
    net_screen = show_net(screen_, SQUARE)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            cell = matrix[row][col]
            if cell == "bomb":
                a = 3








