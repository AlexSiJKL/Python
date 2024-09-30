# Basic Pygame "game loop" with moving background and GIF animation
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

# Initialize pygame and set up the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# Hero properties (square)
square_size = 64
square_position = [150, 150]

# Background properties
background_image = pygame.image.load('game1/images/background.gif')
background_width, background_height = 1000, 600
background_image = pygame.transform.scale(background_image, (background_width, background_height))

background_x1 = 0
background_x2 = background_width

# Load GIF frames for the hero
gif_frames = load_gif('game1/images/hero.gif')
if not gif_frames:  # Check if frames were loaded successfully
	print("Error: No frames loaded from GIF.")
	running = False  # Exit if no frames loaded

frame_index = 0  # Initialize frame index for animation

# Physics variables
fall_speed = 0
gravity = 0.1
background_speed = 1

# Define a custom event for game over
GAMEOVER_EVENT = pygame.USEREVENT + 1

# Function to handle the game over event
def handle_gameover():
	print("You lose!")

# Main game loop
while running:
	# Poll for events (such as closing the window)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == GAMEOVER_EVENT:
			handle_gameover()

	# Update hero's position based on gravity
	fall_speed += gravity
	square_position[1] += fall_speed

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

	# Check if the hero touches the bottom of the screen (collision detection)
	if square_position[1] + square_size >= 600:
		square_position[1] = 600 - square_size
		fall_speed = 0
		# pygame.event.post(pygame.event.Event(GAMEOVER_EVENT))  # Trigger game over

	# Render the current frame of the hero's GIF
	if gif_frames:
		screen.blit(gif_frames[frame_index], (square_position[0], square_position[1]))

	# Update the frame index for the hero's GIF animation
	frame_index = (frame_index + 1) % len(gif_frames)

	# Update the display with the rendered content
	pygame.display.flip()

	# Cap the frame rate at 60 FPS
	clock.tick(60)

# Quit pygame when the game loop ends
pygame.quit()