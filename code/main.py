import pygame

from settings import *
from Player import Player
from sprites import *
from pytmx.util_pygame import load_pygame
from groups import AllSprites

from random import randint
class Game:
    def __init__(self): # The constructor method. This runs once when you create a new Game() object.
        # Setup
        pygame.init() # initializes imported pygame modules
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # canvas, main surface
        pygame.display.set_caption('Vampire Clone')
        self.clock = pygame.time.Clock() # for frame rate
        self.running = True

        # Groups
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()

        # Sprites
        self.player = Player((500, 300), self.all_sprites, self.collision_sprites) #the player is not in both groups, but has access to them

    def setup(self):
        map = load_pygame(join('data', 'maps', 'world.tmx'))

        for x,y, image in map.get_layer_by_name('Ground').tiles():
            Sprite((x * TILE_SIZE,y * TILE_SIZE), image, self.all_sprites)
        for obj in map.get_layer_by_name('Objects'):
            CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

        for obj in map.get_layer_by_name('Collisions'): #collision layer from tiled, invicible
            CollisionSprite((obj.x, obj.y), pygame.Surface((obj.width, obj. height)), self.collision_sprites)


    def run(self):
        while self.running: # while self.running = True, game loop keeps running
            # dt
            dt = self.clock.tick(60) / 1000 # animation will be frame rate independent, based on delta between 2 frames

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            # update
            self.all_sprites.update(dt)
            # calls update method from player, update has .input and .move
            # which take in input and apply movement code from .move

            # draw game
            self.display_surface.fill('black')
            self.all_sprites.draw()
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__': # makes sure that only main.py will be run
    game = Game()
    game.run()

