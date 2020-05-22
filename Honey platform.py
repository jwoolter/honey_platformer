import pygame
from pygame.locals import *
import os
import model


def draw(surface, data):
    surface.fill((30, 30, 30))
    # pygame.draw.rect(surface, (3,60,7), (data))


def main():
    mygame = model.Game("Rabbit Quest", 300, 300)
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.display.set_caption("Honey's adbenture")
    FPSCLOCK = pygame.time.Clock()
    PLAYERMOVEX = 2
    PLAYERMOVEY = 10
    surface = pygame.display.set_mode((300, 300))
    x = 100
    y = 100
    data = [x, y, 30, 30]
    loop = True
    while loop is True:
        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    loop = False

            elif event.type == QUIT:
                loop = False
            elif event.type == KEYDOWN:
                if event.key in [K_w, K_UP]:
                    mygame.move(0, -10)
                    mygame.update()
        keys = pygame.key.get_pressed()

        if keys[K_d] or keys[K_RIGHT]:
            mygame.move(PLAYERMOVEX, 0)

        elif keys[K_a] or keys[K_LEFT]:
            mygame.move(-1 * PLAYERMOVEX, 0)

        mygame.update()

        mygame.move(0, 0.5)
        mygame.update()

        draw(surface, data)
        mygame.blocks.draw(surface)
        mygame.sprites.draw(surface)
        pygame.display.update()

        FPSCLOCK.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
