import pygame

from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):  # constructor method run when new player() object created
        super().__init__(groups)  # possible error? we don't need self?
        self.image = pygame.image.load(join('images', 'player', 'down', '0.png')).convert_alpha()
        self.rect = self.image.get_rect(center=pos)

        # self.image and self.rect = sprite expects 2 attributes
        # .image = pygame surface, 2d pixel grid
        # .rect = rect for movement and collisions

        # movement
        self.direction = pygame.Vector2()
        self.speed = 500

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        # only works if vector has direction

    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt

    def update(self, dt):
        self.input()
        self.move(dt)
