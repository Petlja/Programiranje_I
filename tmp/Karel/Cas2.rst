Час 2 - Робот Карел - условне петље, гранање
############################################

Поред наредби које робот може да извршава, које смо користили у
досадашњим програмима, робот Карел може да поставља следећа питања.

- ``moze_napred()`` - проверава да робот може да се помери напред (да
  ли испред њега постоји зид),
- ``ima_loptica_na_polju()`` - проверава да ли на пољу на ком се робот
  налази има лоптица,
- ``broj_loptica_na_polju()`` - враћа број лоптица на пољу на ком се
  робот налази,
- ``ima_loptica_kod_sebe()`` - проверава да ли робот тренутно има
  лоптица код себе.
- ``broj_loptica_kod_sebe()`` - враћа број лоптица које робот тренутно
  има код себе,



Понављање - условна петља `while`
---------------------------------

Иди напред док можеш
''''''''''''''''''''
.. level:: 1
   
.. questionnote::

   Наредни лавиринт је зачаран и не зна се колико тачно поља постоји
   између робота и лоптице. Напиши програм тако да робот и у таквом
   лавиринту увек стиже до лоптице и узима је. Подсећам те да помоћу
   ``mozeNapred()`` можеш проверити да ли се робот може померити
   напред, тј. да ли се испред њега налази зид.

Петљу ``for`` најчешће користимо када знамо тачно колико пута желимо
да се нешто понови. Међутим, постоји и други облик петље којим се
обезбеђује да се наредбе понављају све док је неки услов испуњен.  У
овом програму желимо роботу да наредимо да иде напред док год је то
могуће и након тога да покупи лоптицу. Док се на енглеском језику каже
while, па се и условна петља назива петља ``while``. Погледај како се
она може употребити. Покрени наредни програм више пута и видећеш да
исправно ради без обзира на то како се се зачарани лавиринт променио.
   
.. karel:: Карел_иди_напред_док_можеш
   :blockly:

   {
      setup: function() {
           function random(n) {
              return Math.floor(n * Math.random());
	   }

	   var N = 3 + random(3);
	   var world = new World(N, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
	   world.putBall(N, 1);
           var robot = new Robot();
	   var code = ["from karel import *",
                       "while mozeNapred():",
		       "    napred()",
		       "uzmi()"]
	   return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
           var lastAvenue = world.getAvenues();
           return robot.getStreet() === 1 &&
           robot.getAvenue() === lastAvenue &&
	   world.getBalls(lastAvenue, 1) == 0;
      }
   }

Запамти, ``while`` значи док. У преходном програму смо, дакле, роботу
рекли следеће: "Док можеш да идеш напред иди напред. Узми лоптицу."

Приметимо и да се након услова петље ``while`` наводи двотачка, док се
наредбе које се понављају увлаче (веома слично као што је био случај и
код петље ``for``). И поруке о грешкама уколико се то не испоштује су
сличне.

И петљама ``while`` ћемо се детаљније бавити у поглављу `Понављање
<Ponavljanje.html>`_.


Купи лоптице док можеш
''''''''''''''''''''''
.. level:: 1
   
.. questionnote::

   Наредни лавиринт је зачаран и не зна се колико тачно има лоптица
   испред робота. Напиши програм којим робот купи све те лоптице.

Један начин да се реши задатак је да се прво одреди колико је лоптица
на пољу на ком се робот налази, а затим да се употреби петља
``for``. Број лоптица на пољу се може одредити позивом
``broj_loptica_na_polju()``.

   
.. karel:: Карел_купи_лоптице_док_можеш
   :blockly:

   {
      setup: function() {
           function random(n) {
              return Math.floor(n * Math.random());
	   }

	   var world = new World(2, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
	   var N = 5 + random(5);
	   world.putBalls(2, 1, N);
           var robot = new Robot();
	   var code = ["from karel import *",
	               "napred()",
		       "for i in range(broj_loptica_na_polju()):",
		       "    uzmi()"]
	   return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
           return robot.getStreet() === 1 &&
           robot.getAvenue() === 2 &&
	   world.getBalls(2, 1) == 0;
      }
   }

Овим програм смо рекли роботу следеће: *"Онолико пута колико је на
пољу лоптица, узми лоптицу"*.

Други начин да се задатак реши је да се употреби петља ``while`` и да
се лоптице купе све док их има на пољу. Ту проверу робот може да
изврши коришћењем питања ``ima_loptica_na_polju()``.

Покушај да измениш претходни програм и задатак решиш на овај
начин. Твој програм треба роботу да каже следеће *"Иди напред. Док има
лоптица на пољу узимај лоптицу"*.

.. reveal:: Карел_купи_лоптице_док_можеш_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење
   
   .. activecode:: Карел_купи_лоптице_док_можеш_решење
      :passivecode: true

      napred()
      while ima_loptica_na_polju():
         uzmi()

Претходни садржај можеш погледати и у наредној видео-лекцији.
      
.. ytpopup:: Zk-4gG4iZmc
      :width: 735
      :height: 415
      :align: center

Гранање
-------

Покупи лоптицу ако је има
'''''''''''''''''''''''''
.. level:: 1

.. questionnote::

   Наредни лавиринт је зачаран. Сваки пут када се робот покрене,
   лоптице на три поља испред њега се наместе другачије. Напиши
   програм којим робот купи све лоптице.

Робот треба три пута да се помери напред и да са сваког поља на које
дође покупи лоптицу (ако на пољу има лоптица). Међутим, пре него што
покупи лоптицу он мора да провери да ли на том пољу уопште постоји
лоптица. Провера услова у програмском језику Python (а и у многим
другим програмским језицима) врши се наредбом ``if``, што на енглеском
језику значи ако.

.. activecode:: Карел_покупи_лоптицу_ако_је_има_if
   :passivecode: true

   if ima_loptica_na_polju():
       uzmi()

Подсетимо се, помоћу услова ``ima_loptica_na_polju`` испитујемо да ли
на пољу има лоптица. Претходним кодом смо роботу рекли *"Ако на пољу
на ком стојиш има лоптица, онда узми лоптицу"*, чиме постижемо да
Карел провери да ли на пољу има лоптица и да, ако их има, узме једну
лоптицу.  Приметимо да је, слично као и код петљи, након услова
наведена двотачка, а да је наредба која се извршава ако је услов
испуњен мало увучена. То је обавезно и, ако то не испоштујеш, добићеш
поруку о грешци, веома сличну као и код петљи.

У зависности од тога да ли је услов који проверавамо испуњен, ток
програма се *грана*, па се наредба ``if`` назива и **наредба
гранања**.  Гранањем и наредбом ``if`` ћемо се много детаљније бавити
у поглављу `Гранање <../KontrolaToka/Cas11.html>`_.

Дакле, да бисмо решили задатак, комбиноваћемо померање робота и
наредбу гранања којом ћемо проверавати да ли на пољу постоји лоптица,
пре него што је робот покупи.
   
.. karel:: Карел_покупи_лоптицу_ако_је_има
   :blockly:

   {
      setup: function() {
	   var world = new World(4, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
	   for (var k = 2; k <= 4; k++)
	      if (Math.random() > 0.5) 
                  world.putBall(k, 1);
           var robot = new Robot();
	   var code = ["from karel import *",
					"napred();             # idi napred",
					"if ima_loptica_na_polju():  # ako je na polju loptica:",
					"    uzmi()       #    uzmi lopticu",
					"",
					"napred();             # idi napred",
					"if ima_loptica_na_polju():  # ako je na polju loptica:",
					"    uzmi()       #    uzmi lopticu",
					"",
					"# dopuni program", "???"]
	   return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
           return world.getBalls(2, 1) == 0 &&
	          world.getBalls(3, 1) == 0 &&
	          world.getBalls(4, 1) == 0;
      }
   }

Приметимо да се у претходном програму наредбе

.. activecode:: Карел_покупи_лоптицу_ако_је_има_тело_петље
   :passivecode: true

   napred()
   if ima_loptica_na_polju():
       uzmi()

понављају три пута и можемо употребити петљу ``for`` да добијемо
једноставнији програм.

.. karel:: Карел_покупи_лоптицу_ако_је_има_for
    :blockly:
   
    {
      setup: function() {
	   var world = new World(4, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
	   for (var k = 2; k <= 4; k++)
	      if (Math.random() > 0.5) 
                  world.putBall(k, 1);
           var robot = new Robot();
	   var code = ["from karel import *",
        "for i in range(3): # ponovi tri puta",
        "    ??? # idi napred",
        "    if True: # ako je na polju loptica",
        "        ??? # uzmi lopticu"]
            return {world: world, robot: robot, code: code};
            },

      isSuccess: function(robot, world) {
           return world.getBalls(2, 1) == 0 &&
	          world.getBalls(3, 1) == 0 &&
	          world.getBalls(4, 1) == 0;
      }
    }
   

.. questionnote::

   И наредни лавиринт је зачаран и његова дужина се мења сваки пут
   када се робот покрене, при чему се лоптице на пољима поново
   непредвидиво размештају. Напиши програм којим робот у оваквом
   лавиринту купи све лоптице.

Пошто у овом случају робот не зна колико пута треба да се помери
напред, употребићемо петљу ``while`` и померати робота напред докле
год је то могуће.

.. karel:: Карел_покупи_лоптицу_ако_је_има_while
    :blockly:
   
    {
      setup: function() {
	   var world = new World(Math.floor(3 + 5 * Math.random()), 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
	   for (var k = 2; k <= world.getAvenues(); k++)
	      if (Math.random() > 0.5) 
                  world.putBall(k, 1);
           var robot = new Robot();
	   var code = ["from karel import *",
        "while moze_napred():",   
        "    ??? # popravi ovu liniju",
        "    if ima_loptica_na_polju():",
        "        ??? # popravi ovu liniju"]
	   return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
	   for (var k = 2; k <= world.getAvenues(); k++)
              if (world.getBalls(k, 1) != 0)
	         return false;
	   return true;
      }
    }

Претходни садржај можеш погледати и у наредној видео-лекцији.
      
.. ytpopup:: Nyun0pML3-M
      :width: 735
      :height: 415
      :align: center

    
Узимање и остављање лоптица
'''''''''''''''''''''''''''
.. level:: 1

.. questionnote::

   Карел не зна где се налазе лоптице, а има задатак да три поља
   испред себе промени тако да узме лоптице са оних поља на којима се
   налазе и да их постави на она поља на којима се не налазе.

У ранијим програмима смо видели како робот може да иде три поља напред
и да узима лоптице на које наиђе. Потребно је да тај програм проширимо
тако да робот оставља лоптице на празна поља. Најлакши начин да се то
уради је да кажемо следеће: "Ако је на пољу лоптица, онда је узми, а у
супротном је остави". То можемо остварити помоћу допуне наредби ``if``
помоћу речи ``else`` која значи у супротном тј. иначе.
   
.. karel:: Карел_узми_и_остави_лоптице
    :blockly:
   
    {
      setup: function() {
	   var world = new World(4, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
	   world.balls = [];
	   for (var k = 2; k <= world.getAvenues(); k++) {
	      var ball = Math.random() > 0.5;
	      world.balls.push(ball);
	      if (ball)
                  world.putBall(k, 1);
           }
           var robot = new Robot();
	   robot.setInfiniteBalls(true);
	   var code = ["from karel import *",
        "for i in range(3):",
        "    napred()",
        "    if ima_loptica_na_polju():",
        "        uzmi()",
        "    else:",
        "        ostavi()"
	   ]
	   return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
	   for (var k = 2; k <= world.getAvenues(); k++)
              if (world.getBalls(k, 1) == world.balls[k-2])
	         return false;
	   return true;
      }
    }

Дакле, ако желимо да робот изврши неке наредбе ако је неки услов
испуњен, а неке друге ако тај услов није испуњен, користимо наредбу
``if-else``. Иза речи ``if`` наводи се услов, затим двотачка и затим
наредбе које ће се извршити ако услов јесте испуњен. Нако тога се
наводи реч ``else`` поравната са речју ``if``, затим се наводи
двотачка, а наредбе које се извршавају ако услов наведен иза ``if``
није испуњен, такође се увлаче.

Претходни садржај можеш погледати и у наредној видео-лекцији.
      
.. ytpopup:: KQVm3KpZtrY
      :width: 735
      :height: 415
      :align: center
       
Кретање у круг
''''''''''''''
.. level:: 2


Покушај да решиш и наредни, мало тежи задатак. 

.. questionnote::

   Напиши програм којим се роботу наређује да се креће у круг око
   лавиринта и да покупи све лоптице на које наиђе.


Једна идеја за решење је да четири пута поновимо наредбе којима робот
иде напред докле год може и купи све лоптице на које наиђе.

.. karel:: Карел_покупи_лоптице_у_круг_1
    :blockly:
   
    {
      setup: function() {
           var dim = 5;
	   var world = new World(dim, dim);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");

	   for (var i = 1; i <= dim; i++)
	      if (Math.random() > 0.5)
	         world.putBall(i, 1);
	   for (var i = 1; i <= dim; i++)
	      if (Math.random() > 0.5)
	         world.putBall(i, dim);
	   for (var i = 2; i <= dim-1; i++)
	      if (Math.random() > 0.5)
	         world.putBall(1, i);
	   for (var i = 2; i <= dim-1; i++)
	      if (Math.random() > 0.5)
	         world.putBall(dim, i);

	   world.addEWWall(2, 1, dim-2);
	   world.addEWWall(2, dim-1, dim-2);
           world.addNSWall(1, 2, dim-2);
           world.addNSWall(dim-1, 2, dim-2);
	   
           var robot = new Robot();
	   var code = ["from karel import *",
        "for i in range(4):",
        "    while moze_napred():",
        "        ??? # popravi ovu liniju",
        "        if ima_loptica_na_polju():",
        "            ??? # popravi ovu liniju",
        "    ??? # popravi ovu liniju"
        ]
            return {world: world, robot: robot, code: code};
            },

      isSuccess: function(robot, world) {
           for (var i = 1; i <= world.dim; i++)
	      for (var j = 1; j <= world.dim; j++)
	         if (world.getBalls(i, j) != 0)
	         return false;
	   return true;
      }
    }


Још једна идеја за решење може биће следећа. Ако робот може да се
помери напред, онда ћемо му рећи да се помери напред и нако тога ћемо
му рећи да провери да ли се на пољу налази лоптица и да је узме. У
супротном, ако робот не може да се помери напред, значи да је дошао до
зида и тада ћемо му рећи да се окрене на лево. Све ово ћемо понављати
у једној петљи (која ће се извршити 20 пута, што је тачно број корака
који је потребан да би робот обишао цео круг). Покушај да наредни код
допуниш тако да робот успешно покупи све лоптице.

.. karel:: Карел_покупи_лоптице_у_круг_2
    :blockly:
   
    {
      setup: function() {
           var dim = 5;
	   var world = new World(dim, dim);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");

	   for (var i = 1; i <= dim; i++)
	      if (Math.random() > 0.5)
	         world.putBall(i, 1);
	   for (var i = 1; i <= dim; i++)
	      if (Math.random() > 0.5)
	         world.putBall(i, dim);
	   for (var i = 2; i <= dim-1; i++)
	      if (Math.random() > 0.5)
	         world.putBall(1, i);
	   for (var i = 2; i <= dim-1; i++)
	      if (Math.random() > 0.5)
	         world.putBall(dim, i);

	   world.addEWWall(2, 1, dim-2);
	   world.addEWWall(2, dim-1, dim-2);
           world.addNSWall(1, 2, dim-2);
           world.addNSWall(dim-1, 2, dim-2);
	   
           var robot = new Robot();
	   var code = ["from karel import *",
        "for i in range(20):",
        "    if moze_napred():",
        "        ??? # popravi ovu liniju",
        "        if ima_loptica_na_polju():",
        "            ??? # popravi ovu liniju",
        "    else:",
        "        ??? # popravi ovu liniju"
            ]
            return {world: world, robot: robot, code: code};
            },

      isSuccess: function(robot, world) {
           for (var i = 1; i <= world.dim; i++)
	      for (var j = 1; j <= world.dim; j++)
	         if (world.getBalls(i, j) != 0)
	         return false;
	   return true;
      }
    }

              
Домаћи задатак
--------------

Лоптице на три стране
'''''''''''''''''''''
.. level:: 2


.. questionnote::

   Помози роботу да покупи све лоптице. Пошто је лавиринт зачаран,
   мораћеш да употребиш петљу са провером услова.

.. karel:: Карел_лоптице_на_три_стране
  :blockly:

   {
     setup: function() {

         function random(n) {
             return Math.floor(n * Math.random());
         }
     
         var N = 4 + random(3);
         var world = new World(N, N);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(N);
         world.setRobotStartDirection("S");
         for (var i = N-1; i >= 1; i--)
            world.putBall(1, i);
         for (var i = 2; i <= N; i++)
            world.putBall(i, 1);
         for (var i = 2; i <= N; i++)
             world.putBall(N, i);
     
         world.addNSWall(1, 2, N-1);
         world.addEWWall(2, 1, N-2);
         world.addNSWall(N-1, 2, N-1); ;
         var robot = new Robot();
         var code = ["from karel import *"]
         return {world: world, robot: robot, code: code};
     },

     isSuccess: function(robot, world) {
          for (var i = 1; i <= world.getAvenues(); i++)
             for (var j = 1; j <= world.getStreets(); j++)
                if (world.getBalls(i, j) != 0)
                   return false;
         return true;
     }
   }

.. reveal:: Карел_лоптице_на_три_стране_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   Једно могуће решење (не и једино) је следеће.               

   .. activecode:: Карел_лоптице_на_три_стране_решење
      :passivecode: true
                    
      from karel import *
      for i in range(3):
          while moze_napred():
              napred()
              uzmi()
          levo() 

Покупи лоптице до којих можеш да дођеш
''''''''''''''''''''''''''''''''''''''
.. level:: 2

.. questionnote::

   Помози роботу да покупи све лоптице. Наравно, лавиринт је опет
   зачаран и распоред препрека и лоптица испред робота се мења
   приликом сваког покретања програма.
   
.. karel:: Карел_покупи_лоптице_до_којих_можеш_да_дођеш
    :blockly:
   
    {
      setup: function() {

         function random(n) {
             return Math.floor(n * Math.random());
         }

         var world = new World(4 + random(4), 2);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(2);
         world.setRobotStartDirection("E");

         world.addEWWall(1, 1, 1);
         var balls = 0;
         var prevBall = false;
         for (var i = 2; i <= world.getAvenues(); i++) {
             if (random(2) == 0 || (balls == 0 && i == world.getAvenues() - 1)) {
                 balls++;
                 if (!prevBall)
                    world.addNSWall(i-1, 1, 1);
                 world.putBall(i, 1);
                 prevBall = true;
             } else {
                 if (prevBall)
                    world.addNSWall(i-1, 1, 1);
                 world.addEWWall(i, 1, 1);
                 prevBall = false;
             }
         }

         var robot = new Robot();
         var code = ["from karel import *"]
         return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
           for (var i = 1; i <= world.getAvenues(); i++)
              for (var j = 1; j <= world.getStreets(); j++)
                 if (world.getBalls(i, j) != 0)
                    return false;
          return true;
      }
    }

У сваком кораку робот треба да се помери напред, затим да се окрене за
90 степени (ка југу) и провери да ли је испред њега препрека. Ако нема
препреке тј. ако може да иде напред, онда треба да оде напред, узме
лоптицу, окрене се за 180 степени (ка северу), поново оде напред и
окрене се за 90 степени (ка истоку). У супротном само треба да се
окрене за 90 степени (ка истоку).

.. reveal:: Карел_покупи_лоптице_до_којих_можеш_да_дођеш_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   Једно могуће решење (не и једино) је следеће.               

   .. activecode:: Карел_покупи_лоптице_до_којих_можеш_да_дођеш_решење
      :passivecode: true
                    
      from karel import *
      while moze_napred():
          napred()
          # okreni se prema jugu
          desno()
          # proveri da li je prepreka ispred tebe
          if moze_napred():
              # idi po lopticu
              napred()
              uzmi()
              # vrati se nazad
              levo()
              levo()
              napred()
              desno()
          else:
              # okreni se prema istoku
              levo()
