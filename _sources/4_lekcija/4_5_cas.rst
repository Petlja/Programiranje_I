4.5. Вежбање 
#############

На крају ти остављамо неколико задатака за вежбу. Оне задатке које не
стигнеш да урадиш на часу уради за домаћи задатак.

Слово L
'''''''

.. questionnote::   

   Напиши програм у којем корњача исцртава велико латиничко слово L (окреће се
   ка југу, затим иде 100 корака, окреће се ка истоку и онда иде 50 корака).

.. activecode:: корњача_слово_L
   :nocodelens:
   :playtask:

   import turtle
   # dovrši program
   ====
   import turtle
   
   turtle.right(90)
   turtle.forward(100)
   turtle.left(90)
   turtle.forward(50)

Слово И
'''''''
   
.. questionnote::

   Напиши програм у којем корњача црта ћириличко слово И. Цртање креће тако
   што корњача прво иде 100 корака ка југу, затим 141 корак ка североистоку и
   затим поново 100 корака ка југу.

.. activecode:: корњача_и
   :nocodelens:
   :playtask:

   import turtle
   # dovrši program
   ====
   import turtle

   turtle.right(90)
   turtle.forward(100)
   turtle.left(135)
   turtle.forward(141)
   turtle.right(135)
   turtle.forward(100)

Плаво-црвена линија
'''''''''''''''''''

.. questionnote::

   Напиши програм у којем корњача црта плаво-црвену линију која
   састоји од 5 плавих и 5 црвених дужи дужине од по 20 пиксела које
   се наизменично смењују. Реализуј програм тако да се у телу петље
   које се понавља 5 пута црта једна плава и једна црвена дуж.

.. activecode:: корњача_црвено_плава_линија
   :nocodelens:
   :playtask:

   import turtle
   # dovrši program
   ====
   import turtle

   for i in range(5):
       turtle.color("blue")
       turtle.forward(20)
       turtle.color("red")
       turtle.forward(20)
