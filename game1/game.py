# Basic Pygame "game loop" with moving background and GIF animation
import pygame, os
from PIL import Image


# Function to load GIF and convert it to Pygame frames
def Load_gif(filename):
	frames = []
	with Image.open(filename) as img:
		for frame in range(0, img.n_frames):
			img.seek(frame)
			img = img.convert('RGBA')  # Ensure the image is in RGBA mode
			data = img.tobytes()  # Get the byte data
			size = img.size
			# Create a pygame image from string
			pygame_image = pygame.image.fromstring(data, size, 'RGBA')  # Use 'RGBA' as the format
			frames.append(pygame.transform.scale(pygame_image, (hero_size, hero_size)))  # Resize if needed
	return frames

# Function to handle the game over event
def Handle_gameover():
    print("You lose!")

# Function to handle gravitation and border limits
def Gravitation():
    global fall_speed, gravity, is_Jumping

    # Update hero's position based on gravity
    fall_speed += gravity
    hero_position[1] += fall_speed

    # Check if the hero touches the bottom and top of the screen (collision detection)
    if hero_position[1] + hero_size >= 600: # Bottom
        hero_position[1] = 600 - hero_size
        fall_speed = 0
        gravity = 0.1
        is_Jumping = False
        
    if hero_position[1] <= 0: # Top
        hero_position[1] = 0
        fall_speed = 0
        gravity = -0.1
        is_Jumping = False

def Animate():
    global frame_index, rotation_angle
    # Render the current frame of the hero's GIF with rotation
    if gif_frames:
        rotated_image = pygame.transform.rotate(gif_frames[frame_index], rotation_angle)
        rotated_rect = rotated_image.get_rect(center=(hero_position[0] + hero_size // 2, hero_position[1] + hero_size // 2))
        screen.blit(rotated_image, rotated_rect.topleft)

    # Update the frame index for the hero's GIF animation
    frame_index = (frame_index + 1) % len(gif_frames)

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

def Draw_laser():
    # Get mouse position
    msPos = pygame.mouse.get_pos()
    
    # Draw laser
    pygame.draw.line(screen, RED, (hero_position[0], hero_position[1]), msPos, 4)


# System variables
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
ASSETS_PATH = os.path.join(SCRIPT_PATH, "images")

# Initialize pygame and set up the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# Color variables
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Laser variables
shooting_laser = False

# Hero properties (square)
hero_size = 64
hero_position = [150, 150]

# Background properties
background_image = pygame.image.load(ASSETS_PATH + '\\background.gif')
background_width, background_height = 1000, 600
background_image = pygame.transform.scale(background_image, (background_width, background_height))

background_x1 = 0
background_x2 = background_width

# Amination variables
frame_index = 0  # Initialize frame index for animation

# Rotation variables
rotation_angle = 0  # Initial angle for rotation

# Physics variables
fall_speed = 0
gravity = 0.1
background_speed = 1
is_Jumping = True # Jumping check
is_Floor = False # Position check

# Define a custom event for game over
GAMEOVER_EVENT = pygame.USEREVENT + 1


# Load GIF frames for the hero
gif_frames = Load_gif(ASSETS_PATH + '\hero.gif')
if not gif_frames:  # Check if frames were loaded successfully
	print("Error: No frames loaded from GIF.")
	running = False  # Exit if no frames loaded


# Set cursor to an image
pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR))

# Main game loop
while running:
    # Poll for events (such as closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == GAMEOVER_EVENT:
            Handle_gameover()

        # Mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left click
                if not is_Jumping and not is_Floor:
                    fall_speed = -5 # Jumping higth
                    is_Jumping = True
                elif not is_Jumping and is_Floor:
                    fall_speed = 5 # Reverse jumping higth
                    is_Jumping = True    
            elif event.button == 2: # Middle click
                print("Middle click")
            elif event.button == 3: # Right click
                fall_speed = -10 if not is_Floor else 10  # Change fall speed according to the new gravity
                gravity = -gravity
                is_Floor = not is_Floor
                is_Jumping = True
        
        # Keyboard button clicks
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shooting_laser = True


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                shooting_laser = False

    # Animate background
    Animate_background()

    # Handle gravitation
    Gravitation()

    # Animation
    Animate()

    # Increment the rotation angle for each frame
    if is_Floor: rotation_angle += 2.5  # Adjust the speed of rotation as needed
    else: rotation_angle -= 2.5
    if rotation_angle >= 360:
        rotation_angle = 0  # Reset the angle if it exceeds 360 degrees

    # Draw laser
    if shooting_laser: Draw_laser()

    # Update the display with the rendered content
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)