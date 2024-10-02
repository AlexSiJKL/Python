# Example file showing a basic pygame "game loop"
import pygame, os, sys
from PIL import Image

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font_big = pygame.font.Font(None, 70)
font_small = pygame.font.Font(None, 30)

# Function to handle gravitation and border limits
def Gameover():
    global running
    screen.fill(BLACK)
    gameover_text = font_big.render("Game over", False, WHITE)
    gameover_text_rect = gameover_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))

    continue_text = font_small.render("Press R to try again or Q to exit", False, WHITE)
    continue_text_rect = continue_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 50))
    
    screen.blit(gameover_text, (gameover_text_rect))
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
                    restart()

def restart():
    global hero_position, fall_speed, gravity, running
    hero_position = [150, 150]
    fall_speed = 0
    gravity = 0.1
    running = True

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

# System variables
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
ASSETS_PATH = os.path.join(SCRIPT_PATH, "images")

# Physics variables
fall_speed = 0
gravity = 0.1
background_speed = 1

# Hero properties (square)
hero_size = 64
hero_position = [150, 150]

# Hero frames
hero_frames = [
    pygame.image.load(os.path.join(ASSETS_PATH, 'hero_1.gif')),
    pygame.image.load(os.path.join(ASSETS_PATH, 'hero_2.gif')),
    pygame.image.load(os.path.join(ASSETS_PATH, 'hero_3.gif'))
]

frame_interval = 200
current_frame = 0
last_frame_time = pygame.time.get_ticks()

# Background properties
background_image = pygame.image.load(ASSETS_PATH + '\\background.gif')
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
    
    # Animate background
    Animate_background()

    # Gravitation
    Gravitation()

    hero_surf = hero_frames[current_frame]
    hero_rect = hero_surf.get_rect(topleft=(hero_position[0], hero_position[1]))
    
    screen.blit(hero_surf, hero_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()