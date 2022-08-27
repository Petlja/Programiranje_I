5.2. Угнежђене петље
####################

У сложенијим задацима често је потребно да се облици који се исцртавају
коришћењем петљи (какве смо исцртавали у претходним лекцијама)
понављају неколико пута, чиме се добијају сложенији облици. Тако се
добијају програми који садрже петље у чијем телу се налазе друге
петље. Такве петље називају се **угнежђене петље**. Урадимо неколико
примера овог облика.

Три квадрата
''''''''''''
	   
.. questionnote::

   Напиши програм којим корњача исцртава мало сложенији облик који се
   састоји од три квадрата, окренутих за по 120 степени један у односу
   на други (као што се види приликом покретања програма).

.. activecode:: полигони_угнежђена_петља
   :nocodelens:
   :enablecopy:

   import turtle

   for i in range(3):       # ponavljamo tri puta za crtanje tri kvadrata
       for j in range(4):     # crtamo četiri stranice jednog kvadrata      
           turtle.forward(50)   
	   turtle.right(90)         
       turtle.right(120)    # posle crtanja jednog kvadrata okrećemo se za 120 stepeni 

По сличном принципу можемо нацртати и наизглед доста сложеније облике.

Компликованија звезда
'''''''''''''''''''''

.. questionnote::

   Напиши програм у којем корњача црта звездицу приказану на слици.
   Она се састоји од 20 троуглова чија је страница дугачка 60 корака,
   који су распоређени око правилног двадесетоугла чија је дужина
   странице 10 корака.

   .. image:: ../../_images/kornjaca-komplikovana-zvezda.png
      :align: center
	      
Исправи наредни програм тако да се добије облик са слике.
	      
.. activecode:: полигони_угнежђена_петља_1
   :nocodelens:
   :enablecopy:
   :playtask:

   import turtle
   m = 20
   n = 3
   turtle.speed(0)
   for i in range(0):
       turtle.color("red")
       for j in range(0):
           turtle.forward(0)
           turtle.left(0)
       turtle.color("black")
       turtle.forward(0)
       turtle.left(0)
   ====
   import turtle
   m = 20
   n = 3
   turtle.speed(0)
   for i in range(m):
       turtle.color("red")
       for j in range(n):
           turtle.forward(60)
	   turtle.left(360/n)
       turtle.color("black")
       turtle.forward(10)
       turtle.left(360/m)
         
