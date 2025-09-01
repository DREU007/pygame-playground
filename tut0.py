import pygame as pg


pg.init()
screen = pg.display.set_mode((320,240))
# clock = pg.clock(60)

countdown = 60
while countdown: 
    pg.font.Font.render(str(countdown))
    countdown -= 1
