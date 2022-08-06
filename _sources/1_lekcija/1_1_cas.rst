1.1. Линијски програми
####################################

.. questionnote::
   Сећате ли се робота Карела и његових задатака са лоптицама у лавиринту?

Хајде на почетку мало да се играмо и тако присетимо 6. разреда и неких
основних појмова програмирања. Одличан начин за то је писање програма
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
присетимо се неколико основних наредби тог језика. 

.. technicalnote::
   Испрограмирали смо га тако да ради унутар прегледача веба и не мораш ништа додатно да
   инсталираш да би писао програме за Карела. 

Линијски програми
-----------------
  
Прикажимо употребу ових наредби на неколико једноставних програма.

Иди до лоптице и узми је
''''''''''''''''''''''''
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


Програмирање слагањем блокова
'''''''''''''''''''''''''''''

Пошто претпостављамо да већ познајеш програмирање уз помоћ слагања
блокова из основне школе(на пример у програму MIT Scratch или на сајту `code.org
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
наредбама. 

.. suggestionnote::
   Наравно, покушај задатак да решиш као прави
   профи-програмер: писањем програмског кода, а не слагањем блокова!
