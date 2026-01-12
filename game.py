import pygame as pg
import sys
import random


# Konstanter
SW, SH = 800, 800





# Initialiser pygame
pg.init()

BLOKK_STORELSE = 50

skjerm = pg.display.set_mode((SW, SH))
pg.display.set_caption("Hogorm")
klokke = pg.time.Clock()


class Hogorm:
    def __init__(self):
        self._x, self._y, = BLOKK_STORELSE,  BLOKK_STORELSE
        self._xdir = 1   
        self._ydir = 0
        self._hode = pg.Rect(self._x, self._y, BLOKK_STORELSE, BLOKK_STORELSE)
        self._kropp = [pg.Rect(self._x-BLOKK_STORELSE, self._y, BLOKK_STORELSE, BLOKK_STORELSE)]
        self._død = False

    def update(self):
        self._kropp.append(self._hode)
        for i in range (len(self._kropp)-1):
          self._kropp[i].x, self._kropp[i].y = self._kropp[i + 1].x, self._kropp[i + 1].y
        self._hode.x += self._xdir * BLOKK_STORELSE
        self._hode.y += self._ydir * BLOKK_STORELSE
        self._kropp.remove(self._hode)
        



def tegngygrid():
  for x in range(0, SW, BLOKK_STORELSE ):
    for y in range(0, SH, BLOKK_STORELSE):
      rect = pg.Rect(x, y, BLOKK_STORELSE, BLOKK_STORELSE)
      pg.draw.rect(skjerm, "#3c3c3b", rect, 1)



tegngygrid()
        
hogorm = Hogorm()

while True:
  for hendelse in pg.event.get():
    if hendelse.type == pg.QUIT:
      pg.quit()
      sys.exit()
    
    if hendelse.type == pg.KEYDOWN:
        if hendelse.key == pg.K_DOWN:
          hogorm._ydir = 1
          hogorm._xdir = 0
        elif hendelse.key == pg.K_UP:
          hogorm._ydir = -1
          hogorm._xdir = 0
        elif hendelse.key == pg.K_RIGHT:
          hogorm._ydir = 0
          hogorm._xdir = 1
        elif hendelse.key == pg.K_LEFT:
          hogorm._ydir = 0
          hogorm._xdir = -1
          
          


    hogorm.update()

    skjerm.fill('black')
    tegngygrid()
    

    pg.draw.rect(skjerm, "green", hogorm._hode)

    for firkant in hogorm._kropp:
       pg.draw.rect(skjerm, "green", firkant)
  
  pg.display.update()
  klokke.tick(10)


