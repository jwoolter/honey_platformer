import pygame
import random
from pygame.locals import *

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)

class Wall (pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("rabbit.png")
        self.rect = self.image.get_rect()


class Game():

    def __init__(self, name, height, width):

        self.name = name
        self.height = height
        self.width = width
        self.rect = pygame.Rect(0, 0, width, height)
        self.dx = 0
        self.dy = 0
        self.gravity = 1
        self.sprites = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.add_blocks()
        self.player = MySprite()
        self.player.rect.center = self.rect.center
        self.sprites.add(self.player)
        """for i in range (10):
            newsprite = MySprite()
            newsprite.rect.x = random.randint(0, self.width)
            newsprite.rect.y = random.randint(0, self.height)
            self.sprites.add(newsprite)"""

    def add_blocks(self):

        newWall = Wall (50,50, 50, 50)
        self.blocks.add (newWall)
        newWall = Wall (20,20, 50, 50)
        self.blocks.add (newWall)
        newWall = Wall (150,190, 50, 50)
        self.blocks.add (newWall)

    def move(self, dx,dy):

        self.dx = dx
        self.dy = dy

    def update(self):

        self.gravity_calc()

        self.player.rect.x += self.dx

        block_hit_list = pygame.sprite.spritecollide(self.player, self.blocks, False)
        for block in block_hit_list:
            print("hit something")

            if self.dx > 0:
                self.player.rect.right = block.rect.left
            elif self.dx <0:
                self.player.rect.left = block.rect.right

            self.dx = 0

        self.player.rect.y += self.dy
        block_hit_list = pygame.sprite.spritecollide(self.player, self.blocks, False)

        for block in block_hit_list:
            print("hit something")

            if self.dy > 0:
                self.player.rect.bottom = block.rect.top
            elif self.dy<0:
                self.player.rect.top = block.rect.bottom

            self.dy = 0


    def gravity_calc(self):

        if self.dy == 0:
            self.dy = 1
        else:
            self.dy += self.gravity


        # See if we are on the ground.
        if self.player.rect.bottom >= self.rect.bottom:
            #self.dy = 0
            self.player.rect.bottom = self.rect.bottom