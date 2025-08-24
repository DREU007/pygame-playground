import pygame as pg
from settings import Resolution

def render():
    pass

def main():
    pg.init()
    screen = pg.display.set_mode((Resolution.h, Resolution.w))
    clock = pg.time.Clock()
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill("black")

        render()

        pg.display.flip()
        clock.tick(60)

    pg.quit()

if __name__ == "__main__":
    main()
