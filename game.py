import pygame as pg
import sys


# Konstanter
BREDDE, HØYDE = 800, 600
RADER, KOLONNER = 20, 20
CELLESTØRRELSE = BREDDE // KOLONNER
PALETT_HØYDE = 50

# Farger
HVIT = (255, 255, 255)
SVART = (0, 0, 0)
GRÅ = (200, 200, 200)

# Initialiser pygame
pg.init()

skjerm = pg.display.set_mode((BREDDE, HØYDE))
pg.display.set_caption("Hogorm")

# Lager en todimensjonal liste som representerer brettet, 
# der hver rute har fargen hvit
brett = [[HVIT for k in range(KOLONNER)] for r in range(RADER)]

def tegnBrett():
  for rad in range(RADER):
    for kol in range(KOLONNER):
      pg.draw.rect(skjerm, brett[rad][kol], (kol * CELLESTØRRELSE, rad * CELLESTØRRELSE, CELLESTØRRELSE, CELLESTØRRELSE))
      pg.draw.rect(skjerm, GRÅ, (kol * CELLESTØRRELSE, rad * CELLESTØRRELSE, CELLESTØRRELSE, CELLESTØRRELSE), 1)



        

while True:
  for hendelse in pg.event.get():
    if hendelse.type == pg.QUIT:
      pg.quit()
      sys.exit()



  skjerm.fill(HVIT)
  tegnBrett()
  pg.display.flip()

