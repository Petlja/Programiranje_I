# -*- acsection: general-init -*-
import pygame as pg
import pygamebg

(sirina, visina) = (150, 180)  # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Цртани филм")

sredina_y = visina / 2

# -*- acsection: main -*-

# učitavamo u listu slike setanje1.png, setanje2.png, ..., setanje5.png
slike = []   # niz u koji dodajemo slike
for i in range(1, 6):
    naziv_slike = "setanje" + str(i) + ".png"  # gradimo naziv slike od delova
    slike.append(pg.image.load(naziv_slike))   # učitavamo sliku i dodajemo je na kraj niza

slika = 0  # indeks tekuće slike

def crtaj():
    prozor.fill(pg.Color("white"))     # bojimo pozadinu prozora u belo
    prozor.blit(slike[slika], (0, 0))  # prikazujemo sliku

def novi_frejm():
    global slika  # ovu globalnu promenljivu menjamo
    slika = (slika + 1) % len(slike)  # prelazimo na sledeću sliku
    crtaj() # ponovo crtamo scenu

# -*- acsection: after-main -*-

# animacija poziva funkciju novi frejm 5 puta u sekundi
pygamebg.frame_loop(1, novi_frejm)
