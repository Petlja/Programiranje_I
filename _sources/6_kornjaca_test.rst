Тест
#####

Питање 1.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: 1
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

.. mchoice:: 2
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

.. mchoice:: 3
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

.. mchoice:: 4
    :answer_a: random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    :feedback_a: Тачно    
    :answer_b: random.randint(0, 255), (0, 255), (0, 255)
    :feedback_b: Нетачно    
    :answer_c: random.randint(0, 255)
    :feedback_c: Нетачно    
    :correct: a
    
	Шта недостаје у следећем коду да би била исцртана фигур као на слици? Изабаери тачан одговор:	
		
	.. code-block:: python
	
	 turtle.speed(10)
	 n = 8
	 for i in range(0, 100):
         turtle.color(???)
         turtle.forward(i)
         turtle.left(360 / n)
		
    
    .. image:: ../_images/kvadratnaSpirala.png      
       :align: center

Питање 5.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: 5
    :answer_a: Квадрат
    :feedback_a: Нетачно    
    :answer_b:  Слово Н
    :feedback_b: нетачно    
    :answer_c:  Слово N
    :feedback_c: Тачно    
    :correct: c
    
	Шта је резултат извршавања следећих наредби? Изабаери тачан одговор:	
		
	.. code-block:: python
	
	 turtle.left(90)
	 turtle.forward(100)
	 turtle.right(135)
	 turtle.forward(141)
	 turtle.left(135)
	 turtle.forward(100)

Питање 6.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: 6
    :answer_a: Квадрат са ивицама које су црвено, зелене, плаве и жуте боје. 
    :feedback_a: Тачно    
    :answer_b:  Правоугаоник са ивицама које су црвено, зелене, плаве и жуте боје.
    :feedback_b: Нетачно    
    :answer_c:  Квадрат са ивицама које су црвено, жуте, плаве и зелене боје.
    :feedback_c: Нетачно    
    :correct: а
    
	Шта је резултат извршавања следећег програма? Изабаери тачан одговор:	
		
	.. code-block:: python
	
	 boje = ("red", "green", "blue", "yellow")
	 for i in range(4):
		turtle.color(boje[i])
		turtle.forward(100)
		turtle.left(90)

Питање 7.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: 7
    :answer_a: 1
    :feedback_a: Тачно    
    :answer_b:  2
    :feedback_b: Нетачно    
    :answer_c:  3
    :feedback_c: Нетачно    
    :correct: a

	(1)
	
	.. code-block:: python
	
	 for i in range(8):
         	turtle.forward(60)
         	turtle.right(135)

	(2)
	
	.. code-block:: python
	
	 for i in range(8):
         	turtle.forward(135)
         	turtle.right(60)

	(3)
	
	.. code-block:: python
	
	 for i in range(9):
         	turtle.forward(135)
         	turtle.right(60)

	Који од понуђених кодва исцртава звезду као на слици? Изабаери тачан одговор:	
	
    .. image:: ../_images/zvezda2.png      
       :align: center

Питање 8.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: 8
    :answer_a: Три правоугаоника црвене, зелене и плаве боје.
    :feedback_a: Нетачно    
    :answer_b:  Три ромба црвене, зелене и плаве боје.
    :feedback_b: Нетачно    
    :answer_c:  Три квадрата црвене, зелене и плаве боје.
    :feedback_c: Тачно    
    :correct: а
    
	Шта је резултат извршавања следећег програма? Изабаери тачан одговор:	
		
	.. code-block:: python
	
	 boje = ("red", "green", "blue")
	 for i in range(3):
         	turtle.color(boje[i])
    		for j in range(4):
                	turtle.forward(50)
                	turtle.right(90)
    		turtle.right(120)

Питање 9.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: 9
    :answer_a: Исцрта се "пахуљица" са осам латица.
    :feedback_a: Нетачно    
    :answer_b:  Исцрта се "пахуљица" са осам латица које се међусобно налазе под углом од 135 степени.
    :feedback_b: Нетачно    
    :answer_c:  Исцрта се "пахуљица" са осам латица које се међусобно налазе под углом од 45 степени.
    :feedback_c: Тачно    
    :correct: c
    
	Шта је резултат извршавања следећег програма? Изабаери тачан одговор:	
		
	.. code-block:: python
	
	 for i in range(8):
         	turtle.forward(50)
         	turtle.backward(50)
         	turtle.left(45)

Питање 10.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: 10
    :answer_a: Лукови
    :feedback_a: Нетачно    
    :answer_b:  Степенице
    :feedback_b: Нетачно    
    :answer_c:  Врх тврђаве
    :feedback_c: Тачно    
    :correct: а
    
	Шта је резултат извршавања следећег програма? Изабаери тачан одговор:	
		
	.. code-block:: python
	
	 dim = 20
	 for i in range(5):
		turtle.forward(dim)
     		turtle.left(90)
     		turtle.forward(dim)
     		turtle.right(90)
     		turtle.forward(dim)
     		turtle.right(90)
     		turtle.forward(dim)
     		turtle.left(90)









