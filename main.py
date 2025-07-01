
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from  asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_WIDTH))
    clock=pygame.time.Clock()
    dt=0
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    shots=pygame.sprite.Group()
    Player.containers=(updatable,drawable)
    Asteroid.containers=(asteroids,updatable,drawable)
    AsteroidField.containers=(updatable)
    Shot.containers=(updatable,drawable,shots)
    asteroid_field=AsteroidField()
    player=Player(x=SCREEN_WIDTH/2,y=SCREEN_HEIGHT/2)
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if player.get_collision(asteroid):
                print("Game over!")
                return
            
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        for asteroid in asteroids:
            for shot in shots:
                if shot.get_collision(asteroid):
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        dt=clock.tick(60)/1000
    

if __name__ == "__main__":
    main()
