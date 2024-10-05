import pygame

class Player:
    # Create and initiate a player
    def __init__(self, posX, posY, speed):
        self.posX = posX
        self.posY = posY
        self.speed = speed

    def movement(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_s]):
            self.posY += self.speed
        if (keys[pygame.K_w]):
            self.posY -= self.speed
        if (keys[pygame.K_a]):
            self.posX -= self.speed
        if (keys[pygame.K_d]):
            self.posX += self.speed

class Hitbox:
    # Create and initiate a hitbox
    def __init__(self, posX, posY, sizeX, sizeY):
        self.posX = posX
        self.posY = posY
        self.sizeX = sizeX
        self.sizeY = sizeY


    # Checks are 2 hitboxes "colliding" (is one touching other)
    # hitbox - Hitbox's class
    def DoHitboxesCollide(self, hitbox):
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
