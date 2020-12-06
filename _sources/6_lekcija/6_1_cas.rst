6.1. Корњача графика - задаци за вежбање
########################################

Циљ ове лекције је да кроз још неколико задатака утврдиш основне
појмове програмирања на примеру програмирања корњача графике.


Линијски програми
'''''''''''''''''

Слово M
'''''''
   
.. questionnote::

   Напиши програм у којем корњача црта слово М.

.. activecode:: корњача_слово_M
   :nocodelens:
   :playtask:

   import turtle
   
   turtle.left(90)
   turtle.forward(150)
   turtle.right(150)
   turtle.forward(100)
   # dovrši program tako da slovo M bude simetrično
   ====
   import turtle

   turtle.left(90)
   turtle.forward(150)
   turtle.right(150)
   turtle.forward(100)
   turtle.left(120)
   turtle.forward(100)
   turtle.right(150)
   turtle.forward(150)

Дијамант
''''''''

.. questionnote::

   Напиши програм у којем корњача исцртава облик дијаманта (облик се добије
   спајањем два једнакостранична троугла по заједничкој хоризонталној ивици).

.. activecode:: корњача_дијамант
   :nocodelens:
   :playtask:

   import turtle
   # dovrši program
   ====
   import turtle

   turtle.forward(100)
   turtle.left(120)
   turtle.forward(100)
   turtle.left(120)
   turtle.forward(100)
   turtle.left(60)
   turtle.forward(100)
   turtle.left(120)
   turtle.forward(100)


Лого Петље
''''''''''

.. questionnote::

   Напиши програм у којем корњача црта лого фондације петља. Лого се
   састоји од два квадрата странице 50 корака, која се додирују и
   окренути су 45 степени у односу на хоризонталу.

   .. image:: ../../_images/petlja.png
	:width: 200px
	:align: center

Допуни наредни програм наредбама којима се корњача окреће, тако да се
добије тражена слика.
		
.. activecode::	лого_петље
   :nocodelens:
   :enablecopy:
   :playtask:

   import turtle
   turtle.color("#18BC9C")
   turtle.width(20)
   ??? # okreni se
   turtle.forward(50)
   ??? # okreni se
   turtle.forward(100)
   ??? # okreni se
   turtle.forward(50)
   ??? # okreni se
   turtle.forward(50)
   ??? # okreni se
   turtle.forward(100)
   ??? # okreni se
   turtle.forward(50)
   ====
   import turtle
   turtle.color("#18BC9C")
   turtle.width(20)
   turtle.left(45)
   turtle.forward(50)
   turtle.right(90)
   turtle.forward(100)
   turtle.left(90)
   turtle.forward(50)
   turtle.left(90)
   turtle.forward(50)
   turtle.left(90)
   turtle.forward(100)
   turtle.right(90)
   turtle.forward(50)
   
      
Петље
'''''

Квадратни сигнал
''''''''''''''''

.. questionnote::

   Напиши програм у којем корњача црта облик квадратног сигнала, као
   на следећој слици.

   .. image:: ../../_images/kornjaca-kvadratni-signal.png
      :align: center

Основни корак у решавању задатка је да се овај сложени облик разложи
на низ једноставнијих облика који се понављају. Покушај прво да
размислиш како то може да се уради, а онда погледај наредну слику.

.. reveal:: квадратни_сигнал_решење
   :showtitle: Прикажи слику
   :hidetitle: Сакриј слику

   .. image:: ../../_images/kornjaca-kvadratni-signal-boje.png
      :align: center

Дакле, облик се састоји од пет понављања основног облика, који се може
добити тако што корњача иде напред, затим се окрене налево, иде
напред, окрене се надесно, иде напред, опет се окрене надесно, иде
напред и окрене се налево (увек се окреће за по 90 степени).
	      
.. activecode:: квадратни_сигнал
   :nocodelens:
   :playtask:

   import turtle
   # dopuni program
   ====
   import turtle
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
     

За вежбу прилагоди програм тако да се димензије облика лако мењају
(уведи променљиве које представљају дужину и ширину основног облика).

Тестерица
'''''''''

.. questionnote::

   Напиши програм којим корњача црта тестерицу са 10 зубаца. Угао при
   врху сваког зупца треба да буде 45 степени, а размак између два
   суседна зупца 25 корака (покушај да на основу тога одредиш дужину
   косих линија које се цртају).

   
.. activecode:: тестерица
   :nocodelens:
   :playtask:

   import turtle
   # dopuni program
   ====
   import turtle

   for i in range(10):
       turtle.left(45)
       turtle.forward(35)
       turtle.right(135)
       turtle.forward(25)
       turtle.left(90)

Плус
''''
   
.. questionnote::

   Напиши програм којим корњача исцртава плус (сваки од четири крака
   плуса је дугачак 50 корака).

У сваком кораку корњача може да оде напред 50 пиксела, да се се врати
назад 50 пиксела и да се окрене за 90 степени.
   
.. activecode:: корњача_плус
   :nocodelens:
   :playtask:

   import turtle
   # dovrši program
   ====
   import turtle
   
   for i in range(4):
       turtle.forward(50)
       turtle.backward(50)
       turtle.right(90)

Отисци корњаче у теменима n-тоугла
''''''''''''''''''''''''''''''''''

.. questionnote::
   
   Напиши програм након који поставља отиске корњаче у сва темена
   правилног n-тоугла.

.. activecode:: отисци_n_тоугао
   :nocodelens:
   :enablecopy:
   :playtask:

   import turtle
   n = 6
   ====
   import turtle
   n = 6
   turtle.shape("turtle")
   turtle.penup()
   for i in range(n):
       turtle.stamp()
       turtle.forward(80)
       turtle.left(360 / n)

Звезда
''''''

.. questionnote::

   Напиши програм у којем корњача црта звезду са пет кракова.

.. image:: ../../_images/star5.png
   :width: 300px   
   :align: center

Израчунајмо унутрашње и спољашње углове звезде са 5 кракова. Пошто је
збир унутрашњих углова правилног петоугла једнак `(5-2)\cdot 180`,
сваки његов унутрашњи угао правилног мноугла је
:math:`\frac{(5-2)\cdot 180^\circ}{5} = 108^\circ`. Сваки крак је
једнакокраки троугао, чији су углови на основици једнаки
:math:`180^\circ - 108^\circ = 72^\circ`, па је угао при врху једнак
:math:`180^\circ - 2\cdot 72^\circ = 36^\circ`. Звезду ћемо цртати
тако што ћемо пет пута нацртати дуж од 100 корака и затим се окренути
тако да наредна дуж заклопи угао од :math:`36^\circ` са претходном. Да
бисмо то постигли, корњача треба да се окрене надесно за суплемент тог
угла тј. за угао од :math:`180^\circ - 36^\circ = 144^\circ`.


.. activecode:: корњача_петокрака
   :nocodelens:
   :enablecopy:
   :playtask:

   import turtle
   for i in range(5):         # ponovi 5 puta:
                              #   idi napred 100 koraka
                              #   okreni se nadesno 144 stepena
   ====			      
   import turtle
   for i in range(5):         # ponovi 5 puta:
       turtle.forward(100)     #   idi napred 100 koraka
       turtle.right(144)       #   okreni se nadesno 144 stepena
      
       
Осмокрака пахуља
''''''''''''''''

.. questionnote::

   Напиши програм који црта пахуљу која има 8 кракова дужине од по 50
   корака.
      
.. activecode:: корњача_осмокраки_плус
   :nocodelens:
   :playtask:
  
   import turtle
   # dovrši program
   ====
   import turtle
   
   for i in range(8):
       turtle.forward(50)
       turtle.backward(50)
       turtle.left(45)

n-токрака пахуља
''''''''''''''''
       
.. questionnote::

   Напиши програм на основу којег корњача црта пахуљицу која се
   састоји од :math:`n` кракова дужине 50 корака, равномерно
   распоређених у круг (сваки крак креће из центра).
      
.. activecode:: корњача_n-токраки_плус
   :nocodelens:
   :playtask:

   import turtle
   # dovrši program
   ====
   import turtle
   turtle.speed(10)
   n = 16
   for i in range(n):
       turtle.forward(50)
       turtle.backward(50)
       turtle.left(360 / n)

Гранање
'''''''

Парни и непарни кракови различите дужине
''''''''''''''''''''''''''''''''''''''''
       
.. questionnote::

   Модификуј претходни програм тако да је сваки други крак краћи
   (дугачак 30 корака).

.. activecode:: корњача_n-токраки_пахуља
   :nocodelens:
   :playtask:

   import turtle
   # dovrši program
   ====
   import turtle
   
   turtle.speed(10)
   n = 36
   for i in range(n):
       if i % 2 == 0:
           duzina = 50
       else:
           duzina = 30
       turtle.forward(duzina)
       turtle.backward(duzina)
       turtle.left(360/n)


Процедуре
'''''''''

           
Квадрат шарених ивица
'''''''''''''''''''''

.. questionnote::

   Дефиниши процедуру за цртање линије у којој се насумично смењују
   дужи две боје. Параметри процедуре треба да буду број дужи, дужина
   сваке дужи и две боје. Употреби процедуру да нацрташ квадрат коме
   ће ивице бити састављене од таквих линија.

.. activecode:: квадрат_шарених_ивица
   :nocodelens:
   :enablecopy:
   :playtask:

   import turtle
    
   def sarena_duz(n, a, boja1, boja2):
       for ???:
           if i % 2 == 0:
               turtle.color(boja1)
           else:
               turtle.color(boja2)
           ???
    
   turtle.width(10)
   sarena_duz(11, 10, "red", "blue")
   turtle.left(90)
   sarena_duz(11, 10, "green", "yellow")
   ???
   ???
   turtle.left(90)
   ???
   turtle.left(90)
   ====      
   import turtle
    
   def sarena_duz(n, a, boja1, boja2):
       for i in range(n):
           if i % 2 == 0:
               turtle.color(boja1)
           else:
               turtle.color(boja2)
           turtle.forward(a)
    
    
   turtle.width(10)
   sarena_duz(11, 10, "red", "blue")
   turtle.left(90)
   sarena_duz(11, 10, "green", "yellow")
   turtle.left(90)
   sarena_duz(11, 10, "orange", "black")
   turtle.left(90)
   sarena_duz(11, 10, "purple", "cyan")
   turtle.left(90)
   

