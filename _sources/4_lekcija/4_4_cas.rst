4.4. Квиз
#########

Питање 1.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: kornjaca_1
    :answer_a: Исцртава се дуж дебљине 20 пиксела.
    :feedback_a: Нетачно    
    :answer_b: Исцртава се дуж дужине 20 пиксела.
    :feedback_b: Тачно
    :answer_c: Корњача се окреће за 20 степени налево.
    :feedback_c: Нетачно    
    :answer_d: Корњача се окреће за 20 степени надесно.
    :feedback_d: Нетачно    
    :correct: b
    
    Шта је резултат извршавања следеће наредбе?
	
	.. code-block:: python
	
	 turtle.forward(20)

Питање 2.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: kornjaca_2
    :answer_a: Исцртава се дуж дебљине 30 пиксела.
    :feedback_a: Нетачно    
    :answer_b: Исцртава се дуж дужине 30 пиксела.
    :feedback_b: Нетачно
    :answer_c: Корњача се окреће за 30 степени налево.
    :feedback_c: Тачно    
    :answer_d: Корњача се окреће за 30 степени надесно.
    :feedback_d: Нетачно    
    :correct: c
    
    Шта је резултат извршавања следеће наредбе?
	
	.. code-block:: python
	
	 turtle.left(30)


Питање 3.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: kornjaca_3
    :answer_a: Корњача оставља траг дебљине 50 пиксела.
    :feedback_a: Нетачно    
    :answer_b: Исцртава се дуж дужине 20 пиксела.
    :feedback_b: Нетачно
    :answer_c: Корњача оставља траг дебљине пет пиксела, прво црвене, затим зелене боје.
    :feedback_c: Тачно    
    :answer_d: Корњача оставља траг дебљине пет пиксела, прво зелене, затим црвене боје.
    :feedback_d: Нетачно    
    :correct: c
    
    Шта је резултат извршавања следеће наредбе?
	
	.. code-block:: python
	
	 turtle.shape("turtle")
	 turtle.width(5)
	 turtle.color("red")
	 turtle.forward(50)
	 turtle.color("green")
	 turtle.forward(50)

Питање 4.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: kornjaca_4
    :answer_a: Исцртава се квадрат.
    :feedback_a: Тачно    
    :answer_b: Исцртава се правоугаоник.
    :feedback_b: Нетачно    
    :answer_c: Исцртава се троугао.
    :feedback_c: Нетачно    
    :correct: a
    
	Шта је резултат извршавања следећег програма? Изабери тачан одговор.	
		
	.. code-block:: python
	
	  turtle.forward(100)   
	  turtle.left(90)       
	  turtle.forward(100)   
	  turtle.left(90) 
	  turtle.forward(100)   
	  turtle.left(90) 
	  turtle.forward(100)   
	  turtle.left(90) 



Питање 5.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: kornjaca_5
    :answer_a: Број 4, затим 100, затим 60.
    :feedback_a: Нетачно    
    :answer_b:  Број 100, затим 4, затим 60.
    :feedback_b: нетачно    
    :answer_c:  Број 4, затим 100, затим 90.
    :feedback_c: Тачно    
    :correct: c
    
	Шта је потребно додати на месту * како би се исцртао квадрат? Изабери тачан одговор.	
		
	.. code-block:: python
	
	  for i in range(*):
	        turtle.forward(*)
	        turtle.left(*)

Питање 6.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: kornjaca_6
    :answer_a: Шестоугао
    :feedback_a: Тачно    
    :answer_b:  Квадрат
    :feedback_b: Нетачно    
    :answer_c:  Правоугаоник
    :feedback_c: Нетачно    
    :correct: a
    
	Шта је резултат извршавања следећег програма? Изабери тачан одговор.	
		
	.. code-block:: python
	
	  for i in range(6):
	     turtle.forward(100)
	     turtle.left(60)

Питање 7.
~~~~~~~~~

.. mchoice:: kornjaca_7
    :answer_a: Седмоугао
    :feedback_a: Нетачно    
    :answer_b:  Квадрат
    :feedback_b: Нетачно    
    :answer_c:  Степенице
    :feedback_c: Tачно    
    :correct: c

    Шта је резултат извршавањa следећег програма? Изабери тачан одговор.	
		
    .. code-block:: python
	
      turtle.forward(20)
      turtle.right(90)
      turtle.forward(20)
      turtle.left(90)
      turtlе.forward(20)
      turtle.right(90)
      turtle.forward(20)
      turtle.left(90)
      turtle.forward(20)
      turtle.right(90)
      turtle.forward(20)
      turtle.left(90)
      turtle.forward(20)


Питање 8.
~~~~~~~~~

.. mchoice:: kornjaca_9
    :answer_a: 1
    :feedback_a: Нетачно    
    :answer_b:  2
    :feedback_b: Нетачно        
    :answer_c:  3
    :feedback_c: Tачно
    :correct: c

    Којом од наредних наредби се може заменити код који следи?	

    .. code-block:: python
	
      turtle.forward(40)
      turtle.left(60)
      turtle.forward(40)
      turtle.left(60)
      turtle.forward(40)
      turtle.left(60)
      turtle.forward(40)
      turtle.left(60)
      turtle.forward(40)
      turtle.left(60)
      turtle.forward(40)
      turtle.left(60)
		
    (1)

    .. code-block:: python
	
      for i in range(6):
      turtle.forward(40)
      turtle.left(60)

    (2)

    .. code-block:: python
	
      for i in range(6):
            turtle.forward(40)
      turtle.left(60)
  
    (3)

    .. code-block:: python
	
      for i in range(6):
            turtle.forward(40)
            turtle.left(60)

Питање 9.
~~~~~~~~~

.. mchoice:: kornjaca_10
    :answer_a: 1
    :feedback_a: Tачно    
    :answer_b:  2
    :feedback_b: Нетачно        
    :answer_c:  3
    :feedback_c: Нетачно
    :correct: a

    Која од наредних сличица је резултат извршавања кода који је дат?	
   
    .. code-block:: python
	
      for i in range(4):
        turtle.forward(50)
        turtle.right(90)
      turtle.right(270)

    (1)

     .. image:: ../../_images/1_strelica.png      
        :align: center
        :width: 100px
   
    (2)

     .. image:: ../../_images/2_strelica.png      
       :align: center
       :width: 100px

    (3)

     .. image:: ../../_images/3_strelica.png      
       :align: center
       :width: 100px


