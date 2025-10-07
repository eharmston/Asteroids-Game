import pygame
from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen): # Drawing the Asteroid on screen
        pygame.draw.circle(screen,"white", self.position, self.radius, 2)

    def update(self, dt): # it moves in a straight line at constant speed
        self.position += self.velocity * dt

    def split(self):
        self.kill() # think about it: this asteroid is always destroyed
        
        
        # If the radius of the asteroid is less than or equal to ASTEROID_MIN_RADIUS, just return, this was a small asteroid and we're done
        # Otherwise spawn 2 new asteroids
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS # Compute the new radius of the smaller asteroids using the formula old_radius - ASTEROID_MIN_RADIUS

        # Use the rotate method on the asteroid's velocity vector to create 2 new vectors, that are rotated by random_angle and -random_angle respectively (they should split in opposite directions).
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # Create two new Asteroid objects at the current asteroid position with the new radius.
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Set the first and second's velocity to the new vectors, but make it move faster by scaling it up (multiplying) by 1.2
        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2
