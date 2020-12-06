3.1. Робот Карел - задаци за вежбање
####################################

Током претходна два часа упознали смо се са Карелом и наредбама које
он "разуме". Сада је време да продубимо и проверимо знање. Најбољи
начин да то и учинимо јесте да решимо још неколико задатака.


Пребаци пет лоптица у рупу
''''''''''''''''''''''''''

.. questionnote::

   Помози роботу да покупи свих пет лоптица и премести у рупу испред
   њих.

.. karel:: Карел_пребаци_свих_пет_лоптица_у_рупу
    :blockly:

    {
      setup: function() {

         var world = new World(3, 1);
         world.setRobotStartAvenue(3);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("W");

         world.putBalls(2, 1, 5);
         world.putHoles(1, 1, 5);

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

    
.. reveal:: Карел_пребаци_свих_пет_лоптица_у_рупу_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   Једно могуће решење (не и једино) је следеће.               

   .. activecode:: Карел_пребаци_свих_пет_лоптица_у_рупу_решење
      :passivecode: true
   
      from karel import *
      napred()
      for j in range(5):
          uzmi()
      napred()
      for j in range(5):
          ostavi()

Покупи лоптице са наредна три поља
''''''''''''''''''''''''''''''''''

.. questionnote::

   Испред Карела су три поља, а на њима редом 5, 3 и 8 лоптица. Карел
   треба да покупи све лоптице.

  
.. karel:: Karel_for_Take_5_3_8
   :blockly:

   {
        setup:function() {
           var world = new World(4, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           
           world.putBalls(2, 1, 5);
           world.putBalls(3, 1, 3);
           world.putBalls(4, 1, 8);
           
           var robot = new Robot();

           var code = ["from karel import *",
                       "# dovrsi program",
                       ""];
           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() == 16;
        },
   }
   
.. reveal:: Karel_for_Take_5_3_8_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење
   
   .. activecode:: Karel_for_Take_5_3_8_solution
      :passivecode: true
      
      from karel import *
      napred()
      for i in range(5):
          uzmi()
      napred()
      for i in range(3):
          uzmi()
      napred()
      for i in range(8):
          uzmi()
          

Победничко постоље
''''''''''''''''''

.. questionnote::

   Помози роботу да покупи све лоптице.

   
.. karel:: Карел_победничко_постоље
    :blockly:

    {
        setup: function() {
            var dim = 5;
            var world = new World(2*dim + 1, dim + 2);
        for (var i = 1; i <= dim; i++)
                world.addNSWall(i, i, 1);
        for (var i = dim + 1; i <= 2 * dim; i++)
                world.addNSWall(i, 2*dim - i + 1, 1);
        for (var i = 1; i <= dim; i++)
                world.addEWWall(i + 1, i, 1);
        for (var i = dim; i <= 2*dim - 1; i++)
                world.addEWWall(i + 1, 2*dim - i, 1);
            for (var i = 2; i <= dim; i++)
                world.putBall(i, i);
        for (var i = dim + 1; i <= 2*dim + 1; i++)
                world.putBall(i, 2*dim - i + 2);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
        world.setRobotStartDirection("E");
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


.. reveal:: Карел_победничко_постоље_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   Једно могуће решење (не и једино) је следеће.               

   .. activecode:: Карел_победничко_постоље_решење
      :passivecode: true
                    
      from karel import *
      for i in range(5):
          levo()
          napred()
          desno()
          napred()
          uzmi()
      for i in range(5):
          napred()
          desno()
          napred()
          uzmi()
          levo()

Петља ``while``
---------------
          
Степенице
'''''''''

.. questionnote::

   Помози роботу да покупи све лоптице. Лавиринт је зачаран и број
   степеница се мења приликом сваког покретања програма.
   
.. karel:: Карел_степенице
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
        world.setRobotStartDirection("E");

        for (var i = 2; i <= N; i++) {
           world.putBall(i, N-i+1);
           world.addNSWall(i-1, N-i+1, 1);
           world.addEWWall(i-1, N-i+1, 1);
        }

        for (var i = 2; i <= N-1; i++)
           world.addNSWall(i, N-i+2, 1);
        for (var i = 2; i <= N; i++)
           world.addEWWall(i, N-i+2, 1);

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

.. reveal:: Карел_степенице_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   Једно могуће решење (не и једино) је следеће.               

   .. activecode:: Карел_степенице_решење
      :passivecode: true
                    
      from karel import *
      while moze_napred():
          napred()
          desno()
          napred()
          uzmi()
          levo()

Гранање
-------

Донеси све лоптице
''''''''''''''''''


.. questionnote::

   Испред Карела је прав пут непознате дужине. На неким пољима има, а
   на неким нема лоптице. Карел треба да прикупи све лоптице са свих
   поља и донесе их на почетно поље.

Задатак је делимично решен, додај део који недостаје.

.. karel:: Karel_while_bring_all_balls
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var N = 2 + random(9);
         var world = new World(N, 1);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
         
         for (var k = 2; k <= N; k++) {
            let B = random(2);
            world.putBalls(k, 1, B);
         }
      
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "while moze_napred():",
                     "    napred()",
                     "    # kazi Karelu da uzme lopticu sa polja, ako je ima",
                     "",
                     "levo(); levo()                # okreni se nazad",
                     "# kazi Karelu da se vrati na pocetno polje (to jest, da ide napred dok moze)",
                     "",
                     "while ima_loptica_kod_sebe(): # ostavi sve loptice",
                     "    ostavi()",
                     ""];

           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           var N = world.getAvenues();
           for (var k = 2; k <= N; k++)
              if (world.getBalls(k, 1) > 0)
                 return false;
               
           if (robot.getBalls() > 0)
                 return false;
                 
           return true;
        },
   }

.. reveal:: Karel_while_if_bring_all_balls_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_while_if_bring_all_balls_solution
      :passivecode: true
      
      from karel import *
      while moze_napred():          # pokupi sve loptice sa svih polja
          napred()
          if ima_loptica_na_polju():
              uzmi()
            
      levo(); levo()                # okreni se nazad
      
      while moze_napred():          # vrati se na pocetno polje
          napred()
      while ima_loptica_kod_sebe(): # ostavi sve loptice           
          ostavi()
          


Угнежђене петље
---------------

Премести све лоптице у рупе (3x3)
'''''''''''''''''''''''''''''''''

.. questionnote::

   Помози роботу да покупи све лоптице премести у рупе испред
   њих. Лавиринт је увек исти (на три поља испред робота се налази по
   три лоптице).
   
.. karel:: Карел_све_лоптице_у_рупе_3x3
    :blockly:

    {
      setup: function() {

         function random(n) {
             return Math.floor(n * Math.random());
         }
      
         var N = 7;
         var world = new World(N, 1);
         world.setRobotStartAvenue(N);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("W");

         for (var i = N-1; i >= 1; i--)
            if (i % 2 == 0)
               world.putBalls(i, 1, 3);
            else
               world.putHoles(i, 1, 3);

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


.. reveal:: Карел_све_лоптице_у_рупе_3x3_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   Једно могуће решење (не и једино) је следеће.               

   .. activecode:: Карел_све_лоптице_у_рупе_3x3_решење
      :passivecode: true
   
      from karel import *
      for i in range(3):
          napred()
          for j in range(3):
              uzmi()
          napred()
          for j in range(3):
              ostavi()

Пребаци све лоптице у рупе
''''''''''''''''''''''''''

.. questionnote::

   Помози роботу да покупи све лоптице премести у рупе испред
   њих. Разлика у односу на претходни задатак је то што је лавиринт
   зачаран и робот не зна унапред колико ће лоптица бити испред њега.
   
.. karel:: Карел_све_лоптице_у_рупе
    :blockly:

    {
      setup: function() {

         function random(n) {
             return Math.floor(n * Math.random());
         }
      
         var N = 2 * (2 + random(3)) + 1;
         var world = new World(N, 1);
         world.setRobotStartAvenue(N);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("W");

         var m;
         for (var i = N-1; i >= 1; i--) {
            if (i % 2 == 0) {
              m = 2 + random(3);
               world.putBalls(i, 1, m);
            } else
               world.putHoles(i, 1, m);
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

.. reveal:: Карел_све_лоптице_у_рупе_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   Једно могуће решење (не и једино) је следеће.               

   .. activecode:: Карел_све_лоптице_у_рупе_решење
      :passivecode: true
   
      from karel import *
      while moze_napred():
          napred()
          while ima_loptica_na_polju():
              uzmi()
          napred()
          while ima_loptica_kod_sebe():
              ostavi()

Узимај по четири лоптице до краја
'''''''''''''''''''''''''''''''''

.. questionnote::

   Испред Карела је једно или више поља, а на сваком пољу су по четири
   лоптице. Карел треба све да их покупи.
  
Сада Карел, све док не дође до зида, треба да понавља корак напред и
узимање 4 лоптице. Покушај да допуниш програм.
  
.. karel:: Karel_while_many_squares_two_bals_per_square
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var N = 2 + random(9);
         var world = new World(N, 1);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
         for (var k = 2; k <= N; k++)
             world.putBalls(k, 1, 4);
      
         var robot = new Robot();
      
         var code = ["from karel import *",
                     "while moze_napred():",
                     "    napred()",
                     "    # dodajte naredbe koje nedostaju",
                     ""];
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         var N = world.getAvenues();
         for (var k = 1; k <= N; k++)
            if (world.getBalls(k, 1) > 0)
               return false;
               
         return true;
      }
   }
   
.. reveal:: Karel_while_many_squares_two_bals_per_square_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_while_many_squares_two_bals_per_square_solution
      :passivecode: true
      
      from karel import *
      while moze_napred():
          napred()
          for i in range(4):
              uzmi()

Покупи све лоптице
''''''''''''''''''

.. questionnote::

   Испред Карела је бар једно поље, а може их бити било колико. На
   сваком од поља испред Карела има нула или више лоптица. Карел треба
   да покупи све лоптице.


.. karel:: Karel_while_many_squares_many_balls
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var N = 2 + random(9);
         var world = new World(N, 1);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
         
         for (var k = 2; k <= N; k++) {
            let B = random(7);
            world.putBalls(k, 1, B);
         }
      
         var robot = new Robot();
      
         var code = ["from karel import *",
                     "while ???:",
                     "    napred()",
                     "    while ???:",
                     "        ???",
                     ""];
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         var N = world.getAvenues();
         for (var k = 1; k <= N; k++)
            if (world.getBalls(k, 1) > 0)
               return false;
               
         return true;
      }
   }              

.. reveal:: Karel_while_many_squares_many_balls_per_square_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_while_many_squares_many_balls_per_square_solution
      :passivecode: true
      
      from karel import *
      while moze_napred():
          napred()
          while ima_loptica_na_polju():
              uzmi()
              
Пун лавиринт лоптица
''''''''''''''''''''

.. questionnote::

   Помози роботу да постави лоптице дуж целог лавиринта.

   
.. karel:: Карел_пун_лавиринт_лоптица
    :blockly:
   
    {
        setup: function() {

           function random(n) {
             return Math.floor(n * Math.random());
           }
        
           var dim = 5 + random(3);
           var world = new World(dim, dim);

           world.addNSWall(1, 2, dim-2);
           world.addNSWall(dim-1, 2, dim-2);
           world.addEWWall(2, 1, dim-2);
           world.addEWWall(2, dim-1, dim-2);

           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("N");
           var robot = new Robot();
           robot.setInfiniteBalls(true);
           var code = ["from karel import *"]
           return {world: world, robot: robot, code: code};
        },

        isSuccess: function(robot, world) {
            for (var i = 1; i <= world.getStreets(); i++) {
                    if (world.getBalls(1, i) != 1)
                    return false;
                    if (world.getBalls(world.getAvenues(), i) != 1)
                    return false;
            }

            for (var i = 1; i <= world.getAvenues(); i++) {
                    if (world.getBalls(i, 1) != 1)
                    return false;
                    if (world.getBalls(i, world.getStreets()) != 1)
                    return false;
            }     

            return true;
        }
    }

.. reveal:: Карел_пун_лавиринт_лоптица_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   Једно могуће решење (не и једино) је следеће.               

   .. activecode:: Карел_пун_лавиринт_лоптица_решење
      :passivecode: true

      from karel import *
      for i in range(4):
          while moze_napred():
              napred()
              ostavi()
          desno()

              


