from main import *
from soldier import *

def create_flag(flag_width, flag_length):
    flag_ = pygame.image.load("flag.png")
    flag_size = (flag_width, flag_length)
    flag = pygame.transform.scale(flag_, flag_size)
    return flag
# supposed to show a net - there is a problem
def show_net(screen_, square):
    for x in range(SCREEN_WIDTH):
        for y in range(SCREEN_LENGTH):
            block = pygame.Rect(x * square, y * square, square, square)
            pygame.draw.rect(screen_, GREEN, block, 1)
    pygame.display.flip()
    return


def create_bomb():
    bomb_ = pygame.image.load("mine.png")
    bomb = pygame.transform.scale(bomb_, BOMB_SIZE)
    return bomb


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


def append_bomb(matrix):
    for i in range(20):
        row = random.randint(0, 25)
        col = random.randint(0, 50)
        matrix[row][col] = "bomb"
    return matrix


def display_bomb(screen_):
    matrix = append_bomb(game_grid)
    net_screen = show_net(screen_, SQUARE)
    bomb = create_bomb()
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            cell = matrix[row][col]
            if cell == "bomb":
                x = SQUARE * col
                y = SQUARE * row
                cord = (x, y)
                net_screen.blit(bomb, cord)
    return screen_








