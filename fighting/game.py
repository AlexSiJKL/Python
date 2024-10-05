from classes import *
import pygame, os

# Draw hitbox (rectangle)
def DrawHitbox(hitbox):
    pygame.draw.rect(screen, "red", (hitbox.posX, hitbox.posY, hitbox.sizeX, hitbox.sizeY))

# Draw player (dot)
def DrawPlayer(player):
    pygame.draw.circle(screen, "green", (player.posX, player.posY), 5)

# System variables
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
ASSETS_PATH = os.path.join(SCRIPT_PATH, "images")

# Pygame setup
pygame.init()
H = 600 # X-axis
W = 800 # Y-axis
screen = pygame.display.set_mode((H, W))
clock = pygame.time.Clock()
running = True

# Create player
player = Player(H // 2, W // 2, 3)

h1 = Hitbox(50,50,10,10)

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
    player.movement()
    # Draw player on the screen
    DrawPlayer(player)

    DrawHitbox(h1)

    # Update screen
    pygame.display.flip()

    # Limits FPS to 60
    clock.tick(60) 

pygame.quit()