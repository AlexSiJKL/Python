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
            mode = img.mode
            size = img.size
            data = img.convert('RGBA').tobytes()
            pygame_image = pygame.image.fromstring(data, size, mode)
            frames.append(pygame.transform.scale(pygame_image, (square_size, square_size)))  # Resize if needed
    return frames

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# Initialize square properties
square_size = 50
square_position = [150, 150]
square_color = (0, 0, 255)  # Start with a blue square

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

        # Check for mouse button click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # Get the mouse cursor position
        # Check if the click is within the square
            if (square_position[0] <= mouse_pos[0] <= square_position[0] + square_size and
                square_position[1] <= mouse_pos[1] <= square_position[1] + square_size):
                # Change the square's color to a random color
                square_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
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
    pygame.draw.rect(screen, square_color, (square_position[0], square_position[1], square_size, square_size))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()