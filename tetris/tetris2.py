# Example file showing a basic pygame "game loop"
import pygame, os

# Game setup
cell_size = 20
board_w = 10
board_h = 10 # 3 lines for figure creating

# pygame setup
pygame.init()
screen = pygame.display.set_mode((board_w * cell_size, board_h * cell_size))
clock = pygame.time.Clock()
running = True

# Game variables
isNeedFigure = True

game_field = [[0 for _ in range(board_h)] for _ in range(board_w)]

def Create_figure():
    global isNeedFigure, figure_coords, game_field
    if isNeedFigure == True:
        figure_coords = [(0,5), (0,6), (1,5), (1,6)]
        for x, y in figure_coords:
            game_field[x][y] = 1
        isNeedFigure = False
        return game_field, figure_coords
    
def Move_figure_left():
    global figure_coords, game_field
    new_coords = []
    can_move = True

    for x, y in figure_coords:
        if y - 1 < 0 or game_field[x][y-1] != 0:
            can_move = False
            break
            
    if can_move == True:
        for x, y in figure_coords:
            game_field[x][y] = 0

        for x, y in figure_coords:
            game_field[x][y-1] = 1

        for x, y in figure_coords:
            new_coords[x][y-1] = 1

    figure_coords = new_coords
    return figure_coords, game_field

def Move_figure_right():
    print("Right")

def Move_figure_down():
    print("Down")

def Draw_game_field():
    os.system('cls')
    for row in game_field:
        print(row)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                Move_figure_down()
            if event.key == pygame.K_LEFT:
                Move_figure_left()
            if event.key == pygame.K_RIGHT:
                Move_figure_right()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    Draw_game_field()
    Create_figure()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()