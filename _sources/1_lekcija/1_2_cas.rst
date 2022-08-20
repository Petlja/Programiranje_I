1.2. Бројачка петља `for`
#######################################

Често робот исту наредбу треба да понови више пута. Да би се такви
програми могли једноставније писати је коришћење **петљи**. У наставку 
присетимо се **бројачке петље**.


Иди 8 поља напред
'''''''''''''''''

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

.. infonote::
   **Важна напомена:** Приметимо да је наредба ``napred()`` увучена. 
   То значи да она припада петљи ``for``. Наредба ``uzmi()`` није увучена,
   што значи да она не припада петљи ``for``.

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
осам пута корак напред". 

Да смо уместо 8 ставили неки други број, на пример 5, робот би корачао напред
пет пута.

Уместо ``i`` смо могли употребити и неко друго
слово или реч (или знак ``_``).

Наредбе које се понављају (за њих се каже да чине **тело** петље) се
обавезно морају увући у односу на наредбу ``for`` (обично помоћу
неколико размака, најчешће 4, или једног табулатора тј. карактера
*Tab* који се на тастатурама налази лево од тастера *Q*). Када се
петља заврши, извршава се наредба која је наведена иза петље и то
поравната са речју ``for`` (у претходном програму то је наредба
``uzmi()``).  

Наредба ``uzmi()`` након петље ``for`` није увучена и због тога не
припада петљи, што
значи да се она извршава само једном и то када се заврши извршавање
петље ``for`` тј. када се њено тело изврши одговарајући број
пута. Када би она била увучена и она би се понављала јер би тада припадала телу петље.

Неке честе грешке
'''''''''''''''''

Нагласимо да се на крају линије у којој се употребљава наредба ``for``
обавезно ставља двотачка (симбол ``:``). Ако се она не наведе добићеш
поруку о грешци:

::

   SyntaxError: bad input on line ???

Ово значи ``Синтаксичка грешка: лош унос на линији ???`` - број линије
ти може указати на то где је грешка направљена (немој да заборавиш да
провериш и линију изнад те). Јако честа грешка програмера-почетника је
да забораве двотачку на крају наредбе ``for`` - обрати пажњу на тај
важан детаљ.

Ако заборавиш да увучеш тело петље, поново ћеш добити поруку:

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
      
