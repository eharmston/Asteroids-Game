import pygame
from shot import Shot
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y):  # Takes x and y inputs
        super().__init__(x, y, PLAYER_RADIUS)  # Adds PLAYER_RADIUS
        self.rotation = 0
        self.shoot_timer = 0 # Shoot timer
    
    # in the player class
    def triangle(self): # Player will look like a triangle
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):  # overrides draw from circleshape
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):   # Takes one argument, dt, when its called it will add players turn speed to the players current rotation
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):  # Takes one argument to modify players position. 
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # unit vector pointing straight up from (0, 0) to (0, 1), rotate that vector by the player's rotation, so it's pointing in the direction the player is facing.
        self.position += forward * PLAYER_SPEED * dt # A larger vector means faster movement.

    def shoot(self): # Creates a new shot at position of player, sets the shots velocity, and rotates to position player is facing
        if self.shoot_timer <= 0: # Prevents the player from shooting if the timer is greater than 0
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN
            

    def update(self, dt):  
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()  # Keyboard setup, moves player when pressed
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]: # Calls the shoot method
            self.shoot()

    
