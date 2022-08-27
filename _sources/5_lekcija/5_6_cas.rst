5.6. Вежбање 
#############

На крају ти остављамо неколико задатака за вежбу. Оне задатке које не
стигнеш да урадиш на часу уради за домаћи задатак.


Квадрати са заједничким доњим левим теменом
'''''''''''''''''''''''''''''''''''''''''''
       
.. questionnote::

   Напиши програм који исцртава десет квадрата који имају заједничко
   доње лево теме и чије су дужине страница у пикселима редом 10, 20, 30, 40 и
   тако даље.

.. activecode:: квадрати
   :nocodelens:
   :enablecopy:
   :playtask:

   import turtle
   for i in range(10):
       # izracunavamo dimenziju narednog kvaddrata
       a = 10*i + 10
       # crtamo kvadrat dimenzije a
       ???
   ====
   import turtle
   for i in range(10):
       # izracunavamo dimenziju narednog kvaddrata
       a = 10*i + 10
       # crtamo kvadrat
       for i in range(4):
           turtle.forward(a)
           turtle.left(90)
	   
Шарени облик
''''''''''''

.. questionnote::

   Наредни интересантан облик се добија тако што корњача црта црвену
   линију дужине 50 пиксела и затим се налево окреће за 31 степен, затим црта
   зелену линију дужине 70 и окреће се налево за 71 степен, затим црта
   плаву линију дужине 90 и окреће се налево за 101 степен, након чега
   се цртеж наставља по истом принципу. Напиши програм који анализом
   остатка при дељењу бројача са 3 унутар петље одређује шта треба да
   уради корњача.

.. activecode:: периода3
   :nocodelens:
   :enablecopy:
   :playtask:

   import turtle

   turtle.speed(0)
   turtle.width(5)
   for i in range(120):
       if i % 3 == 0:
           turtle.color("red")
           turtle.forward(50)
           turtle.left(31)
       ???
   ====
   import turtle
    
   turtle.speed(0)
   turtle.width(5)
   for i in range(120):
       if i % 3 == 0:
           turtle.color("red")
           turtle.forward(50)
           turtle.left(31)
       if i % 3 == 1:
           turtle.color("green")
           turtle.forward(70)
           turtle.left(71)
       if i % 3 == 2:
           turtle.color("blue")
           turtle.forward(90)
           turtle.left(101)

.. reveal:: периода3_ревеал
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   .. activecode:: периода3_решење
      :nocodelens:
      
      import turtle
    
      turtle.speed(0)
      turtle.width(5)
      for i in range(120):
          if i % 3 == 0:
              turtle.color("red")
              turtle.forward(50)
              turtle.left(31)
          if i % 3 == 1:
              turtle.color("green")
              turtle.forward(70)
              turtle.left(71)
          if i % 3 == 2:
              turtle.color("blue")
              turtle.forward(90)
              turtle.left(101)