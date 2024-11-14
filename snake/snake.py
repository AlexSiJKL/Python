import pygame
import random

# Game setup
cell_size = 10
game_field_w = 18
game_field_h = 32
game_field = [[0 for _ in range(game_field_w)] for _ in range(game_field_h)]
snake_position = [(5, 5), (5, 6), (5, 7), (5, 8)]
star_position = []
isStarNeed = True

# Initial direction
direction = "UP"

# pygame setup
pygame.init()
screen = pygame.display.set_mode((game_field_w * cell_size, game_field_h * cell_size))
clock = pygame.time.Clock()
running = True

def CreateStar():
    global isStarNeed, star_position
    if isStarNeed:
        while True:
            star_i = random.randint(0, game_field_h - 1)
            star_j = random.randint(0, game_field_w - 1)
            if all(star_i != x or star_j != y for (x, y) in snake_position):
                break
        star_position = (star_i, star_j)
        isStarNeed = False

def DrawGameField():
    for i, j in snake_position:
        pygame.draw.rect(screen, "blue", (j * cell_size, i * cell_size, cell_size, cell_size))
    if star_position:
        i, j = star_position
        pygame.draw.rect(screen, "red", (j * cell_size, i * cell_size, cell_size, cell_size))

def move_snake():
    global snake_position, isStarNeed, star_position

    head_x, head_y = snake_position[0]
    if direction == "UP":
        new_head_position = ((head_x - 1) % game_field_h, head_y)
    elif direction == "DOWN":
        new_head_position = ((head_x + 1) % game_field_h, head_y)
    elif direction == "LEFT":
        new_head_position = (head_x, (head_y - 1) % game_field_w)
    elif direction == "RIGHT":
        new_head_position = (head_x, (head_y + 1) % game_field_w)

    if new_head_position in snake_position:
        pygame.quit()
        return

    if new_head_position == star_position:
        snake_position.insert(0, star_position)
        star_position = []
        isStarNeed = True
        CreateStar()
    else:
        snake_position = [new_head_position] + snake_position[:-1]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            if event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((168, 223, 0))

    # Update the snake's position and check for star
    move_snake()
    CreateStar()
    DrawGameField()

    pygame.display.flip()
    clock.tick(10)  # Controls snake speed (10 FPS)

pygame.quit()
