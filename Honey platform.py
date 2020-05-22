import pygame
from pygame.locals import *
import os
import model


def draw(surface, data):
    surface.fill((30, 30, 30))
    # pygame.draw.rect(surface, (3,60,7), (data))


def main():
    width = 300
    height = 300

    mygame = model.Game("Rabbit Quest", width, height)
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.display.set_caption("Honey's adbenture")
    FPSCLOCK = pygame.time.Clock()

    PLAYERMOVEX = 2
    PLAYERMOVEY = 10

    surface = pygame.display.set_mode((width, height))
    x = 100
    y = 100
    data = [x, y, 30, 30]

    loop = True

    while loop is True:

        dx = dy = 0

        for event in pygame.event.get():

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    loop = False

            elif event.type == QUIT:
                loop = False

            elif event.type == KEYDOWN:
                if event.key in [K_w, K_UP]:
                    dy = -10

        keys = pygame.key.get_pressed()

        if keys[K_d] or keys[K_RIGHT]:
            dx = PLAYERMOVEX

        elif keys[K_a] or keys[K_LEFT]:
            dx = 0 - PLAYERMOVEX

        mygame.move(dx,dy)
        mygame.update()

        surface.fill((30, 30, 30))
        mygame.blocks.draw(surface)
        mygame.sprites.draw(surface)
        pygame.display.update()

        FPSCLOCK.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
