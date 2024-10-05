# Example file showing a basic pygame "game loop"
import pygame, os

# pygame setup
pygame.init()
screen = pygame.display.set_mode((100, 100))
clock = pygame.time.Clock()
running = True

game_field = [0] * 100

# Variables
isNeedFigure = True

def Create_figure():
    global isNeedFigure
    if isNeedFigure == True:
        game_field[4] = 1
        game_field[13] = 1
        game_field[14] = 1
        game_field[15] = 1
        game_field[24] = 1
        isNeedFigure = False

def Draw_game_field():
    os.system('cls')
    #print(game_field)

    element_w = screen.get_width() // 10
    element_h = screen.get_height() // 10

    for i, element in enumerate(game_field):
        element_pos_w = (i % 10) * element_w
        element_pos_h = (i // 10) * element_h
        if element == 1:
            pygame.draw.rect(screen, "blue", (element_pos_w, element_pos_h, element_w, element_h))
        if element == 2:
            pygame.draw.rect(screen, "red", (element_pos_w, element_pos_h, element_w, element_h))

# Get left and right range of each 10 row
def Get_range(i):
    global left_range, right_range
    left_range = (i // 10) * 10
    right_range = left_range + 9
    return [left_range, right_range]

def Move_figure_down():
    global isNeedFigure
    to_move = []  # List of elements to move
    is_OK_move = True 
    
    # Collect indices of all elements that need to be moved
    for i, element in enumerate(game_field):
        if element == 1:
            to_move.append(i)

    # Check if all elements can be moved down
    for i in to_move:
        if (i + 10) >= len(game_field) or game_field[i + 10] == 2:  # Check boundary or obstacle
            is_OK_move = False
            break

    # If it's possible to move down, move all elements
    if is_OK_move:
        for i in reversed(to_move):  # Move in reverse order to avoid overwriting data
            game_field[i] = 0  # Clear the old position
            game_field[i + 10] = 1  # Move 10 rows down
    else:
        # If at least one element can't be moved, turn all into 2
        for i in to_move:
            game_field[i] = 2
        isNeedFigure = True

def Move_figure_left():
    to_move = []  # List of elements to move

    # Collect indices of all elements that need to be moved left
    for i, element in enumerate(game_field):
        if element == 1:
            range_index = Get_range(i)
    
    # Check if we can move the element left
    if i > range_index[0] and game_field[i - 1] == 0:
        to_move.append(i)

    # Move elements left after collecting all indices
    for i in to_move:
        game_field[i] = 0
        game_field[i - 1] = 1


def Move_figure_right():
    to_move = []  # List of elements to move

    # Collect indices of all elements that need to be moved right
    for i in range(len(game_field) - 1, -1, -1):
        if game_field[i] == 1:
            range_index = Get_range(i)
            # Check if we can move the element right
            if i < range_index[1] and game_field[i + 1] == 0:
                to_move.append(i)

    # Move elements right after collecting all indices
    for i in to_move:
        game_field[i] = 0
        game_field[i + 1] = 1



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