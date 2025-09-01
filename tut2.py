import sys
import pygame as pg


def main():
    pg.init()

    size = width, height = 1280, 800 
    speed = [1, 1]
    black = 0, 0, 0

    screen = pg.display.set_mode(size)
    ball = pg.image.load("intro_ball.webp")
    ballrect = ball.get_rect()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()

        ballrect = ballrect.move(speed)

        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
            speed = [speed[0] * 2, speed[1] * 2]

        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
            speed = [speed[0] * 2, speed[1] * 2]

        screen.fill(black)
        screen.blit(ball, ballrect)
        pg.display.flip()


if __name__ == '__main__':
    main()
