# -*- acsection: general-init -*-
import math
import pygame as pg
import pygamebg

(sirina, visina) = (500, 300)  # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Ауто и авион")

# -*- acsection: main -*-

avion_slika = pg.image.load("avion.png")
(avion_x, avion_y) = (0, 0)
avion_brzina = 200
auto_slika = pg.image.load("auto.png")
(auto_x, auto_y) = (0, visina - auto_slika.get_height())
auto_brzina = 100
FPS = 25
dt = 1/FPS

def crtaj():
    prozor.fill(pg.Color("white"))
    prozor.blit(avion_slika, (avion_x, avion_y))
    prozor.blit(auto_slika, (auto_x, auto_y))

def novi_frejm():
    global avion_x, avion_y, auto_x, auto_y

    # pomeramo avion
    avion_x += avion_brzina*dt
    if avion_x > sirina:
        avion_x = - avion_slika.get_width()

    # pomeramo auto
    auto_x += auto_brzina*dt
    if auto_x > sirina:
        auto_x = - auto_slika.get_width()

    # crtamo scenu
    crtaj()


# -*- acsection: after-main -*-

pygamebg.frame_loop(FPS, novi_frejm)
