import pygame as pg
from settings import Resolution

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Resolution.h, Resolution.w))
        self.clock = pg.time.Clock()
        self.running = True


        self.dt = 0
        self.player = pg.Vector2(
            self.screen.get_width() / 2,
            self.screen.get_height() / 2
        )

    def render(self):
        pg.draw.circle(self.screen, "red", self.player, 40)

        keys=pg.key.get_pressed()
        if keys[pg.K_w]: self.player.y -= 300 * self.dt
        if keys[pg.K_s]: self.player.y += 300 * self.dt
        if keys[pg.K_a]: self.player.x -= 300 * self.dt
        if keys[pg.K_d]: self.player.x += 300 * self.dt


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
