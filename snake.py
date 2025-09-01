
from random import randrange
from collections import deque
import pygame as pg
from settings import Resolution


COIN_SIZE = 20
STEP = 300

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Resolution.h, Resolution.w))
        self.clock = pg.time.Clock()
        self.running = True

        self.score = 0
        self.dt = 0
        self.player = deque()
        self.player.append(
            pg.Vector2(
                self.screen.get_width() / 2,
                self.screen.get_height() / 2
            )
        )
        self.set_random_coin()

    def set_random_coin(self):

        rw = randrange(0, self.screen.get_width() - COIN_SIZE)
        rh = randrange(0, self.screen.get_height() - COIN_SIZE) 
        self.coin = pg.Rect(rw, rh, COIN_SIZE, COIN_SIZE)

    def draw_player(self):
        for element in self.player:
            pg.draw.circle(self.screen, "red", element, 10)


    @staticmethod
    def object_move(obj, attr, step, direction):
        new_value = getattr(obj, attr) + step * direction
        setattr(obj, attr, new_value)

    def player_move(self, head_x, head_y, step=300):
        head = self.player[0]
        new_head_x = head.x + head_x * step * self.dt
        new_head_y = head.y + head_y * step * self.dt
        self.player.appendleft(pg.Vector2(new_head_x, new_head_y))

    def render(self):
        pg.draw.rect(self.screen, "yellow", self.coin)
        self.draw_player()

        head_x, head_y = 0, 0 
        move = False

        keys=pg.key.get_pressed()
        if keys[pg.K_w]: move = True; head_y = -1 
        if keys[pg.K_s]: move = True; head_y = 1 
        if keys[pg.K_a]: move = True; head_x = -1
        if keys[pg.K_d]: move = True; head_x = 1

        if move:
            self.player_move(head_x, head_y)

            is_collision = self.coin.collidepoint(self.player[0])
            if is_collision:
                self.score += 1
                self.set_random_coin()
            else:
                self.player.pop()

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
