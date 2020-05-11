====================
Робот Карел - увод
====================

Хајде да се упознамо са роботом који се зове Карел. Карел живи у
лавиринту и твој задатак је да му помогнеш да се успешно креће кроз
лавиринт. Робот разуме посебан језик који је креиран специјално за
њега, а на теби је да постепено усвајаш елементе овог језика и
описујеш кораке којима Карел може успешно да савлада пролазак кроз
лавиринт.

На наредној слици можеш да видиш како изгледа један од лавирината и
Карела у њему.

.. image:: ../_images/karel1.png      
   :align: center


Робот Карел се налази у лавиринту и разуме наредне наредбе

- ``napred()`` - помери се једно поље напред,
- ``levo()`` - окрени се 90 степени налево (у смеру супротном казаљки на сату),
- ``desno()`` - окрени се 90 степени надесно (у смеру казаљке на сату),
- ``uzmi()`` - покупи лоптицу са поља на којем се налазиш,
- ``ostavi()`` - спусти лоптицу на поље на којем се налазиш

Проласком кроз `лекцију у приручнику
<https://www.petlja.org/biblioteka/r/lekcije/prirucnik-python-gim/karel-cas1>`__
научићеш како коришћењем ових наредби можеш Карела научити да решава
неке интересантне проблеме. У наставку ћемо ти приказати њене
најзначајније делове на које треба посебно да обратиш пажњу.

Линијски програми
-----------------

Линијски програми су они који су представљени низом наредби које се
извршавају редом, једна за другом. На пример, наредни задатак се
решава једним једноставним линијским програмом.

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

Прочитај сада текст у `приручнику
<https://www.petlja.org/biblioteka/r/lekcije/prirucnik-python-gim/karel-cas1#id4>`__
у ком се детаљније описује овај програм. Можеш погледати и наредну
видео-лекцију у којој се описује решење овог задатка и концепти
програмског језика Пајтон који се у његовом решењу користе.


.. ytpopup:: s9KCMku_StY
      :width: 735
      :height: 415
      :align: center

Сада уради наредна два задатка из приручника:

- `Пребаци лоптицу на поље (3, 5) <https://www.petlja.org/biblioteka/r/lekcije/prirucnik-python-gim/karel-cas1#id9>`__
- `Пребаци обе лоптице у рупу <https://www.petlja.org/biblioteka/r/lekcije/prirucnik-python-gim/karel-cas1#id11>`__

