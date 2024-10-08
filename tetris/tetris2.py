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

rotate_figures_0 = {
    0: [
        [1]
    ],
    1: [
        [1]
    ],
    2: [
        [1]
    ],
    3: [
        [1]
    ]        
}

rotate_figures_1 = {
    0: [
        [1, 1],
        [1, 1]
    ],
    1: [
        [1, 1],
        [1, 1]
    ],
    2: [
        [1, 1],
        [1, 1]
    ],
    3: [
        [1, 1],
        [1, 1]
    ]
}

rotate_figures_2 = {
    0: [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ],
    1: [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]
    ],
    2: [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ],
    3: [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]
    ]
}

rotate_figures_3 = {
    0: [
        [1, 1, 0],
        [0, 1, 1],
        [0, 0, 0]
    ],
    1: [
        [0, 0, 1],
        [0, 1, 1],
        [0, 1, 0]
    ],
    2: [
        [1, 1, 0],
        [0, 1, 1],
        [0, 0, 0]
    ],
    3: [
        [0, 0, 1],
        [0, 1, 1],
        [0, 1, 0]
    ]
}

rotate_figures_4 = {
    0: [
        [0, 1, 1],
        [1, 1, 0],
        [0, 0, 0]
    ],
    1: [
        [0, 1, 0],
        [0, 1, 1],
        [0, 0, 1]
    ],
    2: [
        [0, 1, 1],
        [1, 1, 0],
        [0, 0, 0]
    ],
    3: [
        [0, 1, 0],
        [0, 1, 1],
        [0, 0, 1]
    ]
}

rotate_figures_5 = {
    0: [
        [1, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ],
    1: [
        [0, 1, 1],
        [0, 1, 0],
        [0, 1, 0]
    ],
    2: [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 1]
    ],
    3: [
        [0, 1, 0],
        [0, 1, 0],
        [1, 1, 0]
    ],
}


rotate_figures_6 = {
    0: [
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ],
    1: [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 1]
    ],
    2: [
        [0, 0, 0],
        [1, 1, 1],
        [1, 0, 0]
    ],
    3: [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ],
}

rotate_figures_7 = {
    0: [
        [0, 1, 0],
        [1, 1, 1],
        [0, 0, 0]
    ],
    1: [
        [0, 1, 0],
        [0, 1, 1],
        [0, 1, 0]
    ],
    2: [
        [0, 0, 0],
        [1, 1, 1],
        [0, 1, 0]
    ],
    3: [
        [0, 1, 0],
        [1, 1, 0],
        [0, 1, 0]
    ]
}

rotate_figures = {
    0: rotate_figures_0,
    1: rotate_figures_1,
    2: rotate_figures_2,
    3: rotate_figures_3,
    4: rotate_figures_4,
    5: rotate_figures_5,
    6: rotate_figures_6,
    7: rotate_figures_7
}

def Create_figure():
    global is_figure_need, figure_coords, game_field, figure_variant, figure_coords_lc, figure_rotate_position
    if is_figure_need:
        figure_coords_lc = [0, game_field_w//2]
        figure_rotate_position = 0
        figure_variant = random.randint(0,7)
        
        figures = {
            0: rotate_figures_0[0], # 1x1
            1: rotate_figures_1[0], # Block 2x2
            2: rotate_figures_2[0], # Line 4x1
            3: rotate_figures_3[0], # Z
            4: rotate_figures_4[0], # Reflected Z
            5: rotate_figures_5[0], # L
            6: rotate_figures_6[0], # Reflected L
            7: rotate_figures_7[0] # T
        }

        figure_coords = figures.get(figure_variant)
        is_figure_need = False

        for i in range(len(figure_coords)):
            for j in range(len(figure_coords[i])):
                game_field[i + figure_coords_lc[0]][j + figure_coords_lc[1]] += figure_coords[i][j]

    
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

    for i in range(len(game_field) -1, -1, -1):
        for j in range(len(game_field[i])):
            if game_field[i][j] == 1:
                if i + 1 >= game_field_h or (game_field[i + 1][j] == 2):
                    can_move = False
                    break
        if not can_move:
            break
                
    if can_move:
        for i in range(len(game_field) - 1, -1, -1):
            for j in range(len(game_field[i])):
                if game_field[i][j] == 1:
                    game_field[i][j] = 0
                    game_field[i + 1][j] = 1
    else:
        for i in range(len(game_field)):
            for j in range(len(game_field[i])):
                if game_field[i][j] == 1:
                    game_field[i][j] = 2
        is_figure_need = True
        Clean_row()

def Check_for_rotating():
    global can_rotate, figure_coords_lc
    can_rotate = True

    for i in range(len(figure_coords)):
        for j in range(len(figure_coords[i])):
            if i + figure_coords_lc[0] >=len(game_field) or j + figure_coords_lc[1] >=len(game_field[0]):
                can_rotate = False
                break
            if game_field[i+figure_coords_lc[0]][j+figure_coords_lc[1]] == 2:
                can_rotate = False
                break            
    print(can_rotate)


def Figure_rotate_position():
    global figure_rotate_position
    figure_rotate_position = (figure_rotate_position + 1) % 4

def Rotate_figure():
    global figure_rotate_position, figure_coords_lc
    Check_for_rotating()
    if can_rotate:
        Figure_rotate_position()
        print(len(figure_coords))
        for i in range(len(figure_coords)):
            for j in range(len(figure_coords[i])):
                game_field[i + figure_coords_lc[0]][j + figure_coords_lc[1]] = rotate_figures[figure_variant][figure_rotate_position][i][j]
        print(figure_rotate_position)
    
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
                if figure_coords_lc[0] + 1 < len(game_field) - len(figure_coords):
                    figure_coords_lc[0] +=1
                print(figure_coords_lc)
                Move_figure_down()
            if event.key == pygame.K_LEFT:
                if figure_coords_lc[1] - 1 >= 0:
                    figure_coords_lc[1] -=1
                print(figure_coords_lc)
                Move_figure_left()
            if event.key == pygame.K_RIGHT:
                if figure_coords_lc[1] + 1 <= len(game_field[0]) - len(figure_coords[0]):
                    figure_coords_lc[1] += 1
                print(figure_coords_lc)
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