Петља ``while``
===============

Упознаo/упознала си се већ са условном петљом, тј. петљом код које се услов проверава на почетку. 
Можеш се подсети свих детаља `овде <https://petlja.org/biblioteka/r/lekcije/prirucnik-python/karel-cas2#while>`__.

.. activecode:: Наредба `while`
   :passivecode: true

   while uslov:
       naredba1()
       naredba2()
       ...
       naredbak()


Када је потребно у задатку се позвати на понављање, али тако да не знамо унапред, колико пута ће се нешто поновити, користимо петљу ``while``. Карактеристично за 
``while`` петљу је да се услов проверава на почетку. Све док је услов који је дат на почетку испуњен, понављаће се наредба или наредбе које се налазе у телу петље.

У наредном примеру погледај и подсети се како се ова петља може употребити:

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

Запамти, ову пељу користимо када су лавиринти "зачарани", тј. када се лавиринт на свако покретање програма мења (мења своју димензију или мења број лоптица које се налазе у њему).
Запамти, ``while`` значи док. У преходном програму смо, дакле, роботу
рекли следеће: "Док можеш да идеш напред иди напред. Узми лоптицу."

Приметимо и да се након услова петље ``while`` наводи двотачка, док се
наредбе које се понављају увлаче (веома слично као што је био случај и
код петље ``for``). И поруке о грешкама уколико се то не испоштује су
сличне.

У наставку се налази видео који можеш да погледаш у вези са петљом `while`. Наредни `линк <https://petlja.org/biblioteka/r/lekcije/prirucnik-python-gim/karel-cas2#whiles>`__ ће ти помоћи да одеш на Приручник и још једном прочиташ све потребно у вези за овом петљом.

.. ytpopup:: Zk-4gG4iZmc
      :width: 735
      :height: 415
      :align: center
