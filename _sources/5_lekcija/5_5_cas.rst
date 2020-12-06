5.5. Квиз
#########

Питање 1.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: kornjaca_kviz2_1
    :answer_a: Исцртава се испрекидана линија састављена од 10 кратких црвених и 10 дужих плавих линија
    :feedback_a: Нетачно    
    :answer_b: Исцртава се испрекидана линија састављена од 5 кратких црвених и 5 дужих плавих линија
    :feedback_b: Тачно
    :answer_c: Исцртава се испрекидана линија састављена од 10 кратких плавих и 10 дужих црвених линија
    :feedback_c: Нетачно    
    :answer_d: Исцртава се испрекидана линија састављена од 5 кратких плавих и 5 дужих црвених линија
    :feedback_d: Нетачно    
    :correct: b
    
    Шта је резултат извршавања следеће наредбе:
        
        .. code-block:: python
        
         import turtle
         for i in range(10):
             if i % 2 == 0:
                 turtle.color("red")
                 turtle.forward(10)
             else:
                 turtle.color("blue")
                 turtle.forward(20)
                 
Питање 2.
~~~~~~~~~

.. mchoice:: kornjaca_kviz2_2
    :answer_a: Цртају се три квадрата распоређена тако да је сваки наредни окренут 120 степени у односу на претходни
    :feedback_a: Нетачно
    :answer_b: Цртају се четири квадрата распоређена тако да је сваки наредни окренут 90 степени у односу на претходни
    :feedback_b: Нетачно
    :answer_c: Цртају се четири једнакостранична троугла распоређена тако да је сваки наредни окренут 90 степени у односу на претходни
    :feedback_c: Тачно    
    :answer_d: Цртају се четири правоугла троугла распоређена тако да је сваки наредни окренут 90 степени у односу на претходни
    :feedback_d: Нетачно    
    :correct: c
    
    Шта је резултат извршавања следећег програма:
        
        .. code-block:: python

         import turtle
         for i in range(4):
             for j in range(3):
                 turtle.forward(100)
                 turtle.left(120)
             turtle.right(90)

Питање 3.
~~~~~~~~~

.. mchoice:: kornjaca_kviz2_3
    :answer_a: boje = ("red", "green", "blue")
    :feedback_a: Тачно
    :answer_b: boje = ("crvena", "zelena", "plava")
    :feedback_b: Нетачно
    :answer_c: turtle.color("red", "green", "blue")
    :feedback_c: Нетачно
    :answer_d: turtle.forward(100)
    :feedback_d: Нетачно    
    :answer_e: turtle.left(120)
    :feedback_e: Нетачно    
    :correct: a
    
    Како је потребно допунити наредни програм да би се цртао једнакостранични троугао чије су странице
    обојене редом у црвену, зелену и плаву боју?
        
        .. code-block:: python

         import turtle
	 # ovde upisi potrebnu naredbu
         for i in range(3):
	     turtle.color(boje[i])
	     turtle.forward(100)
	     turtle.left(120)
             
Питање 4.
~~~~~~~~~


.. mchoice:: kornjaca_kviz2_4
    :answer_a: for
    :feedback_a: Нетачно
    :answer_b: while
    :feedback_b: Нетачно
    :answer_c: def
    :feedback_c: Тачно
    :answer_d: if
    :feedback_d: Нетачно    
    :answer_e: else
    :feedback_e: Нетачно    
    :correct: c
    
    Која се кључна реч користи за дефинисање нових наредби које корњача може да изврши?
