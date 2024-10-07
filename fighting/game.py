from classes import *
import pygame, os

# Draw hitbox (rectangle)
def DrawHitbox(hitbox):
    pygame.draw.rect(screen, hitbox.color, (hitbox.posX, hitbox.posY, hitbox.sizeX, hitbox.sizeY))


# System variables
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
ASSETS_PATH = os.path.join(SCRIPT_PATH, "images")

# Pygame setup
pygame.init()
H = 1000 # X-axis
W = 800 # Y-axis
screen = pygame.display.set_mode((H, W))
clock = pygame.time.Clock()
running = True

# Create player
player = Player(H // 2, W // 2, 50, 100)

# Create map
map = Map()

# Start game
while running:
    # Poll for events
    for event in pygame.event.get():
        # pygame.QUIT event means the user clicked X to close your window
        if event.type == pygame.QUIT:
            running = False 
        
    # Clear screen
    screen.fill((0,0,0))

    # Controls player's movement
    player.Movement()

    # Draw player's hitbox on the screen
    player.DrawPlayerHitboxes(screen)

    # Display map
    map.DrawMap(screen)

    # Apply gravitation on player
    player.Gravity(map)

    # Update screen
    pygame.display.flip()

    # Limits FPS to 60
    clock.tick(60) 

pygame.quit()