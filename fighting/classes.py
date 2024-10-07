import pygame

class Player:
    # Create and initiate a player
    def __init__(self, posX, posY, sizeX, sizeY, speed=5, health=100, gravity=5, isFacingRight=True):
        # Set position on x-axis
        self.posX = posX
        # Set position on y-axis
        self.posY = posY
        # Set size on x-axis
        self.sizeX = sizeX
        # Set size on y-axis
        self.sizeY = sizeY
        # Set speed
        self.speed = speed
        # Set amount of maximum jumping frames
        # To count optimal frame amount: FPS / timeToJump
        self.maxJumpFrames = 30
        # Set current jumping frame
        self.curJumpFrame = 0
        # Set a variable for jumping
        self.isJumping = False
        # Set health
        self.health = health
        # Set gravity
        self.gravity = gravity
        # Set facing
        self.isFacingRight = isFacingRight
        # Create player's hitbox
        self.hitbox = Hitbox(self.posX, self.posY, self.sizeX, self.sizeY, "green")
        # Create a list of all hitboxes
        self.hitboxes = [self.hitbox]
        # Create a list of all attack hitboxes
        self.attackHitboxes = []

    def Movement(self):
        keys = pygame.key.get_pressed()
        # Move player and player's Hitboxes
        # Move left
        if (keys[pygame.K_a]):
            self.isFacingRight = False
            self.posX -= self.speed
            for hitbox in self.hitboxes:
                hitbox.posX -= self.speed
        
        # Move right
        if (keys[pygame.K_d]):
            self.isFacingRight = True
            self.posX += self.speed
            for hitbox in self.hitboxes:
                hitbox.posX += self.speed

        # Jump
        if (keys[pygame.K_SPACE]):
            if not self.isJumping:
                self.isJumping = True

        # Attack on E pressed
        if (keys[pygame.K_e]):
            self.Attack()
        


    def Attack(self, hitboxDistance=50, hitboxSizeX=50, hitboxSizeY=50):
        # Create a hitbox on distance from player center to the side player is facing
        # Facing right
        if self.isFacingRight:
            self.attackHitboxes.append(Hitbox(self.posX + self.sizeX + hitboxDistance, self.posY + int(self.sizeY // 2) - int(hitboxSizeY // 2), hitboxSizeX, hitboxSizeY))
        # Facing left
        else:
            self.attackHitboxes.append(Hitbox(self.posX - 2*hitboxDistance, self.posY + int(self.sizeY // 2) - int(hitboxSizeY // 2), hitboxSizeX, hitboxSizeY))
        
    def Gravity(self, map):
        # Reset jumping state
        if self.curJumpFrame >= self.maxJumpFrames:
            self.isJumping = False
            self.curJumpFrame = 0

        # Falling upwards = Jumping
        if self.isJumping:
            self.posY -= self.gravity
            for hitbox in self.hitboxes:
                hitbox.posY -= self.gravity
            
            self.curJumpFrame += 1

        # Apply gravity downwards
        elif not self.hitbox.DoHitboxesCollide(map.blocks):
            self.posY += self.gravity
            for hitbox in self.hitboxes:
                hitbox.posY += self.gravity

    # Draw all hitboxes
    def DrawPlayerHitboxes(self, screen):
        # Draw player's hitboxes
        for hitbox in self.hitboxes:
            pygame.draw.rect(screen, hitbox.color, (hitbox.posX, hitbox.posY, hitbox.sizeX, hitbox.sizeY))
        # Draw player's attacking hitboxes
        for hitbox in self.attackHitboxes:
            pygame.draw.rect(screen, hitbox.color, (hitbox.posX, hitbox.posY, hitbox.sizeX, hitbox.sizeY))


class Map:
    # Create and initiate a map
    def __init__(self):
        self.blocks = [Block(100, 600, 800, 100, "green", False)]

    # Draw every block from the list on the screen
    def DrawMap(self, screen):
        for block in self.blocks:
            pygame.draw.rect(screen, block.color, (block.posX, block.posY, block.sizeX, block.sizeY))


class Block:
    # Create and initiate a block
    def __init__(self, posX, posY, sizeX, sizeY, color, isPassable):
        # Set position on x-axis
        self.posX = posX
        # Set position on y-axis
        self.posY = posY
        # Set size on x-axis
        self.sizeX = sizeX
        # Set size on y-axis
        self.sizeY = sizeY
        # Set color
        self.color = color
        # Set passibility (can you walk trough the block: True - yes; False - no)
        self.isPassable = isPassable
        # Create a hitbox
        self.hitbox = Hitbox(self.posX, self.posY, self.sizeX, self.sizeY, "red")
    


class Hitbox:
    # Create and initiate a hitbox
    # color="red", means that if you won't set a value for it, it will by default be "red"
    def __init__(self, posX, posY, sizeX, sizeY, color="red"):
        # Set position on x-axis
        self.posX = posX
        # Set position on y-axis
        self.posY = posY
        # Set size on x-axis
        self.sizeX = sizeX
        # Set size on y-axis
        self.sizeY = sizeY
        # Set color
        self.color = color


    # Checks are list of hitboxes "colliding" (is one touching other) with the self.hitbox
    # hitbox - Hitbox's class
    def DoHitboxesCollide(self, hitboxes):
        for hitbox in hitboxes:
            # Check each angle for colliding in other hitbox
            # Top left, other hitbox
            if (self.posX <= hitbox.posX <= self.posX + self.sizeX) and (self.posY <= hitbox.posY <= self.posY + self.sizeY):
                return True
            # Top right, other hitbox
            if (self.posX <= hitbox.posX + hitbox.sizeX <= self.posX + self.sizeX) and (self.posY <= hitbox.posY <= self.posY + self.sizeY):
                return True
            # Down left, other hitbox
            if (self.posX <= hitbox.posX <= self.posX + self.sizeX) and (self.posY <= hitbox.posY + hitbox.sizeY <= self.posY + self.sizeY):
                return True
            # Down right, other hitbox
            if (self.posX <= hitbox.posX + hitbox.sizeX <= self.posX + self.sizeX) and (self.posY <= hitbox.posY + hitbox.sizeY <= self.posY + self.sizeY):
                return True
            
            # Check each angle for colliding in self hitbox
            # Top left, self hitbox
            if (hitbox.posX <= self.posX <= hitbox.posX + hitbox.sizeX) and (hitbox.posY <= self.posY <= hitbox.posY + hitbox.sizeY):
                return True
            # Top right, self hitbox
            if (hitbox.posX <= self.posX + self.sizeX <= hitbox.posX + hitbox.sizeX) and (hitbox.posY <= self.posY <= hitbox.posY + hitbox.sizeY):
                return True
            # Down left, self hitbox
            if (hitbox.posX <= self.posX <= hitbox.posX + hitbox.sizeX) and (hitbox.posY <= self.posY + self.sizeY <= hitbox.posY + hitbox.sizeY):
                return True
            # Down right, self hitbox
            if (hitbox.posX <= self.posX + self.sizeX <= hitbox.posX + hitbox.sizeX) and (hitbox.posY <= self.posY + self.sizeY <= hitbox.posY + hitbox.sizeY):
                return True
            
            # If not colliding
            return False