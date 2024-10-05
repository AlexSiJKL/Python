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
        figure_coords = [[0,5], [0,6], [1,5], [1,6], [1,7]]
        for el in figure_coords:
            game_field[el[0]][el[1]] = 1
        isNeedFigure = False
    
def Move_figure_left():
    global figure_coords, game_field
    can_move = True

    for el in figure_coords:
        if el[1] - 1 < 0 or (game_field[el[0]][el[1]-1] == 2):
            can_move = False
            break
            
    if can_move == True:
        for el in figure_coords:
            game_field[el[0]][el[1]] = 0

        for el in figure_coords:
            game_field[el[0]][el[1]-1] = 1

        for i in range(len(figure_coords)):
            figure_coords[i][1] -= 1

def Move_figure_right():
    global figure_coords, game_field
    can_move = True

    for el in figure_coords:
        if el[1] + 1 >= board_w or (game_field[el[0]][el[1]+1] == 2):
            can_move = False
            break
            
    if can_move == True:
        for el in figure_coords:
            game_field[el[0]][el[1]] = 0

        for el in figure_coords:
            game_field[el[0]][el[1]+1] = 1

        for i in range(len(figure_coords)):
            figure_coords[i][1] += 1

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