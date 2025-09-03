
from random import randrange
from collections import deque
import pygame as pg
from settings import Resolution


COIN_SIZE = 32 
STEP = 32 

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Resolution.h, Resolution.w))
        self.clock = pg.time.Clock()
        self.running = True

        self.score = 0
        self.dt = 0
        self.player = pg.Vector2(16, 16)
        self.selected = None
        self.is_selected = False
        self.set_random_coin()

    def set_random_coin(self):

        rw = randrange(0, self.screen.get_width() - COIN_SIZE)
        rh = randrange(0, self.screen.get_height() - COIN_SIZE) 
        self.coin = pg.Rect(rw, rh, COIN_SIZE, COIN_SIZE)

    def select(self):
        self.is_selected = not self.is_selected
        x = self.player.x // STEP * STEP
        y = self.player.y // STEP * STEP
        self.selected = pg.Rect(x, y, STEP, STEP)


    @staticmethod
    def object_move(obj, attr, step, direction):
        new_value = getattr(obj, attr) + step * direction
        setattr(obj, attr, new_value)

    def player_move(self, move_x, move_y, step=STEP):
        self.player.x += move_x * step
        self.player.y += move_y * step

    def render(self):
        pg.draw.rect(self.screen, "yellow", self.coin)
        if self.is_selected:
            pg.draw.rect(self.screen, "grey", self.selected)
        pg.draw.circle(self.screen, "red", self.player, 16)
        

        move_x = 0
        move_y = 0
        keys=pg.key.get_just_pressed()
        if keys[pg.K_w]: move_y = -1
        if keys[pg.K_s]: move_y = 1
        if keys[pg.K_a]: move_x = -1
        if keys[pg.K_d]: move_x = 1
        if keys[pg.K_SPACE]: self.select() 
        self.player_move(move_x, move_y)

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
