import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Groups: Containers that holds and manages multiple game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Containers
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,) # Only updatable as it's not drawable, and it's not an asteroid itself

    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()  # Clock object
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Instantiate a Player object. 
                                                         # You can pass these values to the constructor to spawn it in the middle of the screen:
    # Main Game Loop
    while True:  # Infinite While loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for asteroid in asteroids: # Iterate over all of the objects in asteroids group
            if player.collides_with(asteroid): # Checks for collisions
                print("Game over!")
                pygame.quit()
                sys.exit()

        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collides_with(asteroid):
                    bullet.kill()
                    asteroid.split()

        screen.fill("black")  # Fills screen with black
        for sprite in drawable:
            sprite.draw(screen)  # Re-renders the sprite on screen each frame, done after filling the screen with black but before flipping the screen

        pygame.display.flip()  #  This refreshes the, must be called last
        dt = clock.tick(60) / 1000   # The .tick() method also returns the amount of time that has passed since the last time it was called: the delta time. 
                                     # Divide the return value by 1000 (to convert from milliseconds to seconds)

    


if __name__ == "__main__":
    main()
