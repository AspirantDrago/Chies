import pygame as pg

a = WEDTH, HEIGHT = 600, 600

negr = pg.display.set_mode(a)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
lox= (238, 232, 170)
xz = (160, 82, 45)

fps = 60

siz = 75

clock = pg.time.Clock()

board = pg.Surface((600, 600))

for i in range(8):
    for y in range(8):
        if (i + y) % 2 == 0:
            pg.draw.rect(board, lox, [siz * i, siz * y, siz, siz])
        else:
            pg.draw.rect(board, xz, [siz * i, siz * y, siz, siz])


while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            quit()

    negr.blit(board, (0, 0))

    pg.display.flip()
    clock.tick(fps)


