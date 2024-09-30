# Example file showing a basic pygame "game loop"
import pygame
import random
from PIL import Image

# Function to load GIF and convert it to Pygame frames
def load_gif(filename):
    frames = []
    with Image.open(filename) as img:
        for frame in range(0, img.n_frames):
            img.seek(frame)
            img = img.convert('RGBA')  # Ensure the image is in RGBA mode
            data = img.tobytes()  # Get the byte data
            size = img.size
            # Create a pygame image from string
            pygame_image = pygame.image.fromstring(data, size, 'RGBA')  # Use 'RGBA' as the format
            frames.append(pygame.transform.scale(pygame_image, (square_size, square_size)))  # Resize if needed
    return frames

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# Initialize square properties
square_size = 64
square_position = [150, 150]

# Load GIF frames
gif_frames = load_gif('game1/images/hero.gif')
if not gif_frames:  # Check if frames were loaded
    print("Error: No frames loaded from GIF.")
    running = False  # Exit if no frames loaded

frame_index = 0

#physics
fallSpeed = 0
gravity = 0.1

# Define a custom event for gameover
GAMEOVER_EVENT = pygame.USEREVENT + 1

# Function to handle the lose event
def handle_gameover():
    print("You lose!")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check for the game over event
        if event.type == GAMEOVER_EVENT:
            handle_gameover()  # Call the game over handler function

    # Update square position for gravity
    fallSpeed += gravity
    square_position[1] += fallSpeed

    # Check for collision with the bottom of the screen
    if square_position[1] + square_size >= 600:
        square_position[1] = 600 - square_size
        fallSpeed = 0
        pygame.event.post(pygame.event.Event(GAMEOVER_EVENT))

    # Fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    # Draw the current frame of the GIF
    if gif_frames:  # Check if there are frames loaded
        screen.blit(gif_frames[frame_index], (square_position[0], square_position[1]))

    # Update frame index for GIF animation
    frame_index = (frame_index + 1) % len(gif_frames)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()