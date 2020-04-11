Тест
#####

Питање 1.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: k1
    :answer_a: Исцртава се дуж дужине 10 пиксела.
    :feedback_a: Нетачно    
    :answer_b: Исцртава се испрекидана дуж која има 5 видљивих и 5 невидљивих цртица.
    :feedback_b: Тачно
    :answer_c: Исцртава се испрекидана дуж дебљине 5 пиксела
    :feedback_c: Нетачно    
    :answer_d: Исцртава се испрекидана дуж која има 10 видљивих и 10 невидљивих цртица.
    :feedback_d: Нетачно    
    :correct: b

    Шта је резултат извршавања следеће наребе:

    .. code-block:: python

	for i in range(10):
		turtle.forward(10)
		if i % 2 == 0:
			turtle.penup()
		else:
			turtle.pendown()

Питање 2.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: k2
    :answer_a: i / 2 = 0
    :feedback_a: Нетачно    
    :answer_b: i // 2 == 0
    :feedback_b: Нетачно
    :answer_c: i % 2 == 0
    :feedback_c: Тачно    
    :answer_d: i % 2 = 0
    :feedback_d: Нетачно    
    :correct: c
    
    Шта би требало написати на месту ??? како би се исцртала звезда као на слици? Изабери тачан одговор:
	
	.. code-block:: python
	
	 for i in range(10):
	   turtle.forward(40)
	   if ????:
	      turtle.left(72) 
	   else:
	      turtle.right(144)
    
    .. image:: ../_images/zvezda.png      
       :align: center


Питање 3.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: k3
    :answer_a: Петља иза петље.
    :feedback_a: Нетачно    
    :answer_b: Две петље које се позивају у једном задатку.
    :feedback_b: Нетачно
    :answer_c: Петља унутар петље.
    :feedback_c: Тачно    
    :answer_d: Петља која се извршава паран број пута.
    :feedback_d: Нетачно    
    :correct: c
    
    Шта је угнежђена петља? Изабери тачан одговор:
	
Питање 4.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: k4
    :answer_a: У нивоу спољашње петље for, на крају, једна наредба turtle.left(90).
    :feedback_a: Тачно    
    :answer_b: У нивоу спољашње петље for једна наредба turtle.forward(90).
    :feedback_b: Нетачно    
    :answer_c: У нивоу унутрашње петље for, на крају, једна наредба turtle.left(90).
    :feedback_c: Нетачно    
    :correct: a
    
	Шта недостаје у следећем коду да би била исцртана фигур као на слици? Изабаери тачан одговор:	
		
	.. code-block:: python
	
	  for j in range(4):
		for i in range(4):
			turtle.forward(90)
			turtle.left(90)

Питање 5.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: k5
    :answer_a: Процедура за цртање правоугаоника.
    :feedback_a: Нетачно    
    :answer_b:  Процедура за цртање елипсе
    :feedback_b: нетачно    
    :answer_c:  Процедура за цртање квадрата.
    :feedback_c: Тачно    
    :correct: c
    
	Шта је дефинисано исцртавањем следећих наредби? Изабаери тачан одговор:	
		
	.. def poligon(n, a):
		for i in range(n):
			turtle.forward(a)
			turtle.right(360 / n)

Питање 6.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: k6
    :answer_a: Квадрат са ивицама које су црвено, зелене, плаве и жуте боје. 
    :feedback_a: Тачно    
    :answer_b:  Правоугаоник са ивицама које су црвено, зелене, плаве и жуте боје.
    :feedback_b: Нетачно    
    :answer_c:  Квадрат са ивицама које су црвено, жуте, плаве и зелене боје.
    :feedback_c: Нетачно    
    :correct: а
    
	Шта је резултат извршавањ следећег програма? Изабаери тачан одговор:	
		
	.. code-block:: python
	
	 boje = ("red", "green", "blue", "yellow")
	 for i in range(4):
		turtle.color(boje[i])
		turtle.forward(100)
		turtle.left(90)


