Бројачка петља ``for``
----------------------

Често робот исту наредбу треба да понови више пута. Такви програми се
једноставније могу писати коришћењем **петљи**.

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
           robot.getAvenue() === 6 &&
       world.getBalls(6, 1) == 0;
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

Прочитај сада у `приручнику
<https://www.petlja.org/biblioteka/r/lekcije/prirucnik-python-gim/karel-cas1#id13>`__
детаљно објашњење овог програма и детаљно објашњење петље ``for``.

Увежбај сада петљу ``for`` тако што ћеш урадити наредна три задатка из
приручника.

- `Иди 7 поља напред <https://www.petlja.org/biblioteka/r/lekcije/prirucnik-python-gim/karel-cas1#id19>`__
- `Покупи 10 лоптица <https://www.petlja.org/biblioteka/r/lekcije/prirucnik-python-gim/karel-cas1#id22>`__
- `Покупи пет лоптица на пет поља испред <https://www.petlja.org/biblioteka/r/lekcije/prirucnik-python-gim/karel-cas1#id24>`__

Детаљна објашњења ова три задатка можеш погледати у наредној
видео-лекцији.
  
.. ytpopup:: Txibc29OzmQ
      :width: 735
      :height: 415
      :align: center

  
Петља може бити део тела петље. Такве се петље називају **угнежђене**
петље. Употреби угнежђене петље у решењу наредног задатка из
приручника.

- `Покупи по три лоптице на пет поља испред
  <https://www.petlja.org/biblioteka/r/lekcije/prirucnik-python-gim/karel-cas1#id28>`__

Решење овог задатка можеш погледати у наредној видео-лекцији.

.. ytpopup:: fEzQrKjTHzY
      :width: 735
      :height: 415
      :align: center
  
