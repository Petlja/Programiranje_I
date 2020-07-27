Час 5 - Корњача графика - гранање, угнежђене петље, процедуре, торке/листе
##########################################################################

Гранање
-------

Приликом цртања неких фигура корњача наизменично треба да извршава
одређене врсте наредби. На пример, приликом цртања испрекидане линије
корњача у сваком кораку помера напред и након сваког померања или
подиже или спушта оловку и то чини наизменично (напред, подигни,
напред, спусти, напред, подигни, напред, спусти). То је могуће постићи
тако што се у сваком кораку петље испитује да ли је вредност бројача
парна или непарна тј. да ли при дељењу са два даје остатак 0 (као што
ћемо детаљније описати у поглављу о `израчунавању
<../Izracunavanje/toctree.html>`_, у језику Python се остатак при
дељењу броја ``i`` са 2 може израчунати помоћу ``i % 2``). Гранање,
тј. условно извршавање наредби, постижемо помоћу наредбе ``if-else``.

Испрекидана линија
''''''''''''''''''
.. level:: 2

.. questionnote::	   

   Нацртај поново испрекидану линију, али овај пут коришћењем гранања.

Корњача иде напред 10 пута, при чему пет пута од тога има подигнуту, а
пет пута има спуштену оловку. Дакле, уведи петљу чије се тело понавља
пет пута, у телу петље помери корњачу за 20 корака, а затим или
подигни или спусти оловку, тако да то буде наизменично (то можеш
реализовати тако што ћеш у парним корацима подизати, а у непарним
корацима спуштати оловку). Имајући ово у виду исправи наредни програм
тако да црта испрекидану линију.

.. activecode:: испрекидана_линија_1
   :nocodelens:
   :enablecopy:
   :playtask:

   import turtle
   for i in range(0):
       turtle.forward(0)
       if True:
           turtle.penup()
       else:
           turtle.pendown()
   ====
   import turtle
   for i in range(10):
       turtle.forward(20)
       if i % 2 == 0:
           turtle.penup()
       else:
           turtle.pendown()   

     
Звезда без пресецања
''''''''''''''''''''
.. level:: 2

.. questionnote::

   Напиши програм у којем корњача црта звезду без цртања унутрашњег
   петогула, као на следећој слици.

   .. image:: ../../_images/kornjaca-zvezda.png
      :align: center

Звезду можемо нацртати тако што нацртамо десет дужи (десет кракова
једнакокраких троуглова који представљају краке звезде). Након цртања
сваке од тих дужи окрећемо се и то наизменично налево за
:math:`72^\circ` (када смо у дну крака) па надесно за
:math:`144^\circ` (када смо на врху крака). Поново наизменично
изршавање наредби (овај пут окретања) можемо остварити тако што
проверавамо парност бројачке променљиве.
     
.. activecode:: корњача_петокрака_1
   :nocodelens:
   :enablecopy:

   import turtle
   for i in range(10):        # ponovi 10 puta:
       turtle.forward(40)     #    idi napred 40 koraka
       if ???:                #    ako je vrednost brojaca i paran broj:
           turtle.???         #       okrneni se ulevo za 72 stepena
       else:                  #    u suprotnom:
           turtle.???         #       okreni se udesno za 144 stepena



Угнежђене петље
---------------

У сложенијим задацима имамо потребу да се облици који се ицртавају
коришћењем петљи понављају неколико пута. Тако се добијају програми
који садрже петље у чијем телу се налазе друге петље. Такве петље
називају се **угнежђене петље**. Урадимо неколико примера овог облика.


Три квадрата
''''''''''''
.. level:: 2
	   
.. questionnote::

   Напиши програм којим корњача црта мало сложенији облик који се
   састоји од три квадрата, окренутих за по 120 степени један у односу
   на други, као на слици.

.. activecode:: полигони_угнежђена_петља
   :nocodelens:
   :enablecopy:

   import turtle

   for i in range(3):
       for j in range(4):
           turtle.forward(50)
	   turtle.right(90)
       turtle.right(120)

По сличном принципу можемо нацртати и наизглед доста сложеније облике.

Компликованија звезда
'''''''''''''''''''''
.. level:: 3

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
         

.. questionnote::

   Напиши програм који исцртава десет квадрата који имају заједничко
   доње лево теме и чије су дужине страница редом 10, 20, 30, 40 и
   тако даље.

.. activecode:: квадрати
   :nocodelens:
   :enablecopy:
   :playtask:

   import turtle
   n = 10
   for i in range(10):
       a = 10*i + 10
       ???
   ====
   import turtle
   n = 10
   for i in range(10):
       a = 10*i + 10
       for i in range(4):
           turtle.forward(a)
           turtle.left(90)
       
Процедуре
---------

Угнежђене петље се могу избећи, а програми се могу учинити много
разумљивијим ако се уведу процедуре за цртање основних облика.

Процедура за цртање многоугла
'''''''''''''''''''''''''''''
.. level:: 2

Приметимо да се цртање многоугла (каже се и *полигона*) јавило у више
различитих програма. Стога је корисно дефинисати **процедуру** за
цртање многоугла.  Параметри те процедуре биће број страница полигона
и дужина једне странице.

.. activecode:: процедура
   :passivecode: true

   # procedura za crtanje pravilnog poligona
   # parametri su broj stranica poligona n i duzina stranice a
   def poligon(n, a):
       for i in range(n):             # n puta ponovi:
           turtle.forward(a)          #    idi napred a koraka
	   turtle.right(360 / n)      #    okreni se za spoljasnji ugao n-tostranog pravilnog poligona
   
Дефиниција процедуре започета је кључном речју ``def`` након чега је
наведен назив процедуре (у нашем примеру, то је био ``poligon``), а
након тога параметри процедуре у заградама. Након двотачке, наведен је
програмски код који чини тело процедуре, увучен у односу на прву
линију (слично као што је и тело наредби ``for``, ``while`` и ``if``
увек увучено). Тело сачињавају наредбе које се извршавају сваки пут
када се процедура позове.

Дефинисањем процедуре дефинисали смо заправо нову наредбу коју можемо
користити у пруграму. Након ове дефиниције, квадрат димензије 100
пиксела нацртаћемо тако што наведемо ``poligon(4, 100)``, а шестоугао
димензије 50 тако што наведемо ``poligon(6, 50)``. Са процедуром за
цртање многоугла на располагању, наш програм за цртање три квадрата
различите боје је доста једноставније написати и постаје доста
разумљивији.

.. activecode:: полигон_процедура
   :nocodelens:
   :enablecopy:
		
   import turtle

   # definisemo proceduru za crtanje pravilnog poligona
   # parametri su broj stranica poligona n i duzina stranice a
   def poligon(n, a):
       for i in range(n):             # n puta ponovi:
           turtle.forward(a)          #    idi napred a koraka
	   turtle.right(360 / n)      #    okreni se za spoljasnji ugao n-tostranog pravilnog poligona

   for i in range(3):                 # 3 puta ponovi:
       poligon(4, 50)                 #   nacrtaj kvadrat dimenzije 50 koraka
       turtle.right(360 / 3)          #   kvadrati su pravilno rasporedjeni duž punog kruga, pa se okreni za 120 stepeni

Покушај да измениш претходни програм тако да уместо квадрата црта три
шестоугла дужине страница 80 корака.
       
Четири квадрата
'''''''''''''''
.. level:: 3

.. questionnote::

   Напиши програм у којем корњача црта облик који се састоји од четири
   квадрата, како је приказано на наредној слици.
   
   .. image:: ../../_images/kornjaca-cetiri-kvadrata.png
      :align: center

Дефиниши процедуру за цртање квадрата, а затим размисли како су ти
квадрати међусобно распоређени, тј. колико треба да се окрене корњача
након завршетка цртања сваког квадрата.

.. activecode:: четири_квадрата
   :nocodelens:
   :enablecopy:
   :playtask:

   import turtle
   n = 100
   # dopuni resenje
   ====
   import turtle
   n = 100
   for j in range(4):
       for i in range(4):
           turtle.forward(n)
           turtle.left(90)
       turtle.left(90)
   
   
.. reveal:: четири_квадрата_решење
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   Решење са петљом у петљи.
	       
   .. activecode:: четири_квадрата_1

      import turtle
      n = 100
      for j in range(4):
          for i in range(4):
	      turtle.forward(n)
	      turtle.left(90)
	  turtle.left(90)

   Решење са помоћном процедуром за цртање квадрата.
	 
   .. activecode:: четири_квадрата_2

      import turtle

      def kvadrat(n):
          for i in range(4):
	  turtle.forward(n)
	  turtle.left(90)

      n = 100
      for i in range(4):
          kvadrat(n)
	  turtle.left(90)

Торке/листе
-----------

Некада желимо да се у сваком кораку петље користи различита вредност.
Најједноставнији начин да тако нешто постигнемо је да употребимо торку
тј. листу вредности (о чему ће бити много више речи у поглављу о
`структурама података <../StrukturePodataka/toctree.html>`_). Погледајмо
пар примера ове технике.

Шарени квадрат - петља
''''''''''''''''''''''
.. level:: 2

.. questionnote::

   Допуни претходни програм тако да црта шарени квадрат, чије су боје
   страница редом црвена, зелена, плава и жута.

За решавање задатка нам је згодно да употребимо торку у којој ћемо
упамтити четири ниске које представљају називе те четири боје на
енглеском језику (такву торку можемо дефинисати помоћу ``boje =
("red", "green", "blue", "yellow")``).  У сваком кораку петље, боју
ћемо постављати на i-ти елемент те торке, где је i бројачка променљива
која редом узима вредности 0, 1, 2 и 3 (i-том елементу торке ``boje``
можемо приступити навођењем ``boje[i]``). У наредном програму опет има
неколико грешака и твој задатак је да их исправиш.

.. activecode:: корњача_шарени_квадрат
   :nocodelens:
   :enablecopy:
   :playtask:

   import turtle
   boje = ("red", "green", "", "yellow")
   for i in range(0):      # ponovi 4 puta:
       turtle.color(boje)    #   postavi boju na i-ti element torke boja
       turtle.forward(0)     #   idi napred 100 koraka
       turtle.left(0)        #   okreni se nalevo za 90 stepeni
   ====
   import turtle
   boje = ("red", "green", "blue", "yellow")
   for i in range(4):      # ponovi 4 puta:
       turtle.color(boje[i]) #   postavi boju na i-ti element torke boja
       turtle.forward(100)   #   idi napred 100 koraka
       turtle.left(90)       #   okreni se nalevo za 90 stepeni


Звезда без пресецања
''''''''''''''''''''
.. level:: 2

.. questionnote::

   Напиши програм у којем корњача црта звезду без цртања унутрашњег
   петогула, као на следећој слици.

   .. image:: ../../_images/kornjaca-zvezda.png
      :align: center

Овај задатак смо већ решавали уз помоћ гранања, али решење можемо
добити и уз помоћ двочлане листе. У листу можемо поставити углове од
72 и -144 степена и у сваком кораку се окретати улево за један од та
два угла (окрет удесно за 144 степена је једнак окрету улево за -144
степена), наизменично. Угловима из листе приступамо наизменично,
тј. приступамо угловима на позицији 0, затим 1, па 0, па 1, и тако
даље. Ово можемо остварити тако што у сваком кораку приступимо углу у
листи на позицији која се добије као остатак при дељењу променљиве
``i`` бројем два (подсетимо се, тај остатак можемо израчунати помоћу
``i % 2``).  У складу са тим исправи наредни програм.

.. activecode:: корњача_петокрака_2
   :nocodelens:
   :enablecopy:
   :playtask:

   import turtle
   uglovi = (0, 0)
   for i in range(10):          # ponovi 10 puta:
       turtle.forward(40)         #    idi napred 40 koraka
       turtle.left(uglovi[0])     #    okreni se ulevo za naredni od dva ugla iz liste
   ====
   import turtle
   uglovi = (72, -144)
   for i in range(10):          # ponovi 10 puta:
       turtle.forward(40)         #    idi napred 40 koraka
       turtle.left(uglovi[i % 2]) #    okreni se ulevo za naredni od dva ugla iz liste

   
Домаћи задатак
--------------

Шарени облик
''''''''''''
.. level:: 2

.. questionnote::

   Наредни интересантан облик се добија тако што корњача црта црвену
   линију дужине 50 и затим се налево окреће за 31 степен, затим црта
   зелену линију дужине 70 и окреће се налево за 71 степен, затим црта
   плаву линију дужине 90 и окреће се налево за 101 степен након чега
   се цртеж наставља по истом принципу. Напиши програм који анализом
   остатка при дељењу са 3 бројача у петљи одређује шта треба да
   уради.

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
           
Квадрат шарених ивица
'''''''''''''''''''''
.. level:: 2

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
   
   
