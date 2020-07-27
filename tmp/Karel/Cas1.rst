Час 1 - Робот Карел - линијски програми и бројачке петље
########################################################

Хајде на почетку мало да се играмо тако да кроз игру научимо неке
основне појмове програмирања. Одличан начин за то је писање програма
за робота који се зове Карел (по чешком писцу Карелу Чапеку, који је
измислио реч робот).

Наредбе које Карел разуме
-------------------------

Робот Карел се налази у лавиринту и разуме наредне наредбе

- ``napred()`` - помери се једно поље напред,
- ``levo()`` - окрени се 90 степени налево (у смеру супротном казаљки на сату),
- ``desno()`` - окрени се 90 степени надесно (у смеру казаљке на сату),
- ``uzmi()`` - покупи лоптицу са поља на којем се налазиш,
- ``ostavi()`` - спусти лоптицу на поље на којем се налазиш
  
Робот Карел разуме и програмски језик Python и, програмирајући га,
научићемо неколико основних наредби тог језика. Испрограмирали смо га
тако да ради унутар прегледача веба и не мораш ништа додатно да
инсталираш да би писао програме за Карела. 

Линијски програми
-----------------
  
Прикажимо употребу ових наредби на неколико једноставних програма.

Иди до лоптице и узми је
''''''''''''''''''''''''
.. level:: 1

.. questionnote::

   Напиши програм на основу којега ће робот доћи на поље (3, 3) и
   покупити лоптицу.

Да би дошао на жељено поље робот мора два пута да иде напред, да се
окрене на лево, затим опет да иде два пута напред и на крају да покупи
лоптицу. То му можемо наредити наредним програмом.
   
.. karel:: Карел_на_поље_33

   {
        setup:function() {
            var world = new World(5,5);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            world.putBall(3, 3);
            world.addEWWall(1, 1, 2);
            world.addNSWall(2, 2, 2);
            world.addEWWall(2, 3, 3);
            world.addNSWall(3, 1, 2);
            world.addNSWall(3, 4, 1);
            world.addNSWall(1, 5, 1);
            world.addEWWall(4, 1, 1);
            
	    var robot = new Robot();

	    var code = ["from karel import *",
					"napred()      # idi napred",
					"napred()      # idi napred",
					"levo()        # okreni se nalevo",
					"napred()      # idi napred",
					"napred()      # idi napred",
					"uzmi()        # uzmi lopticu"];
            return {robot:robot, world:world, code:code};
        },
	
        isSuccess: function(robot, world) {
           return robot.getStreet() === 3 &&
           robot.getAvenue() === 3 &&
	   robot.getBalls() === 1;
        },
   }

Прва линија програма ``from karel import *`` је линија којом почињу
сви програми за Карела - остави је таквом каква јесте. Након тога се
роботу задаје једна по једна наредба, свака у посебном реду. Иза сваке
наредбе роботу наведене су заграде (њих не смемо изоставити). Додатно,
свака наредба мора бити у посебном реду и испред наредби не смеш
писати размаке. Оваква правила називају се синтаксичка правила и ако
се неко од њих не испоштује долази до **синтаксичке грешке**. Програм не
сме садржати ни једну синтаксичку грешку да би исправно радио.

Текст иза знака ``#`` представља такозване коментаре. Робот тај текст
не чита - написали смо га само да би теби било јасније шта која
наредба значи.

У наредном програму има неколико синтаксичких грешака. Ако покушаш да
га покренеш добићеш поруку

::

   SyntaxError: bad input on line 4

Примети да је грешка пријављена у линији 4 иако је грешка направљена
већ у линији 3, где су изостављене заграде. Ово се често дешава, па
када анализираш где је грешка настала, увек провери и линију испред
оне која је у поруци о грешци наведена.
   
Исправи све синтаксичке грешке, па онда покрени програм.

.. karel:: Карел_на_поље_33_грешке

   {
        setup:function() {
            var world = new World(5,5);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            world.putBall(3, 3);
            world.addEWWall(1, 1, 2);
            world.addNSWall(2, 2, 2);
            world.addEWWall(2, 3, 3);
            world.addNSWall(3, 1, 2);
            world.addNSWall(3, 4, 1);
            world.addNSWall(1, 5, 1);
            world.addEWWall(4, 1, 1);
          
			var robot = new Robot();

	    var code = ["from karel import *",
					"napred()",
					"napred",
					"  levo()",
					"napred)",
					"    napred[]",
					" uzmi{}"];
            return {robot:robot, world:world, code:code};
        },
	
        isSuccess: function(robot, world) {
           return robot.getStreet() === 3 &&
           robot.getAvenue() === 3 &&
	   robot.getBalls() === 1;
        },
   }


У претходном програму је свака наредба Карелу била написана у посебној
линији. Могуће је задати и више наредби у једној линији, али тада их
је потребно раздвојити тачка-запетом (симболом ``;``).

.. karel:: Карел_на_поље_33_један_ред

   {
        setup:function() {
            var world = new World(5,5);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            world.putBall(3, 3);
            world.addEWWall(1, 1, 2);
            world.addNSWall(2, 2, 2);
            world.addEWWall(2, 3, 3);
            world.addNSWall(3, 1, 2);
            world.addNSWall(3, 4, 1);
            world.addNSWall(1, 5, 1);
            world.addEWWall(4, 1, 1);
          
			var robot = new Robot();

	    var code = ["from karel import *",
                        "napred(); napred(); levo(); napred(); napred(); uzmi()"];
            return {robot:robot, world:world, code:code};
        },
	
        isSuccess: function(robot, world) {
           return robot.getStreet() === 3 &&
           robot.getAvenue() === 3 &&
	   robot.getBalls() === 1;
        },
   }

Решење у којем је свака наредба у посебној линији се ипак мало чешће
користи (вероватно зато што се такав код лакше чита и мења, ако је то
потребно).

Претходни садржај можеш погледати и у наредној видео-лекцији.

.. ytpopup:: s9KCMku_StY
      :width: 735
      :height: 415
      :align: center


Програмирање слагањем блокова
'''''''''''''''''''''''''''''

Пошто претпостављамо да већ познајеш програмирање уз помоћ слагања
блокова (на пример у програму MIT Scratch или на сајту `code.org
<http://code.org/>`_), омогућили смо ти да прве програме пишеш на два
начина: текстом у програмском језику Python или слагањем
блокова. Сваки програм написан за робота Карела се може приказати и у
облику блокова - довољно је да притиснеш дугме **Blockly**.  Програм
састављен од блокова можеш мењати и прилагођавати (можеш променити
редослед блокова, додати нове блокове, обрисати неке блокове,
променити вредности уписане у неке блокове и слично) и када завршиш
дугметом **Врати у Python**, које се налази у доњем десном углу прозора,
тај програм можеш добити написан у језику Python. Ускоро ћеш и
сам/сама видети да је писање текста често бржи и ефикаснији начин
креирања програма (зато сви професионални програмери своје програме
пишу у текстуалним, а не у блоковским језицима), тако да те
охрабрујемо да од самог почетка кренеш да програме уносиш куцањем
текста у програмском језику Python, а да блокове користиш само као
помоћно средство када се заглавиш.

Испробај ту могућност на примеру који смо мало пре видели, тако што
ћеш коришћењем блокова додати наредбе која недостају, тако да робот
дође до поља (3, 3) и покупи лоптицу.

.. karel:: Карел_на_поље_33_Blockly
   :blockly:

   {
        setup:function() {
            var world = new World(5,5);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            world.putBall(3, 3);
            world.addEWWall(1, 1, 2);
            world.addNSWall(2, 2, 2);
            world.addEWWall(2, 3, 3);
            world.addNSWall(3, 1, 2);
            world.addNSWall(3, 4, 1);
            world.addNSWall(1, 5, 1);
            world.addEWWall(4, 1, 1);
          
			var robot = new Robot();

	    var code = ["from karel import *",
					"napred()      # idi napred",
					"napred()      # idi napred",
					"napred()      # idi napred",
					"napred()      # idi napred"];
            return {robot:robot, world:world, code:code};
        },
	
        isSuccess: function(robot, world) {
           return robot.getStreet() === 3 &&
           robot.getAvenue() === 3 &&
	   robot.getBalls() === 1;
        },
   }

Ако покренеш програм пре него што додаш наредбу да робот скрене,
видећеш да ће доћи до грешке током извршавања твог програма. Наиме, у
трећем кораку напред робот ће ударити у зид и добићеш поруку ``Робот
је ударио у зид``.

Коришћење блокова демонстрирано је и у наредној видео-лекцији.

.. ytpopup:: 0BzYkGw_nmQ
      :width: 735
      :height: 415
      :align: center
   
Пребаци лоптицу на поље (3, 5)
''''''''''''''''''''''''''''''
.. level:: 1

.. questionnote::

   У овом задатку ћемо нашем роботу дати мало компликованији задатак.
   Потребно је дође до поља (4, 3) на којем се налази једна лоптица, а
   затим да ту лоптицу пребаци у рупу на пољу (3, 5).

Допуни наредни програм тако да робот изврши дати задатак.   
   
.. karel:: Карел_пребаци_лоптицу
   :blockly:

   {
	setup: function() {
	   var world = new World(5, 5);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           world.putBall(4, 3);
           world.putHole(3, 5);
           world.addEWWall(1, 1, 2);
           world.addNSWall(2, 2, 2);
           world.addEWWall(2, 3, 3);
           world.addNSWall(3, 1, 2);
           world.addNSWall(3, 4, 1);
           world.addNSWall(1, 5, 1);
           world.addEWWall(4, 1, 1);
           var robot = new Robot();
	   var code = [ "from karel import *",
					"napred()",
					"napred()",
					"levo()",
					"napred()",
					"napred()",
					"desno()",
					"napred()",
					"uzmi()",
					"???    # dodaj naredbe koje nedostaju ovde",
					"ostavi()"]
           return {robot:robot, world:world, code: code};
	},

	isSuccess: function(robot, world) {
	   return world.getBalls(3, 5) == 0;
	}
   }

Ако користиш блокове, на месту на ком треба да додаш нове наредбе
добићеш један велики зелени блок који треба да избациш (на пример, да
га превучеш до канте за смеће) и да га замениш одговарајућим
наредбама. Наравно, покушај задатак да решиш као прави
профи-програмер: писањем програмског кода, а не слагањем блокова!

Пребаци обе лоптице у рупу
''''''''''''''''''''''''''
.. level:: 2
   
.. questionnote::

   У овом задатку робот Карел има задатак да покупи обе лоптице и
   пребаци их у рупу (на њој пише колико лоптица треба да оставиш у
   рупу).

Помози сада роботу тако што ћеш попунити недостајућа места у коду.
   
.. karel:: Карел_пребаци_две_лоптице_1
   :blockly:

   {
      setup: function() {
	   var world = new World(3, 3);
           world.setRobotStartAvenue(3);
           world.setRobotStartStreet(3);
           world.setRobotStartDirection("E");
           world.putBall(1, 1);
           world.putBall(3, 1);
           world.putHoles(2, 2, 2);
           world.addNSWall(1, 1, 1);
           world.addNSWall(2, 1, 1);
           world.addEWWall(2, 1, 1);
           world.addEWWall(2, 2, 1);
           world.addNSWall(2, 3, 1);
           var robot = new Robot();
	   var code = ["from karel import *",

	   "desno(); napred(); napred();                    # idi do prve loptice",
	   "uzmi();                                         # uzmi je",
	   "???                                             # idi do rupe",
	   "ostavi();                                       # ostavi lopticu",
	   "???                                             # idi do druge loptice",
	   "???                                             # uzmi je",
	   "desno(); desno(); napred(); desno(); napred();  # idi do žutog polja",
	   "ostavi()                                        # ostavi lopticu"]
	   return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
           return world.getBalls(2, 2) == 0;
      }
   }

Понављање - бројачка петља `for`
--------------------------------

Често робот исту наредбу треба да понови више пута. Да би се такви
програми могли једноставније писати је коришћење **петљи**.

Иди 8 поља напред
'''''''''''''''''
.. level:: 1
           

.. questionnote::

   У наредном лавиринту постоји 8 поља испред робота. Коришћењем
   петље учини да робот дође до лоптице и да је затим покупи.

Један начин да решимо задатак је да роботу 8 пута задамо наредбу да
иде напред и затим наредбу да покупи лоптицу.
   
.. karel:: Карел_8_поља_напред
   :blockly:

   {
      setup: function() {
	   var world = new World(9, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
	   world.putBall(9, 1);
           var robot = new Robot();
	   var code = ["from karel import *",
	       "napred()", "napred()", "napred()", "napred()", "napred()", "napred()", "napred()", "napred()", "uzmi()"]
	   return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
           return robot.getStreet() === 1 &&
           robot.getAvenue() === 9 &&
	   world.getBalls(9, 1) == 0;
      }
   }


Замислимо колико би досадно било куцати десет или сто пута наредбу да
робот иде напред, када би лавиринт био већи. Пошто се у програмима
често јавља потреба да се неке наредбе понављају, сви програмски
језици обезбеђују начин да се то постигне. У програмском језику
Python, који наш робот Карел разуме, понављање се постиже коришћење
наредбе ``for``. Понављања у програмима се називају **циклуси** или
**петље** (по чему је наша фондација "Петља" добила име). Погледајмо
како се претходни програм може скратити употребом петље ``for``.

.. karel:: Карел_8_поља_напред_for
   :blockly:

   {
      setup: function() {
	   var world = new World(9, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
	   world.putBall(9, 1);
           var robot = new Robot();
	   var code = ["from karel import *",
	       "for i in range(8):", "    napred()", "uzmi()"]
	   return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
           return robot.getStreet() === 1 &&
           robot.getAvenue() === 9 &&
	   world.getBalls(9, 1) == 0;
      }
   }

Овде смо употребили петљу ``for i in range(n):`` која је уобичајени
начин да се изрази да се наредбе наведене у телу петље извршавају
``n`` пута (ми смо уместо ``n`` навели ``8``, чиме смо постигли то да
се наредба ``napred()`` изврши 8 пута). Овим смо дакле рекли "Понови
пет пута корак напред". Уместо ``i`` смо могли употребити и неко друго
слово или реч (или знак ``_``).

Наредбе које се понављају (за њих се каже да чине **тело** петље) се
обавезно морају увући у односу на наредбу ``for`` (обично помоћу
неколико размака, најчешће 4, или једног табулатора тј. карактера
*Tab* који се на тастатурама налази лево од тастера *Q*). Када се
петља заврши, извршава се наредба која је наведена иза петље и то
поравната са речју ``for`` (у претходном програму то је наредба
``uzmi()``).  Наредба ``uzmi()`` након петље ``for`` није увучена, што
значи да се она извршава само једном и то када се заврши извршавање
петље ``for`` тј. када се њено тело изврши одговарајући број
пута. Када би она била увучена и она би се понављала.

Неке честе грешке
'''''''''''''''''

Нагласимо да се на крају линије у којој се употребљава наредба ``for``
обавезно ставља двотачка (симбол ``:``). Ако се она не наведе добићеш
поруку о грешци

::

   SyntaxError: bad input on line ???

Ово значи ``Синтаксичка грешка: лош унос на линији ???`` - број линије
ти може указати на то где је грешка направљена (немој да заборавиш да
провериш и линију изнад те). Јако честа грешка програмера-почетника је
да забораве двотачку на крају наредбе ``for`` - обрати пажњу на тај
важан детаљ.

Ако заборавиш да увучеш тело петље, поново ћеш добити поруку

::

   SyntaxError: bad input on line ???

Још једна грешка која може наступити услед неодговарајућег увлачења
наредби је и

::
   
   IndentationError: unindent does not match any outer indentation level on line ???

На енглеском језику ``IndentationError`` значи *Грешка у
увлачењу*.


У складу са претходном дискусијом, исправи наредни програм.

.. karel:: Карел_8_поља_напред_for_грешке

   {
      setup: function() {
	   var world = new World(9, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
	   world.putBall(9, 1);
           var robot = new Robot();
	   var code = ["from karel import *",
	       "for i in range(8)", "napred()", " uzmi()"]
	   return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
           return robot.getStreet() === 1 &&
           robot.getAvenue() === 9 &&
	   world.getBalls(9, 1) == 0;
      }
   }


Петљама ћемо се много детаљније бавити у поглављу `Понављање
<Ponavljanje.html>`_.

Иди 7 поља напред
'''''''''''''''''
.. level:: 1

Пробај сада самостално да допуниш наредни програм тако да робот покупи
лоптицу. Не заборави да се пре петље окрене у правом смеру.

.. karel:: Карел_7_поља_напред
   :blockly:

   {
      setup: function() {
	   var world = new World(1, 8);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
	   world.putBall(1, 8);
           var robot = new Robot();
	   var code = ["from karel import *"]
	   return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
           return robot.getStreet() === 8 &&
           robot.getAvenue() === 1 &&
	   world.getBalls(1, 8) == 0;
      }
   }

.. reveal:: Карел_7_поља_напред_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   Карел треба прво да се окрене налево, затим да иде 7 пута напред и
   на крају да узме лоптицу. Прекопирај наредни код у претходни
   програм и испробај га.
   
   .. activecode:: Карел_7_поља_напред_решење
      :passivecode: true
   
      levo()
      for i in range(7):
         napred()
      uzmi()
      
Покупи 10 лоптица
'''''''''''''''''
.. level:: 1
   
.. questionnote::
   Испред робота се налази 10 лоптица. Напиши програм којим робот купи
   све те лоптице.
   
.. karel:: Карел_покупи_10_лоптица
   :blockly:

   {
      setup: function() {
	   var world = new World(2, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
	   world.putBalls(2, 1, 10);
           var robot = new Robot();
	   var code = ["from karel import *"]
	   return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
           return robot.getStreet() === 1 &&
           robot.getAvenue() === 2 &&
	   world.getBalls(2, 1) == 0;
      }
   }

*Савет*: употреби поново петљу ``for`` да се иста наредба не би
понављала пуно пута.

Покупи пет лоптица на пет поља испред
'''''''''''''''''''''''''''''''''''''
.. level:: 1
   
.. questionnote::

   Напиши програм у којем робот купи лоптице на пет поља испред себе.

.. karel:: Карел_покупи_5_лоптица_на_5_поља_испред
   :blockly:

   {
      setup: function() {
	   var world = new World(6, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
	   for (var i = 2; i <= 6; i++)
	      world.putBalls(i, 1, 1);
           var robot = new Robot();
	   var code = ["from karel import *",
	               "for i in range(5):",
		       "    napred()",
		       "    uzmi()"]
	   return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
           return robot.getStreet() === 1 &&
           robot.getAvenue() === 6 &&
	   robot.getBalls() === 5;
      }
   }
   
Приметимо да су у овом програму две наредбе робота понављале пет пута
(наредба ``napred()`` и наредба ``uzmi()``) и да су обе биле увучене
по 4 карактера. Пробај сада да наредиш роботу да се врати на почетно
поље када покупи лоптице.

.. karel:: Карел_покупи_5_лоптица_на_5_поља_испред_и_врати_се
   :blockly:

   {
      setup: function() {
	   var world = new World(6, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
	   for (var i = 2; i <= 6; i++)
	      world.putBalls(i, 1, 1);
           var robot = new Robot();
	   var code = ["from karel import *",
	               "for i in range(5):",
		       "    napred()",
		       "    uzmi()",
		       "???  # dopuni ovde kod"]
	   return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
           return robot.getStreet() === 1 &&
           robot.getAvenue() === 1 &&
	   robot.getBalls() === 5;
      }
   }


На крају, модификуј програм тако да робот док се враћа оставља по
једну лопту на сваком пољу, тако да распоред лоптица буде исти као и
на почетку.

.. karel:: Карел_покупи_5_лоптица_на_5_поља_испред_и_врати_се_остављајући_лоптице
   :blockly:

   {
      setup: function() {
	   var world = new World(6, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
	   for (var i = 2; i <= 6; i++)
	      world.putBalls(i, 1, 1);
           var robot = new Robot();
	   var code = ["from karel import *",
	               "for i in range(5):",
		       "    napred()",
		       "    uzmi()",
		       "???  # dopuni ovde kod"]
	   return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
           for (var i = 2; i <= 6; i++)
               if (world.getBalls(i, 1) != 1)
                 return false;
           return robot.getStreet() === 1 &&
                  robot.getAvenue() === 1 &&
   	          robot.getBalls() === 0;
      }
   }

   
Претходни садржај можеш погледати и у наредној видео-лекцији.

.. ytpopup:: Txibc29OzmQ
      :width: 735
      :height: 415
      :align: center

Покупи по три лоптице на пет поља испред
''''''''''''''''''''''''''''''''''''''''
.. level:: 2

.. questionnote::

   На сваком од пет поља испред робота налазе се по три
   лоптице. Напиши програм на основу којег робот купи све те лоптице.

   
.. karel:: Карел_покупи_по_3_лоптице_на_5_поља_испред
   :blockly:

   {
      setup: function() {
	   var world = new World(6, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
	   for (var i = 2; i <= 6; i++)
	      world.putBalls(i, 1, 3);
           var robot = new Robot();
	   var code = ["from karel import *",
	               "for i in range(5):",
		       "    napred()",
		       "    for j in range(3):",
		       "        uzmi()"]
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

Приметимо да се у претходном програму петља ``for`` налази у телу
петље ``for``. Такве се петље називају **угнежђене петље**. Приметимо
да смо у њима морали употребити различита слова (у спољној смо
употребили ``i``, а у унутрашњој ``j``). Више детаља о овоме биће у
наредним поглављима.

Претходни садржај можеш погледати и у наредној видео-лекцији.

.. ytpopup:: fEzQrKjTHzY
      :width: 735
      :height: 415
      :align: center


Домаћи задатак
--------------

Пребаци обе лоптице у рупу
''''''''''''''''''''''''''
.. level:: 2

.. questionnote::

   Задатак је исти као мало пре, једино се лавиринт мало
   променио. Потребно је да робот пребаци обе лоптице у рупу.

.. karel:: Карел_пребаци_две_лоптице_2
   :blockly:

   {
        setup:function() {
            var world = new World(5,5);
            world.setRobotStartAvenue(5);
            world.setRobotStartStreet(5);
            world.setRobotStartDirection("W");
            world.putBall(3, 3);
            world.putBall(1, 2);
            world.putHoles(5, 1, 2);
	    
	    world.addEWWall(2, 4, 1);
 	    world.addEWWall(2, 3, 1);
 	    world.addNSWall(1, 4, 1);
 	    world.addNSWall(2, 4, 1);

	    world.addEWWall(2, 2, 1);
 	    world.addEWWall(2, 1, 1);
 	    world.addNSWall(1, 2, 1);
 	    world.addNSWall(2, 2, 1);

	    world.addEWWall(4, 4, 2);
	    world.addNSWall(3, 2, 3);
	    world.addEWWall(4, 1, 2);
	
 	    var robot = new Robot();

	    var code = ["from karel import *",
	                "??? # idi do prve loptice i uzmi je",
			"??? # idi do druge loptice i uzmi je",
			"??? # idi do rupe i ostavi obe loptice"];
            return {robot:robot, world:world, code:code};
        },
	
        isSuccess: function(robot, world) {
           return world.getBalls(5, 1) == 0;
        }
   }

.. reveal:: Карел_пребаци_две_лоптице_2_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   Једно могуће решење (не и једино) је следеће.	       

   .. activecode:: Карел_пребаци_две_лоптице_2_решење
      :passivecode: true
		    
      from karel import *
      # idi do prve loptice i uzmi je
      napred()
      napred()
      levo()
      napred()
      napred()
      uzmi()
      # idi do druge loptice i uzmi je
      desno()
      napred()
      napred()
      levo()
      napred()
      uzmi()
      # idi do rupe i ostavi loptice
      napred()
      levo()
      napred()
      napred()
      napred()
      napred()
      ostavi()
      ostavi()


Размакнуте лоптице
''''''''''''''''''
.. level:: 2

.. questionnote::

   Помози роботу да покупи три лоптице испред себе. Напиши програм без
   петље и програм са петљом.


.. karel:: Карел_размакнуте_лоптице
  :blockly:

   {
     setup: function() {
        var world = new World(7, 1);
        world.setRobotStartAvenue(1);
        world.setRobotStartStreet(1);
        world.setRobotStartDirection("E");

        world.putBall(3, 1);
        world.putBall(5, 1);
        world.putBall(7, 1);

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
          
.. reveal:: Карел_размакнуте_лоптице_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење
 
   Једно могуће решење са петљом (не и једино) је следеће.               
 
   .. activecode:: Карел_размакнуте_лоптице_решење
      :passivecode: true
                    
      from karel import *
      for i in range(3):
          napred()
          napred()
          uzmi()

      
