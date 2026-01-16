import pygame as pg
import sys
import random


# Konstanter
SW, SH = 800, 600

antall_spillere = None
velg = True



# Initialiser pygame
pg.init()

BLOKK_STORELSE = 50

FONT = pg.font.Font("Pygame/Pygamehogorm/font.ttf", BLOKK_STORELSE)

skjerm = pg.display.set_mode((SW, SH))
pg.display.set_caption("Hogorm")
klokke = pg.time.Clock()

while velg:
    skjerm.fill("black")
    tittel = FONT.render("HOGORM", True, "green")
    tekst1 = FONT.render("Trykk 1 for 1 spiller", True, "white")
    tekst2 = FONT.render("Trykk 2 for 2 spillere", True, "white")

    skjerm.blit(tittel, (SW//2 - tittel.get_width()//2, SH//4))
    skjerm.blit(tekst1, (SW//2 - tekst1.get_width()//2, SH//2))
    skjerm.blit(tekst2, (SW//2 - tekst2.get_width()//2, SH//2 + 80))

    pg.display.update()
   
    for hendelse in pg.event.get():
        if hendelse.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if hendelse.type == pg.KEYDOWN:
            if hendelse.key == pg.K_1:
                antall_spillere = 1
                velg = False 
            elif hendelse.key == pg.K_2:
               antall_spillere = 2
               velg = False               

if antall_spillere == 2:
    BLOKK_STORELSE = 25

class Hogorm:
    def __init__(self, x, y, farge):
        self._x, self._y, = x, y
        self._xdir = 1   
        self._ydir = 0
        self._hode = pg.Rect(self._x, self._y, BLOKK_STORELSE, BLOKK_STORELSE)
        self._kropp = [pg.Rect(self._x-BLOKK_STORELSE, self._y, BLOKK_STORELSE, BLOKK_STORELSE)]
        self._død = False
        self._farge = farge

    def update(self):
        global apples

        for firkant in self._kropp:
            if self._hode.x == firkant.x and self._hode.y == firkant.y:
              self._død = True
            if self._hode.x not in range(0, SW) or self._hode.y not in range(0, SH):
              self._død = True
            
        
        if self._død:
            self.x, self.y = BLOKK_STORELSE, BLOKK_STORELSE
            self._hode = pg.Rect(self._x, self._y, BLOKK_STORELSE, BLOKK_STORELSE)
            self._kropp = [pg.Rect(self._x-BLOKK_STORELSE, self._y, BLOKK_STORELSE, BLOKK_STORELSE)]
            self._xdir = 1 
            self._ydir = 0 
            self._død = False
                




        self._kropp.append(self._hode)
        for i in range (len(self._kropp)-1):
          self._kropp[i].x, self._kropp[i].y = self._kropp[i + 1].x, self._kropp[i + 1].y
        self._hode.x += self._xdir * BLOKK_STORELSE
        self._hode.y += self._ydir * BLOKK_STORELSE
        self._kropp.remove(self._hode)
        
class Apple:
    def __init__(self):
        self._x = int(random.randint(0, SW)/BLOKK_STORELSE) * BLOKK_STORELSE
        self._y = int(random.randint(0, SH)/BLOKK_STORELSE) * BLOKK_STORELSE
        self.rect = pg.Rect(self._x, self._y, BLOKK_STORELSE, BLOKK_STORELSE)


    def update(self):
      pg.draw.rect(skjerm, "red", self.rect)




def tegngygrid():
  for x in range(0, SW, BLOKK_STORELSE ):
    for y in range(0, SH, BLOKK_STORELSE):
      rect = pg.Rect(x, y, BLOKK_STORELSE, BLOKK_STORELSE)
      pg.draw.rect(skjerm, "#3c3c3b", rect, 1)

score = FONT.render("1", True, "white")
score_rect = score.get_rect(center=(SW/2, SH/20))


tegngygrid()

if antall_spillere == 1:
    apples = [Apple()]
else:
    apples = [Apple(), Apple()]

hogorm1 = Hogorm(50, 50, "green")

if antall_spillere == 2:
   hogorm2 = Hogorm(50, 550, "blue")


høyeste = 0
høyeste1 = 0
høyeste2 = 0

while True:
    for hendelse in pg.event.get():
        if hendelse.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if hendelse.type == pg.KEYDOWN:
            if hendelse.key == pg.K_s:
                hogorm1._ydir = 1
                hogorm1._xdir = 0
            elif hendelse.key == pg.K_w:
                hogorm1._ydir = -1
                hogorm1._xdir = 0
            elif hendelse.key == pg.K_d:
                hogorm1._ydir = 0
                hogorm1._xdir = 1
            elif hendelse.key == pg.K_a:
                hogorm1._ydir = 0
                hogorm1._xdir = -1

            if antall_spillere == 2:
                if hendelse.key == pg.K_DOWN:
                    hogorm2._ydir = 1
                    hogorm2._xdir = 0
                elif hendelse.key == pg.K_UP:
                    hogorm2._ydir = -1
                    hogorm2._xdir = 0
                elif hendelse.key == pg.K_RIGHT:
                    hogorm2._ydir = 0
                    hogorm2._xdir = 1
                elif hendelse.key == pg.K_LEFT:
                    hogorm2._ydir = 0
                    hogorm2._xdir = -1
               
          
          


    hogorm1.update()
 

        
            


    skjerm.fill('black')
    tegngygrid()

    for apple in apples:
        apple.update()


    pg.draw.rect(skjerm, "green", hogorm1._hode)

    if antall_spillere == 2:
        hogorm2.update()

        pg.draw.rect(skjerm, "blue", hogorm2._hode)

        for firkant in hogorm2._kropp:
            pg.draw.rect(skjerm, "blue", firkant)
        
        if hogorm1._hode.colliderect(hogorm2._hode):
            hogorm1._død = True
        
        for firkant in hogorm2._kropp:
            if hogorm1._hode.colliderect(firkant):
                hogorm1._død = True
        
        if hogorm2._hode.colliderect(hogorm1._hode):
            hogorm2._død = True
        
        for firkant in hogorm1._kropp:
            if hogorm2._hode.colliderect(firkant):
                hogorm2._død = True

    for firkant in hogorm1._kropp:
       pg.draw.rect(skjerm, "green", firkant)

    if antall_spillere == 1:
        nåscore = len(hogorm1._kropp) + 1
        if nåscore >= høyeste:
            høyeste = nåscore
        
        score = FONT.render(f"Beste: {høyeste}", True, "white")
        skjerm.blit(score, (SW/2 - score.get_width()//2, 10))

    else:
        nåscore1 = len(hogorm1._kropp) + 1
        nåscore2 = len(hogorm2._kropp) + 1
        if nåscore1 >= høyeste1:
            høyeste1 = nåscore1
        
        score = FONT.render(f"Beste Grønn: {høyeste1}", True, "white")
        skjerm.blit(score, (SW/4 - score.get_width()//2, 10))

        if nåscore2 >= høyeste2:
            høyeste2 = nåscore2
        
        score2 = FONT.render(f"Beste Blå: {høyeste2}", True, "white")
        skjerm.blit(score2, (SW/1.5 - score2.get_width()//2, 10))

    for i, apple in enumerate(apples):
        if hogorm1._hode.colliderect(apple.rect):
            sist = hogorm1._kropp[-1]
            hogorm1._kropp.append(pg.Rect(sist.x, sist.y, BLOKK_STORELSE, BLOKK_STORELSE))
            apples[i] = Apple()

        if antall_spillere == 2:
            if hogorm2._hode.colliderect(apple.rect):
                sist2 = hogorm2._kropp[-1]
                hogorm2._kropp.append(pg.Rect(sist2.x, sist2.y, BLOKK_STORELSE, BLOKK_STORELSE))
                apples[i] = Apple()

    pg.display.update()
    klokke.tick(5)


