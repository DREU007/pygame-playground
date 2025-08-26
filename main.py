
from random import randrange
import pygame as pg
from settings import Resolution


COIN_SIZE = 20

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Resolution.h, Resolution.w))
        self.clock = pg.time.Clock()
        self.running = True

        self.score = 0
        self.dt = 0
        self.player = pg.Vector2(
            self.screen.get_width() / 2,
            self.screen.get_height() / 2
        )

        self.set_random_coin()

    def set_random_coin(self):

        rw = randrange(0, self.screen.get_width() - COIN_SIZE)
        rh = randrange(0, self.screen.get_height() - COIN_SIZE) 
        self.coin = pg.Rect(rw, rh, COIN_SIZE, COIN_SIZE)

    def render(self):
        pg.draw.rect(self.screen, "yellow", self.coin)
        pg.draw.circle(self.screen, "red", self.player, 10)

        keys=pg.key.get_pressed()
        if keys[pg.K_w]: self.player.y -= 300 * self.dt
        if keys[pg.K_s]: self.player.y += 300 * self.dt
        if keys[pg.K_a]: self.player.x -= 300 * self.dt
        if keys[pg.K_d]: self.player.x += 300 * self.dt

        is_collision = self.coin.collidepoint(self.player)
        if is_collision:
            self.score += 1
            self.set_random_coin()

    def main(self):

        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.screen.fill("black")
            self.render()

            pg.display.flip()
            self.dt = self.clock.tick(60) / 1000

        pg.quit()

if __name__ == "__main__":
   g = Game()
   g.main()
