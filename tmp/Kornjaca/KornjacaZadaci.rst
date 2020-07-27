Корњача графика - Додатни задаци за вежбу
#########################################

Задаци
------

Слово N латиницом
'''''''''''''''''
   
.. questionnote::

   Напиши програм у којем корњача црта латиничко слово N. Цртање креће тако
   што корњача прво иде 100 корака ка северу, затим 141 корак ка југоистоку и
   затим поново 100 корака ка северу.

.. activecode:: корњача_N
   :nocodelens:
   :playtask:

   import turtle
   # dovrši program
   ====
   import turtle

   turtle.left(90)
   turtle.forward(100)
   turtle.right(135)
   turtle.forward(141)
   turtle.left(135)
   turtle.forward(100)
   

Квадратна спирала
'''''''''''''''''
      
.. questionnote::

   Напиши програм који исцртава квадратну спиралу. Свака наредна
   линија је 5 корака дужа од претходне и са њом гради прав угао.
   
.. activecode:: корњача_квадратна_спирала
   :nocodelens:
   :playtask:

   import turtle, random
   # dovrši program
   ====
   import turtle, random
   turtle.speed(10)
   for i in range(0, 200, 5):
       turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
       turtle.forward(i)
       turtle.left(90)

N-тоугаона спирала
''''''''''''''''''
       
.. questionnote::

   Прилагоди претходни програм тако да се црта произвољан
   :math:`n`-тоугао.
   
.. activecode:: корњача_спирала
   :nocodelens:
   :playtask:

   import turtle, random
   turtle.speed(10)
   n = 8
   # dovrši program
   ====
   import turtle, random
   turtle.speed(10)
   n = 8
   for i in range(0, 100):
       turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
       turtle.forward(i)
       turtle.left(360 / n)

Осмокраке звезде у теменима осмоугла
''''''''''''''''''''''''''''''''''''

.. questionnote::

   Осмокрака звезда се може нацртати тако што корњача нацрта 8 дужи,
   при чему се након сваке окреће надесно за 135 степени. Дефиниши
   процедуру за цртање такве звезде, при чему је дужина дужи параметар
   те процедуре. Употреби ту процедуру да корњача нацрта 8 таквих
   звезда у теменима правилног осмоугла. Дужина дужи којом се цртају
   звезде треба да буде једнака половини дужине осмоугла.

.. activecode:: корњача88
   :nocodelens:
   :enablecopy:
   :playtask:

   import turtle

   def zvezda8(a):
       ???

   n = 8
   a = 60
   for i in range(n):
       ???
   
   ====
   import turtle
    
   def zvezda8(a):
       for i in range(8):
           turtle.forward(a)
           turtle.right(135)

   turtle.speed(0)
   n = 8
   a = 60
   for i in range(n):
       zvezda8(a/2)
       turtle.forward(a)
       turtle.left(360/n)
   
.. questionnote::

   Издвој главни део претходног програма у посебну процедуру која
   прима број страна n-тоугла и дужину једне стране, а затим употреби
   ту функцију тако да се нацртају квадрат, петоугао и шестоугао који
   у теменима имају осмокраке звезде, распоређени у темена
   једнакостраничног троугла.


.. activecode:: корњача8345
   :nocodelens:
   :enablecopy:
   :playtask:
   
   import turtle

   def zvezda8(a):
       ???


   def zvezdani_mnogougao(n, a):
       ???

   turtle.speed(0)        
   for i in range(3):
       zvezdani_mnogougao(i+4, 50)
       turtle.forward(150)
       turtle.left(120)
   ====
   import turtle

   def zvezda8(a):
       for i in range(8):
           turtle.forward(a)
           turtle.right(135)

   def zvezdani_mnogougao(n, a):
       for i in range(n):
           zvezda8(a/2)
           turtle.forward(a)
           turtle.left(360/n)

   turtle.speed(0)        
   for i in range(3):
       zvezdani_mnogougao(i+4, 40)
       turtle.forward(150)
       turtle.left(120)
   

Линија од дужи у три боје, три дужине
'''''''''''''''''''''''''''''''''''''

.. questionnote::

   Напиши програм којим корњача црта линију која се састоји од црвених
   делова дужине 15 пиксела, зелених делова дужине 10 пиксела и плавих
   делова дужине 20 пиксела, који се смењују у круг.
      
.. activecode:: корњача_боје_и_дужине_у_круг
   :nocodelens:
   :playtask:

   import turtle
   turtle.width(5)
   
   linije = (('red', 15), ('green', 10), ('blue', 20))
   # dovrši program
   ====
   import turtle

   turtle.width(5)
   linije = (('red', 15), ('green', 10), ('blue', 20))
   for i in range(20):
       (boja, duzina) = linije[i % len(linije)]
       turtle.color(boja)
       turtle.forward(duzina)

       
n-токрака звезда без пресецања
''''''''''''''''''''''''''''''
           
Покушај да уопштиш неки програм који је цртао петокраку звезду без
пресецања тако да црта звезду са :math:`n` кракова. Помоћ: звезда се
састоји од централног правилног :math:`n`-тоугла, чије су странице
продужене тако да формирају једнакокраке троуглове који чине
краке. Дакле, углови на основици звездиних кракова су спољашњи углови
правилног многоугла и могу се лако израчунати (ти углови одговарају
првом окрету корњаче). У другом окрету корњача се окреће за суплемент
(допуну до 180 степени) угла који се налази на врху једнакостраничног
троугла који чини звездин крак. Имајући ово у виду, допуни наредни
програм попуњавајући углове (одреди још и од колико се дужи састоји
звезда са :math:`n` кракова).

.. activecode:: корњача_n_токрака
   :nocodelens:
   :enablecopy:
   :playtask:

   import turtle
   n = 7
   uglovi = (0, 0)
   for i in range(0):
       turtle.forward(40) 
       turtle.left(uglovi[i % 2])
   ====
   import turtle
   n = 7
   uglovi = [360/n, -720/n]
   for i in range(2*n):
       turtle.forward(40) 
       turtle.left(uglovi[i % 2])
     
   
Три квадрата
''''''''''''
.. level:: 2
	   
.. questionnote::

   Напиши програм којим корњача црта мало сложенији облик који се
   састоји од три квадрата, окренутих за по 120 степени један у односу
   на други, при чему је први црвене, други зелене, а трећи плаве боје.

Боје квадрата можемо уписати у листу, а онда у сваком кораку спољне
петље мењати боју на основу одговарајућег елемента листе.
   
.. activecode:: полигони_угнежђена_петља_листе
   :nocodelens:
   :enablecopy:

   import turtle

   boje = ("red", "green", "blue")
   for i in range(3):
       turtle.color(boje[i])
       for j in range(4):
           turtle.forward(50)
           turtle.right(90)
       turtle.right(120)
     
