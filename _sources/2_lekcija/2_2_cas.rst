2.2 Гранање
##########################

Покупи лоптицу ако је има
'''''''''''''''''''''''''

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
на неком од наредних часова (ван контекста програма за робота Карела).

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
    
Узимање и остављање лоптица
'''''''''''''''''''''''''''

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

       
Кретање у круг
''''''''''''''


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

