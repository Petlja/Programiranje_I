Први час - квиз
===============

Провери своје познавање координатног система тако што ћеш одговорити на следећа питања

Питање 1.
~~~~~~~~~

.. mchoice:: tacke3
    :answer_a: (250, 220)
    :feedback_a: Нетачно    
    :answer_b: (250, 380)
    :feedback_b: Тачно
    :answer_c: (170, 300)
    :feedback_c: Нетачно    
    :answer_d: (330, 300)
    :feedback_d: Нетачно    
    :correct: b
    
    Које ће бити нове координате тачке T(250, 300) уколико се она помери за 80 пиксела на доле?

    Изабери тачан одговор:



Питање 2.
~~~~~~~~~

.. mchoice:: tacke4xy
    :answer_a: (150, 350)
    :feedback_a: Нетачно    
    :answer_b: (150, 250)
    :feedback_b: Нетачно    
    :answer_c: (200, 350)
    :feedback_c: Нетачно    
    :answer_d: (200, 250)
    :feedback_d: Тачно
    :answer_e: Ниједан од осталих понуђених одговора није тачан.
    :feedback_e: Нетачно    
    :correct: d
    
    Нека су (150, 150) и (250, 350) редом координате тачака A и B у PyGame прозору. Које су координате тачке C која представља средиште дужи AB?

    Изабери тачан одговор:


Питање 3.
~~~~~~~~~

.. mchoice:: crvena_cista
    :answer_a: (255, 0, 255)
    :feedback_a: Нетачно    
    :answer_b: (0, 0, 255)
    :feedback_b: Нетачно    
    :answer_c: (0, 255, 255)
    :feedback_c: Нетачно    
    :answer_d: (255, 255, 255)
    :feedback_d: Нетачно    
    :answer_e: (255, 0, 0)
    :feedback_e: Тачно
    :correct: e
    
    Која од наведених уређених тројки у RGB систему боја представља црвену боју?


    Изабери тачан одговор:

Питање 4.
~~~~~~~~~


.. mchoice:: svetlija
    :answer_a: слична боја, само мало тамнија
    :feedback_a: Нетачно    
    :answer_b: бела боја
    :feedback_b: Нетачно    
    :answer_c: слична боја, само мало светлија
    :feedback_c: Тачно
    :answer_d: црна боја
    :feedback_d: Нетачно    
    :answer_e: комплементарна боја
    :feedback_e: Нетачно    
    :correct: c
    
    Малим повећавањем све три вредности у уређеној тројци која представља боју, добија се 

    Изабери тачан одговор:


Питање 5.
~~~~~~~~~

.. mchoice:: dve_duzi
    :answer_a: Фигура у облику слова Г
    :feedback_a: Нетачно    
    :answer_b: Фигура у облику слова L
    :feedback_b: Нетачно    
    :answer_c: Фигура у облику слова Т
    :feedback_c: Тачно
    :answer_d: Фигура у облику знака +
    :feedback_d: Нетачно    
    :correct: c
    

    Шта се исцртава помоћу следеће две наредбе?

    .. code-block:: python

       pygame.draw.line(prozor, pygame.Color("black"), (400, 350), (500, 350), 3)
       pygame.draw.line(prozor, pygame.Color("black"), (450, 350), (450, 450), 3)



    Изабери тачан одговор:

Питање 6.
~~~~~~~~~


.. mchoice:: dijag
    :answer_a: Наредба 1
    :feedback_a: Нетачно    
    :answer_b: Наредба 2
    :feedback_b: Нетачно    
    :answer_c: Наредба 3
    :feedback_c: Тачно
    :correct: c
    
    Која од наредних наредби исцртава дијагоналу прозора димензије 150 x 150?

    1) 

    .. code-block:: python

       pygame.draw.line(prozor, pygame.Color("black"), (0, 0), (0, 150), 1)

    2)

    .. code-block:: python

       pygame.draw.line(prozor, pygame.Color("black"), (150, 0), (150, 150), 1)

    3) 

    .. code-block:: python
  
       pygame.draw.line(prozor, pygame.Color("black"), (0, 150), (150, 0), 1)


    Изабери тачан одговор:

Питање 7.
~~~~~~~~~


.. mchoice:: duz_duzina_pravac
    :answer_a: Усправну дуж дужине 500
    :feedback_a: Нетачно    
    :answer_b: Усправну дуж дужине 50
    :feedback_b: Нетачно    
    :answer_c: Водоравну дуж дужине 500
    :feedback_c: Нетачно    
    :answer_d: Водоравну дуж дужине 50
    :feedback_d: Тачно
    :correct: d
    

    Какву дуж исцртава следећа наредба?

    .. code-block:: python

       pygame.draw.line(prozor, pygame.Color("black"), (370, 500), (420, 500), 3)


    Изабери тачан одговор: