Тест
#####

Питање 1.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: kornjaca_11
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

.. mchoice:: kornjaca_21
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

.. mchoice:: kornjaca_31
    :answer_a: Корњача оставља траг дебљине 5 пиксела.
    :feedback_a: Нетачно    
    :answer_b: Исцртава се дуж дужине 20 пиксела.
    :feedback_b: Нетачно
    :answer_c: Корњача оставља траг дебљине 5 пиксела прво црвене, затим зелене боје.
    :feedback_c: Тачно    
    :answer_d: Корњача оставља траг дебљине 5 пиксела прво зелене, затим црвене боје.
    :feedback_d: Нетачно    
    :correct: c
    
    Шта је резултат извршавања следеће наребе:
	
	.. code-block:: python
	
	 turtle.shape("turtle")
	 turtle.width(5)
	 turtle.color("red")
	 turtle.forward(50)
	 turtle.color("green")
	 turtle.forward(50)

Питање 4.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: kornjaca_41
    :answer_a: Исцртава се квадрат.
    :feedback_a: Тачно    
    :answer_b: Исцртава се правоугаоник.
    :feedback_b: Нетачно    
    :answer_c: Исцртава се троугао.
    :feedback_c: Нетачно    
    :correct: a
    
	Шта је резултат извршавања следећег програма? Изабаери тачан одговор:	
		
	.. code-block:: python
	
	  turtle.forward(100)   
	  turtle.left(90)       
	  turtle.forward(100)   
	  turtle.left(90) 

Питање 5.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: kornjaca_51
    :answer_a: Број 4, затим 100, затим 60.
    :feedback_a: Нетачно    
    :answer_b:  Број 100, затим 4, затим 60.
    :feedback_b: нетачно    
    :answer_c:  Број 4, затим 100, затим 90.
    :feedback_c: Тачно    
    :correct: c
    
	Шта је потребно додати на месту * како би се исцртао квадрат? Изабаери тачан одговор:	
		
	.. code-block:: python
	
	  for i in range(*):
	        turtle.forward(*)
	        turtle.left(*)

Питање 6.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: kornjaca_61
    :answer_a: шестоугао
    :feedback_a: Тачно    
    :answer_b:  квадрат
    :feedback_b: Нетачно    
    :answer_c:  правоугаоник
    :feedback_c: Нетачно    
    :correct: а
    
	Шта је резултат извршавањ следећег програма? Изабаери тачан одговор:	
		
	.. code-block:: python
	
	  for i in range(6):
	     turtle.forward(100)
	     turtle.left(60)


