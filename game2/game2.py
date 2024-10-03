# Example file showing a basic pygame "game loop"
import pygame, os, sys
from PIL import Image
import random

# System variables
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
ASSETS_PATH = os.path.join(SCRIPT_PATH, "images")

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Font
font_big = pygame.font.Font(None, 70)
font_small = pygame.font.Font(None, 30)

# Hero
def Hero():
    global hero_rect
    hero_surf = hero_frames[current_frame]
    hero_rect = hero_surf.get_rect(topleft=(hero_position[0], hero_position[1]))
    return screen.blit(hero_surf, hero_rect)

# Function to handle gravitation and border limits
def Gameover():
    global running
    screen.fill(BLACK)
    gameover_text = font_big.render("Game over", False, WHITE)
    gameover_text_rect = gameover_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))

    points_text = font_small.render(("Your score is " + str(round(points, 2)) + " points"), False, WHITE)
    points_text_rect = points_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 50))

    continue_text = font_small.render("Press R to try again or Q to exit", False, WHITE)
    continue_text_rect = continue_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 80))
    
    screen.blit(gameover_text, (gameover_text_rect))
    screen.blit(points_text, (points_text_rect))
    screen.blit(continue_text, (continue_text_rect))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                waiting = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    waiting = False
                    Restart()

def Restart():
    global hero_position, fall_speed, gravity, running, random_rect_bottom, random_rect_top, points
    points = 0
    hero_position = [150, 150]
    fall_speed = 0
    gravity = 0.1
    running = True
    random_rect_top, random_rect_bottom = Generate_random_rectangle()

def Gravitation():
    global fall_speed, gravity

    # Update hero's position based on gravity
    fall_speed += gravity
    hero_position[1] += fall_speed

    # Check if the hero touches the bottom and top of the screen (collision detection)
    if hero_position[1] + hero_size >= 600: # Bottom
        hero_position[1] = 600 - hero_size
        Gameover()
        
    if hero_position[1] <= 0: # Top
        hero_position[1] = 0

def Collision_detection():
    if hero_rect.colliderect(random_rect_top) or hero_rect.colliderect(random_rect_bottom):
        Gameover()

def Animate_background():
    global background_x1, background_x2
    # Move background to the left
    background_x1 -= background_speed
    background_x2 -= background_speed

    # Loop backgrounds when they go off-screen
    if background_x1 <= -background_width:
        background_x1 = background_x2 + background_width
    if background_x2 <= -background_width:
        background_x2 = background_x1 + background_width

    # Draw the background images
    screen.blit(background_image, (background_x1, 0))
    screen.blit(background_image, (background_x2, 0))

# Obstacles generator
def Generate_random_rectangle():

    global random_rect_top, random_rect_bottom

    rect_top_width = 50
    rect_top_height = random.randint(50, (screen.get_height() - 50 - 250))
    rect_top_x = screen.get_width() + rect_top_width
    rect_top_y = 0

    rect_bottom_width = 50
    rect_bottom_height = 50 + screen.get_height() - rect_top_height - 250
    rect_bottom_x = screen.get_width() + rect_bottom_width
    rect_bottom_y = screen.get_height() - rect_bottom_height

    random_rect_top = pygame.Rect(rect_top_x, rect_top_y, rect_top_width, rect_top_height)
    random_rect_bottom = pygame.Rect(rect_bottom_x, rect_bottom_y, rect_bottom_width, rect_bottom_height)
    
    return random_rect_top, random_rect_bottom

random_rect_top, random_rect_bottom = Generate_random_rectangle()

def Obstacles_if():
    global random_rect_top, random_rect_bottom

    if random_rect_top.right < 0:
        random_rect_top, random_rect_bottom = Generate_random_rectangle()
        return random_rect_top, random_rect_bottom
       
def Obstacles_moving():
    random_rect_top.x -= background_speed
    random_rect_bottom.x -= background_speed
    random_rect_bottom_surf = pygame.image.load(os.path.join(ASSETS_PATH, 'wood_bottom.gif'))
    random_rect_top_surf = pygame.image.load(os.path.join(ASSETS_PATH, 'wood_top.gif'))
    screen.blit(random_rect_bottom_surf, (random_rect_bottom.x, random_rect_bottom.y))
    screen.blit(random_rect_top_surf, (random_rect_top.x, random_rect_top.y - 400 + random_rect_top.height))

def Obstacles():
    Obstacles_if()
    Obstacles_moving()

def Points():
    global points
    points += background_speed
    return points

# Physics variables
fall_speed = 0
gravity = 0.1
background_speed = 1

# Scores
points = 0

# Hero properties (square)
hero_size = 64
hero_position = [150, 150]

# Hero frames
hero_frames = [
    pygame.image.load(os.path.join(ASSETS_PATH, 'hero_1.gif')),
    pygame.image.load(os.path.join(ASSETS_PATH, 'hero_2.gif')),
    pygame.image.load(os.path.join(ASSETS_PATH, 'hero_3.gif')),
    pygame.image.load(os.path.join(ASSETS_PATH, 'hero_2.gif'))
]

frame_interval = 200
current_frame = 0
last_frame_time = pygame.time.get_ticks()

# Background properties
background_image = pygame.image.load(os.path.join(ASSETS_PATH, 'background.gif'))
background_width, background_height = 1000, 600
background_image = pygame.transform.scale(background_image, (background_width, background_height))

background_x1 = 0
background_x2 = background_width

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left click
                fall_speed = -3 # Jumping higth
                current_frame = (current_frame + 1) % len(hero_frames)  # Next frame
        
        # Keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fall_speed = -3 # Jumping higth
                current_frame = (current_frame + 1) % len(hero_frames)  # Next frame
    
    Animate_background()
    Hero()
    Points()
    Gravitation()
    Obstacles()
    Collision_detection()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()