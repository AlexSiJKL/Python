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

# Colors and gifs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
random_rect_bottom_surf = pygame.image.load(os.path.join(ASSETS_PATH, 'wood_bottom.gif'))
random_rect_top_surf = pygame.image.load(os.path.join(ASSETS_PATH, 'wood_top.gif'))

# Font
font_big = pygame.font.Font(None, 70)
font_small = pygame.font.Font(None, 30)

# Hero
def Hero():
    global hero_rect, current_frame, last_frame_time
    now = pygame.time.get_ticks()
    if now - last_frame_time > frame_interval:
        current_frame = (current_frame + 1) % len(hero_frames)
        last_frame_time = now
    global hero_rect
    hero_surf = hero_frames[current_frame]
    hero_rect = hero_surf.get_rect(topleft=(hero_position[0], hero_position[1]))
    return screen.blit(hero_surf, hero_rect)

# Bills and coins

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
    global hero_position, fall_speed, gravity, running, points, obstacles, worm_money
    points = 0
    hero_position = [150, 150]
    fall_speed = 0
    gravity = 0.1
    running = True
    obstacles = [Generate_2_random_rectangles() for _ in range (1)]
    worm_money = Create_worm_money()
    

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
    global points
    for random_rect_top, random_rect_bottom in obstacles:
        if hero_rect.colliderect(random_rect_top) or hero_rect.colliderect(random_rect_bottom):
            Gameover()
    if hero_rect.colliderect(worm_money):
        points += 500
        worm_money.x +=900 # move worm money to new position

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

# Worm money
def Create_worm_money():
    rect_worm_money_width = 110
    rect_worm_money_height = 72
    rect_worm_money_x = 975 # 975
    rect_worm_money_y = random.randint(1,528)

    rect_worm_money = pygame.Rect(rect_worm_money_x, rect_worm_money_y, rect_worm_money_width, rect_worm_money_height)

    return rect_worm_money

worm_money = Create_worm_money()
is_worm_money_need = False
current_worm_money_frame = 0
last_worm_money_frame_time = pygame.time.get_ticks()
worm_money_frame_interval = 200  # 200 ms between frames

def Move_worm_money():
    global current_worm_money_frame, last_worm_money_frame_time, worm_money

    now = pygame.time.get_ticks()
    if now - last_worm_money_frame_time > worm_money_frame_interval:
        current_worm_money_frame = (current_worm_money_frame + 1) % len(worm_money_frames)
        last_worm_money_frame_time = now
    worm_money.x -= background_speed
    screen.blit(worm_money_frames[current_worm_money_frame], (worm_money.x, worm_money.y))
    
    if worm_money.x < (-worm_money.width): worm_money = Create_worm_money() # Create new worm money if miss last one

# Obstacles generator
def Generate_2_random_rectangles():
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

obstacles = [Generate_2_random_rectangles() for _ in range (1)]

def Obstacles_if():
    # Check last rect in the list
    if obstacles[-1][0].right < 600:
        obstacles.append(Generate_2_random_rectangles())
    # Delete first pair of rects
    if obstacles[0][0].right < 0:
        obstacles.pop(0)
       
def Obstacles_moving(): 
    for random_rect_top, random_rect_bottom in obstacles:
        random_rect_top.x -= background_speed
        random_rect_bottom.x -= background_speed

        screen.blit(random_rect_bottom_surf, (random_rect_bottom.x, random_rect_bottom.y))
        screen.blit(random_rect_top_surf, (random_rect_top.x, random_rect_top.y - 400 + random_rect_top.height))

def Obstacles():
    Obstacles_if()
    Obstacles_moving()

def Points():
    global points
    points += background_speed
    points_text = font_small.render(("Your score is " + str(round(points, 2)) + " points"), True, RED)
    points_text_rect = points_text.get_rect(topleft=(20,20))
    pygame.draw.rect(screen, WHITE, points_text.get_rect(topleft=(20,20)).inflate(10, 10)) # .inflate increases the rectangle (#,#)
    screen.blit(points_text, (points_text_rect))

# Physics variables
fall_speed = 0
gravity = 0.1
background_speed = 1

# Points
points = 0

# Hero properties (square)
hero_size = 50
hero_position = [150, 150]

# Hero frames
hero_frames = [
    pygame.image.load(os.path.join(ASSETS_PATH, 'hero_1.gif')),
    pygame.image.load(os.path.join(ASSETS_PATH, 'hero_2.gif')),
    pygame.image.load(os.path.join(ASSETS_PATH, 'hero_3.gif')),
    pygame.image.load(os.path.join(ASSETS_PATH, 'hero_2.gif'))
]
# Worm money
worm_money_frames = [
    pygame.image.load(os.path.join(ASSETS_PATH, '500_1.gif')),
    pygame.image.load(os.path.join(ASSETS_PATH, '500_2.gif')),
    pygame.image.load(os.path.join(ASSETS_PATH, '500_3.gif')),
    pygame.image.load(os.path.join(ASSETS_PATH, '500_2.gif'))
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
        
        # Keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fall_speed = -3 # Jumping higth
    
    Animate_background()
    Hero()
    Gravitation()
    Obstacles()
    Collision_detection()
    Points()
    Move_worm_money()

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()