# Example file showing a basic pygame "game loop"
import pygame, os, random

# Game setup
cell_size = 20
game_field_w = 10
game_field_h = 10

# pygame setup
pygame.init()
screen = pygame.display.set_mode((game_field_w * cell_size, game_field_h * cell_size))
clock = pygame.time.Clock()
running = True

# Game variables
is_figure_need = True

game_field = [[0 for _ in range(game_field_w)] for _ in range(game_field_h)]

def Create_figure():
    global is_figure_need, figure_coords, game_field, figure_variant
    if is_figure_need:
        figure_variant = random.randint(0,7)
        
        figures = {
            # 1x1
            0: [
                [1]
            ],
            # Block 2x2
            1: [
                [1, 1],
                [1, 1]
            ],
            # Line 4x1
            2: [
                [1, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            # Z
            3: [
                [1, 1, 0],
                [0, 1, 1],
                [0, 0, 0]
            ],
            # Reflected Z
            4: [
                [0, 1, 1],
                [1, 1, 0],
                [0, 0, 0]
            ],
            # L
            5: [
                [1, 0, 0],
                [1, 1, 1],
                [0, 0, 0]
            ],
            # Reflected L
            6:[
                [0, 0, 1],
                [1, 1, 1],
                [0, 0, 0]
            ],
            # T
            7: [
                [0, 1, 0],
                [1, 1, 1],
                [0, 0, 0]
            ]
        }

        figure_coords = figures.get(figure_variant)

        is_figure_need = False

        for i in range(len(figure_coords)):
            for j in range(len(figure_coords[i])):
                game_field[i][j + game_field_w//2] += figure_coords[i][j]

        print(game_field)

    
def Move_figure_left():
    global game_field
    can_move = True

    for i in range(len(game_field)):
        for j in range(len(game_field[i])):
            if game_field[i][j] == 1:
                if j - 1 < 0 or game_field[i][j-1] == 2:
                    can_move = False
                    break
            
    if can_move == True:
        for i in range(len(game_field)):
            for j in range(len(game_field[i])):
                if game_field[i][j] == 1:
                    game_field[i][j-1] = 1
                    game_field[i][j] = 0

def Move_figure_right():
    global game_field
    can_move = True

    for i in range(len(game_field)):
        for j in range(len(game_field[i])):
            if game_field[i][j] == 1:
                if j + 1 >= game_field_w or game_field[i][j+1] == 2:
                    can_move = False
                    break
            
    if can_move == True:
        for i in range(len(game_field)):
            for j in range(len(game_field[i])-1, -1, -1):
                if game_field[i][j] == 1:
                    game_field[i][j + 1] = 1
                    game_field[i][j] = 0

def Move_figure_down():
    global figure_coords, game_field, is_figure_need
    can_move = True

    for el in figure_coords:
        if el[0] + 1 >= game_field_h or (game_field[el[0]+1][el[1]] == 2):
            for el in figure_coords:
                game_field[el[0]][el[1]] = 2
                Clean_row()
            is_figure_need = True
            return
            
    if can_move == True:
        for el in figure_coords:
            game_field[el[0]][el[1]] = 0

        for el in figure_coords:
            game_field[el[0]+1][el[1]] = 1

        for i in range(len(figure_coords)):
            figure_coords[i][0] += 1

def Rotate_figure():
    global figure_coords
    can_rotate = True
    figure_coords_after_rotate = []
    if figure_variant == 0:
        pass
    elif figure_variant == 1:
        pass
    elif figure_variant == 7:
        print(figure_variant)
        print(figure_coords)

        '''
        for i in range(len(figure_coords)):
            figure_coords_after_rotate.append([figure_coords[i][1], -figure_coords[i][0]])
            print(figure_coords_after_rotate)
            figure_coords = figure_coords_after_rotate\
        '''

def Clean_row():
    row_sums = []
    rows_to_delete = []
    os.system('cls')
    for i in range(len(game_field)):
        row_sum = sum(game_field[i])
        row_sums.append(row_sum)
        print(row_sum)

        if row_sum == game_field_w * 2:
            rows_to_delete.append(i)

    for i in rows_to_delete:
        del game_field[i]
        game_field.insert(0, [0] * game_field_w)
            

def Draw_game_field():
    #os.system('cls')
    #for row in game_field:
    #    print(row)
    
    for i in range(len(game_field)):
        for j in range(len(game_field[i])):
            if game_field[j][i] == 1:
                pygame.draw.rect(screen, "blue", (i * cell_size, j * cell_size, cell_size, cell_size))
            if game_field[j][i] == 2:
                pygame.draw.rect(screen, "red", (i * cell_size, j * cell_size, cell_size, cell_size))

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
            if event.key == pygame.K_UP:
                Rotate_figure()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    Draw_game_field()
    Create_figure()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()