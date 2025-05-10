from settings import *
from Player import Player

class Game:
    def __init__(self): # The constructor method. This runs once when you create a new Game() object.
        pygame.init() # initializes imported pygame modules
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # canvas, main surface
        pygame.display.set_caption('Vampire Clone')
        self.clock = pygame.time.Clock() # for frame rate
        self.running = True

        #groups
        self.all_sprites = pygame.sprite.Group

        self.player = Player((400,300), self.all_sprites)

    def run(self):
        while self.running: # while self.running = True game loop keeps running
            # dt
            dt = self.clock.tick() / 1000 # animation will be frame rate independent, based on delta between 2 frames

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False


            # update game

            # draw game
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__': # makes sure that only main.py will be run
    game = Game()
    game.run()

