from settings import *
from Player import Player
from sprites import *

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
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        # Sprites
        self.player = Player((400, 300), self.all_sprites, self.collision_sprites) #the player is not in both groups, but has access to them
        for i in range(6):
            x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
            w, h = randint(60, 100), randint(50, 100)
            CollisionSprite((x, y), (w, h), (self.all_sprites, self.collision_sprites))
            # Creates frect at random x,y coordinates with random w,h within set w,h limits

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
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__': # makes sure that only main.py will be run
    game = Game()
    game.run()

