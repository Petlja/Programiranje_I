31. Завршни квиз
================

Питање 1.
~~~~~~~~~

.. mchoice:: duz_16
    :answer_a: Дуж ће бити постављена хоризонтално.
    :feedback_a: Нетачно    
    :answer_b: Дуж ће бити постављена вертикално/усправно.
    :feedback_b: Нетачно
    :answer_c: Дуж ће бити искошена.
    :feedback_c: Тачно    
    :correct: c
    
    У ком положају ће бити дуж исцртана наредном командом?

    .. code-block:: python

       pygame.draw.line(prozor, pg.Color("black"), (100, 200), (200, 300), 1)

    Изабери тачан одговор:

Питање 2.
~~~~~~~~~

.. mchoice:: krugkruznica_16
    :answer_a: Круг попуњен бојом
    :feedback_a: Нетачно    
    :answer_b: Кружница - линија
    :feedback_b:  Тачно  
    :answer_c: Елипса (која није круг) попуњена бојом
    :feedback_c: Нетачно    
    :answer_d: Елипса - линија (која није кружница)
    :feedback_d: Нетачно 
    :correct: b
    
    Шта се исцртава следећом наредбом?

    .. code-block:: python
  
      pygame.draw.circle(prozor, pygame.Color("blue"), (120, 80), 40, 1)

    Изабери тачан одговор:

Питање 3.
~~~~~~~~~

.. mchoice:: ntougao_16
   :answer_a: троугао
   :feedback_a: Нетачно
   :answer_b: четвороугао
   :feedback_b: Нетачно    
   :answer_c: петоугао
   :feedback_c: Нетачно    
   :answer_d: ништа од наведеног
   :feedback_d: Тачно
   :correct: d
    
   Шта се исцртава помоћу следећих наредби?

   .. code-block:: python
  
      temena = [(40, 80), (80, 80), (80, 40), (60, 20), (40, 40), (100, 40), (30, 40)]
      pygame.draw.polygon(prozor, pygame.Color("gray"), temena)
    
   Изабери тачан одговор:

Питање 4.
~~~~~~~~~

.. mchoice:: pravougaonik_centrirano_16
   :multiple_answers:
   :answer_a: pg.draw.rect(prozor, boja, (100, 100, 100, 50))
   :feedback_a: Нетачно    
   :answer_b: pg.draw.rect(prozor, boja, (45, 80, 150, 80))
   :feedback_b: Тачно
   :answer_c: pg.draw.rect(prozor, boja, (120, 120, 100, 50))
   :feedback_c: Нетачно    
   :answer_d: pg.draw.rect(prozor, boja, (280, 280, 100, 50))
   :feedback_d: Нетачно    
   :correct: b
    
   Коју наредбу можеш употребити како би нацртао правоугаоник ширине 150 и висине 80 коме је центар у тачки (120, 120)?


   Изабери тачан одговор:

Питање 5.
~~~~~~~~~

.. mchoice:: pomeranje_duzi_16
    :answer_a: pygame.draw.line(prozor, pygame.Color("black"), (x+100, y1+50), (x, y2))
    :feedback_a: Нетачно    
    :answer_b: pygame.draw.line(prozor, pygame.Color("black"), (x+100, y1+100), (x+50, y2+50))
    :feedback_b: Нетачно    
    :answer_c: pygame.draw.line(prozor, pygame.Color("black"), (x, y1+100), (x, y2+100))
    :feedback_c: Нетачно    
    :answer_d: pygame.draw.line(prozor, pygame.Color("black"), (x+150, y1+50), (x+150, y2+50))
    :feedback_d: Тачно
    :answer_e: pygame.draw.line(prozor, pygame.Color("black"), (x, y1), (x+100, y2+50))
    :feedback_e: Нетачно    
    :correct: d
    
    Једна усправна дуж је нацртана наредбом

    .. code-block:: python

        pygame.draw.line(prozor, pygame.Color("black"), (x, y1), (x, y2))

    Којом наредбом ћемо нацртати исту такву дуж, померену 150 пиксела удесно и 50 пиксела на доле?

    Изабери тачан одговор:

Питање 6.
~~~~~~~~~

.. mchoice:: for_stepenice_16
    :answer_a: усправна испрекидана линија
    :feedback_a: Нетачно    
    :answer_b: водоравна испрекидана линија
    :feedback_b: Tачно    
    :answer_c: степенаста линија
    :feedback_c: Нетачно
    :correct: b
    
    Шта се исцртава следећим кодом?

    .. code-block:: python

        x, y = 100, 100
        for i in range(10):
            pygame.draw.line(prozor, pygame.Color("black"), (x, y), (x+10, y), 1)
            x = x+20

    Изабери тачан одговор:

Питање 7.
~~~~~~~~~

.. mchoice:: krstici2_16
    :answer_a: усправна испрекидана линија
    :feedback_a: Нетачно    
    :answer_b: водоравна испрекидана линија
    :feedback_b: Нетaчно   
    :answer_c: степенаста линија
    :feedback_c: Нетачно
    :answer_d: дијагонално поређани крстићи
    :feedback_d: Tачно
    :correct: d
    
    Шта се исцртава следећим кодом?

    .. code-block:: python

        x, y = 100, 100
        for i in range(10):
            pg.draw.line(prozor, pg.Color("black"), (x, y), (x+10, y), 1)
            pg.draw.line(prozor, pg.Color("black"), (x+5, y-5), (x+5, y+10), 1)
            x, y = x+20, y+20 

    Изабери тачан одговор:

Питање 8.
~~~~~~~~~

.. mchoice:: kvadrat_poligon_zk
   :answer_a: Ако је c-a = d-b
   :feedback_a: Тачно
   :answer_b: Дата наредба увек исцртава квадрат
   :feedback_b: Нетачно    
   :answer_c: Ако је a=b и c=d
   :feedback_c: Нетачно    
   :answer_d: Дата наредба ни под којим условима не исцртава квадрат
   :feedback_d: Нетачно    
   :correct: a
    
   Под којим условима би следећа наредба исцртала квадрат?

   .. code-block:: python
  
      pygame.draw.polygon(prozor, pygame.Color("gray"), [(a, b), (a, d), (c, d), (c, b)])

   Изабери тачан одговор:

Питање 9.
~~~~~~~~~

.. mchoice:: elipse_simetrija_zk 
   :answer_a: pg.draw.ellipse(prozor, pg.Color("gray"), (200, 100, 50, 80) )
   :feedback_a: Тачно
   :answer_b:  pg.draw.ellipse(prozor, pg.Color("gray"), (250, 100, 50, 80) )
   :feedback_b: Нетачно    
   :answer_c: pg.draw.ellipse(prozor, pg.Color("gray"), (50, 200, 50, 80) )
   :feedback_c: Нетачно  
   :answer_d: pg.draw.ellipse(prozor, pg.Color("gray"), (100, 180, 50, 80) )
   :feedback_d: Нетачно    
   :correct: a
    
   Дата линија програма исцртава једну елипсу. Ако је прозор је ширине 300 пиксела и висине 300 пиксела, која од понуђених функција ће исцртати елипсу симетричну већ нацртаној у односу на вертикалну осу симетрије прозора?

   .. code-block:: python
  
      pg.draw.ellipse(prozor, pg.Color("gray"), (50, 100, 50, 80) )

   Изабери тачан одговор:

Питање 10.
~~~~~~~~~~

.. mchoice:: blit_zk
   :answer_a: prozor.blit
   :feedback_a: Тачно
   :answer_b: pg.draw.image
   :feedback_b: Нетачно    
   :answer_c: pg.image
   :feedback_c: Нетачно
   :answer_d: prozor.image
   :feedback_d: Нетачно    
   :correct: a
    
   Коју функцију користимо да бисмо приказали слику на Пајгејм прозору?

   Изабери тачан одговор:

Питање 11.
~~~~~~~~~~

.. mchoice:: dkeydownup1zavr
   :answer_a: Плави круг ће постати и остати видљив након првог притиска на било који тастер.
   :feedback_a: Нетачно    
   :answer_b: Плави круг не може бити видљив, јер одмах по исцртавању бива прецртан црвеним кругом.
   :feedback_b: Нетачно    
   :answer_c: Плави круг ће бити видљив онолико дуго колико је тастер притиснут.
   :feedback_c: Тачно
   :correct: c

      
   Ако је реакција на догађаје дефинисана наредним кодом, шта је потребно да корисник уради да би плави круг био видљив?

   .. code-block:: python

      def obradi_dogadjaj(dogadjaj):
            if dogadjaj.type == pg.KEYDOWN:
               pg.draw.circle(prozor, pg.Color("blue"), (200, 200), 100)
            elif dogadjaj.type == pg.KEYUP:
               pg.draw.circle(prozor, pg.Color("red"), (200, 200), 100)

   Изабери тачан одговор:

Питање 12.
~~~~~~~~~~

.. mchoice:: pg_brzina_pixperseczavr
   :answer_a: 3 пиксела по секунди
   :feedback_a: Нетачно    
   :answer_b: 20 пиксела по секунди
   :feedback_b: Нетачно    
   :answer_c: 60 пиксела по секунди
   :feedback_c: Тачно
   :answer_d: не помера се
   :feedback_d: Нетачно    
   :correct: c
      
   Дат је део програма којим се анимира кретање црвеног круга

   .. code-block:: python

         def novi_frejm():
            global x
            x += 3
            prozor.fill(pg.Color("white"))
            pg.draw.circle(prozor, pg.Color("red"), (x, y), 30)
       
         pygamebg.frame_loop(20, novi_frejm)    

   Којом брзином се помера круг по екрану?

   Изабери тачан одговор:

Питање 13.
~~~~~~~~~~

.. mchoice:: pg_krug_raste2zavr
   :answer_a: На сваких 100 милисекунди круг се помера за 10 пиксела на десно.
   :feedback_a: Нетачно    
   :answer_b: Круг пролази преко екрана и у сваком проласку мења брзину.
   :feedback_b: Тачно    
   :answer_c: На сваких 100 милисекунди полупречник круга (који је на почетку 20 пиксела) се повећава за 10 пиксела.
   :feedback_c: Нетачно
   :answer_d: Ниједан од осталих понуђених одговора није тачан.  
   :feedback_d: Нетачно    
   :correct: b
      
   Шта је резултат извршавања следећег програма?

   .. code-block:: python

      import pygame as pg, pygamebg
      import random
      prozor = pygamebg.open_window(200,100, "")
      x = 0
      z = 15
      r = 30
      def novi_frejm():
            global x, z
            x += z
            prozor.fill(pg.Color("white"))
            pg.draw.circle(prozor, pg.Color("red"), (x, 50), r)
            if x - r > 200:
                  x = -r
                  z = random.randint(10, 30)
      pygamebg.frame_loop(10, novi_frejm)



Питање 14.
~~~~~~~~~~

.. mchoice:: sudari_linijazavr
   :answer_a: 1
   :feedback_a: Нетачно    
   :answer_b: 2
   :feedback_b: Нетачно    
   :answer_c: 3
   :feedback_c: Тачно
   :answer_d: 4
   :feedback_d: Нетачно    
   :correct: c
      
   Која од следећих функција проверава да ли се круг судара (додирује) са било левом, било десном ивицом екрана?

   .. code-block:: python

      (1)
      .. code-block:: python

            def sudar_sa_ivicom():
               return x_centar_kruga - poluprecnik_kruga < 0

      (2)
      .. code-block:: python

            def sudar_sa_ivicom():
               return x_centar_kruga - poluprecnik_kruga < 0 and x_centar_kruga + poluprecnik_kruga > sirina

      (3)
      .. code-block:: python

            def sudar_sa_ivicom():
               return x_centar_kruga - poluprecnik_kruga < 0 or x_centar_kruga + poluprecnik_kruga > sirina
         
      (4)
      .. code-block:: python

            def sudar_sa_ivicom():
               return x_centar_kruga + poluprecnik_kruga < 0 or x_centar_kruga - poluprecnik_kruga > sirina

   Изабери тачан одговор:

Питање 15.
~~~~~~~~~~

.. mchoice:: dkeypojedinacnolevozavr
    :answer_a: 1
    :feedback_a: Тачно
    :answer_b: 2
    :feedback_b: Нетачно    
    :answer_c: 3
    :feedback_c: Нетачно    
    :correct: a
    
    Којим од понуђених линија кода се врши провера да ли је притиснут тастер стрелице лево?

    1)
        .. code-block:: python

            if (dogadjaj.type == pygame.KEYDOWN) and (dogadjaj.key == pygame.K_LEFT):  

    2)
        .. code-block:: python

            if (dogadjaj.type == pygame.KEYDOWN) or (dogadjaj.key == pygame.LEFT):

    3)
        .. code-block:: python

            if (dogadjaj.type == pygame.K_LEFT):

    Изабери тачан одговор:
