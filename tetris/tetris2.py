# Example file showing a basic pygame "game loop"
import pygame

# Game setup
cell_size = 20
board_w = 20
board_h = 20 # 3 lines for figure creating

# pygame setup
pygame.init()
screen = pygame.display.set_mode((board_w * cell_size, board_h * cell_size))
clock = pygame.time.Clock()
running = True

# Game variables

for h in board_h:
    game_board = [] * board_w

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()