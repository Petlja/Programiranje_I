Робот Карел - Додатни задаци за вежбу
#####################################

Задаци
------

Помери све лоптице уназад
'''''''''''''''''''''''''
.. level:: 2

.. questionnote::

   Испред Карела је прав пут непознате дужине. На почетном пољу нема
   лоптица. Карел треба да сваку лоптицу премести за једно поље ка
   левој страни екрана.
  
Овај задатак можемо да решимо и без употребе наредбе ``if``. На пример,
можемо да док год има поља испред Карела, понављамо следеће кораке:

- пређи на следеће поље
- узми све лоптице са тог поља
- иди корак назад (то јест, окрени се два пута и иди напред)
- остави све лоптице
- врати се на поље са којег си узео лоптице

Овакво решење је дато као почетно у прозору испод. Пратећи дати
програм, Карел ће се чак и кад не узме ни једну лоптицу враћати на
претходно поље. Можеш ли да убациш једну наредбу ``if`` у програм,
тако да се Карел не враћа ако није узео ни једну лоптицу? Наравно,
биће потребно да се неке дате наредбе увуку у тело наредбе ``if``.

.. karel:: Karel_if_all_balls_one_square_left
   :blockly:

   {
        setup:function() {
           function random(n) {
              return Math.floor(n * Math.random());
           }
           var choice = random(3); // need initial world to get rid of 'choice'
           var N = [3, 4, 5];
           var world = new World(N[choice], 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           
           var B = 0;
           if (Math.random() > 0.8) B = random(3);
           if (choice == 0) {
              world.putBalls(2, 1, B);
              world.putBalls(3, 1, B + 2);
           }
           if (choice == 1) {
              world.putBalls(2, 1, B);
              world.putBalls(3, 1, B + 3);
              world.putBalls(4, 1, B + 1);
           }
           if (choice == 2) {
              world.putBalls(2, 1, B);
              world.putBalls(3, 1, B + 4);
              world.putBalls(4, 1, B + 1);
              world.putBalls(5, 1, B + 3);
           }

           var robot = new Robot();

           var code = ["from karel import *",
                       "while moze_napred():             # dok ima polja ispred Karela, ponavljaj",
                       "    napred();                        # idi napred",
                       "    while ima_loptica_na_polju():    # pokupi sve loptice sa polja",
                       "        uzmi()",                        
                       "    levo(); levo(); napred()         # idi jedno polje nazad",
                       "    while ima_loptica_kod_sebe():    # ostavi sve loptice",
                       "        ostavi()",                      
                       "    levo(); levo(); napred()         # vrati se jedno polje napred",
                       ""];
                       
           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           var N = world.getAvenues();
           var B = world.getBalls(1, 1);
           if (N == 3) {
              if (world.getBalls(2, 1) != B + 2)
                return false;              
           }
           if (N == 4) {
              if (world.getBalls(2, 1) != B + 3)
                return false;
              if (world.getBalls(3, 1) != B + 1)
                return false;              
           }
           if (N == 5) {
              if (world.getBalls(2, 1) != B + 4)
                return false;
              if (world.getBalls(3, 1) != B + 1)
                return false;
              if (world.getBalls(4, 1) != B + 3)
                return false;
           }
           
           if (world.getBalls(N, 1) != 0) 
              return false;

           if (robot.getBalls() > 0)
                 return false;
                 
           return true;
        },
   }
   
.. reveal:: Karel_if_all_balls_one_square_left_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_if_all_balls_one_square_left_solution
      :passivecode: true
      
      from karel import *
      while moze_napred():                  # dok ima polja ispred Karela, ponavljaj
          napred();                         #     idi napred
          if ima_loptica_na_polju():
              while ima_loptica_na_polju(): #     pokupi sve loptice sa polja
                  uzmi()
              levo(); levo(); napred()      #     idi jedno polje nazad
              while ima_loptica_kod_sebe(): #     ostavi sve loptice
                  ostavi()
              levo(); levo(); napred()      #     vrati se jedno polje napred


Три пута горе-доле
''''''''''''''''''
.. level:: 2

.. questionnote::

   Карел се налази на правоугаоној табли од 5 редова и 7 колона и
   треба да стигне до доњег десног поља.


Карел треба три пута да понови једну сложену радњу, а то је: да пређе
у следећу (десну) колону, оде до њеног врха, оде још једну колону
десно, сиђе до првог реда и на крају да се окрене ка последњој колони
да би се припремио за следеће понављање.

Допуни програм, водећи рачуна да се бројач у *for* наредбама које
додајеш не зове ``i`` (то име је већ употребљено у спољној петљи).

.. karel:: Karel_for_up_col_down_col_constant
   :blockly:

   {
      setup:function() {

         var X2 = 3;
         var Y = 5;
         var world = new World(2*X2+1, Y);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
            
         world.addEWWall(1, 1, 1);
         for (let x = 0; x < X2; x++) { 
            world.addNSWall(2*x + 1, 2, Y - 1);
            world.addNSWall(2*x + 2, 1, Y - 1);
         }
         
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "for i in range(3):              # tri puta ponovi sve sto sledi",
                     "    napred(); levo()             #    udji u sledecu kolonu i okreni se na sever",
                     "    # upotrebite for naredbu da kazete Karelu da ode do gornje ivice",
                     "    ",
                     "    desno(); napred(); desno()   #    predji u sledecu kolonu i okreni se na jug",
                     "    # upotrebite for naredbu da kazete Karelu da ode do donje ivice",
                     "    ",
                     "    levo()                       #    okreni se na istok",
                     ""];
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return robot.getAvenue() == world.getAvenues() &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_for_up_col_down_col_constant_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_for_up_col_down_col_constant_solution
      :passivecode: true
      
      from karel import *
      for i_vodoravno in range(3):     # 3 puta ponovi sve sto sledi
          napred(); levo()             #     udji u sledecu kolonu i okreni se na sever
          for i_uspravno in range(4):  #     idi do gornje ivice
              napred()

          desno(); napred(); desno()   #     predji u sledecu kolonu i okreni se na jug
          for i_uspravno in range(4):  #     idi do donje ivice
              napred()

          levo()                       #     okreni se na istok

Горе-доле
'''''''''
.. level:: 2

.. questionnote::

   Карел се налази на правоугаоној табли непознате величине (број
   колона је увек непаран), без лоптица. Циљ је да Карел стигне до
   доњег десног поља, а да би то постигао, мораће да се креће кроз
   колоне наизменично горе-доле.

.. karel:: Karel_while_up_col_down_col
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var X2 = 1 + random(4);
         var Y = 2 + random(5);
         var world = new World(2*X2+1, Y);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
            
         world.addEWWall(1, 1, 1);
         for (let x = 0; x < X2; x++) { 
            world.addNSWall(2*x + 1, 2, Y - 1);
            world.addNSWall(2*x + 2, 1, Y - 1);
         }
         
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "# dodajte naredbe ",
                     ""];
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return robot.getAvenue() == world.getAvenues() &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_while_up_col_down_col_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_while_up_col_down_col_solution
      :passivecode: true
      
      from karel import *
      while moze_napred():           # dok nismo u donjem desnom uglu
          napred(); levo()           #     udji u sledecu kolonu i okreni se na sever
          while moze_napred():       #     idi do gornje ivice
              napred()

          desno(); napred(); desno() #     predji u sledecu kolonu i okreni se na jug
          while moze_napred():       #     idi do donje ivice
              napred()

          levo()                     #     okreni se na istok


          
Донеси све са табле
'''''''''''''''''''
.. level:: 2

.. questionnote::

  Карел треба да донесе свих 12 лоптица на полазно поље.


Карел треба четири пута да пређе у следећу колону и испразни је, а на
крају да дође на полазно поље и остави све лоптице. Карел ће
испразнити колону ако три пута понови корак напред и узимање, а затим
се врати на почетак колоне у исти положај.

Допуни програм.

.. karel:: Karel_for_fetch_from_matrix
   :blockly:

   {
      setup:function() {
         var X = 5;
         var Y = 4;
         var world = new World(X, Y);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");

         world.addEWWall(1, 1, 1);
         world.addNSWall(1, 2, Y - 1);
         
         for (var col = 2; col <= X; col++) {
            for (var row = 2; row <= Y; row++) {
               world.putBall(col, row);
            }
         }
         
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "for i_kolona in range(4):      # cetiri puta ponovi ciscenje kolone",
                     "    napred()                   #     udji u sledecu kolonu",
                     "    levo()                     #     okreni se na sever",
                     "    #for ...                   #     3 puta ponovi korak napred i uzimanje",
                     "",
                     "    desno(); desno()           #     okreni se na jug",
                     "    #for ...                   #     3 koraka napred do donje ivice",
                     "",
                     "    levo()                     #     okreni se na istok",
                     "    ",
                     "                               # sada smo prosli sva polja",
                     "levo()                         #     okreni se na zapad",
                     "levo()",
                     "#for ...                       # vrati se na pocetno polje",
                     "    ",
                     "for i_loptica in range(12):",
                     "    ostavi()",
                     ""];
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return world.getBalls(1, 1) == 12 &&
            robot.getAvenue() == 1 &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_for_fetch_from_matrix_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_for_fetch_from_matrix_solution
      :passivecode: true
      
      from karel import *
      for i_kolona in range(4):     # cetiri puta ponovi ciscenje kolone
          napred()                  #     udji u sledecu kolonu
          levo()                    #     okreni se na sever
          for i_red in range(3):    #     idi do gornje ivice i usput pokupi
              napred()
              uzmi()

          desno(); desno()          #     okreni se na jug
          for i_red in range(3):    #     idi do donje ivice
              napred()

          levo()                    #     okreni se na istok
         
      levo()                        # okreni se na zapad
      levo()
      for i_kolona in range(4):     # vrati se na pocetno polje
          napred()
         
      for i_loptica in range(12):   # ostavi sve loptice
          ostavi()


Донеси свих 60
''''''''''''''
.. level:: 3

.. questionnote::

   Сада се на сваком од истих 12 поља као у претходном задатку налази
   по 5 лоптица. Карел треба да донесе свих 60 лоптица на полазно
   поље.


Овај програм се од претходног разликује по томе што наредба *uzmi()*
треба да стоји у додатној петљи, трећој у дубину. Такође, разликује се
и број лоптица које Карел на крају програма оставља на полазно
поље. Покушај да ископираш претходни програм и преправиш га.

.. karel:: Karel_for_fetch_60_from_matrix
   :blockly:

   {
      setup:function() {
         var X = 5;
         var Y = 4;
         var world = new World(X, Y);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");

         world.addEWWall(1, 1, 1);
         world.addNSWall(1, 2, Y - 1);
         
         for (var col = 2; col <= X; col++) {
            for (var row = 2; row <= Y; row++) {
               world.putBalls(col, row, 5);
            }
         }
         
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "# dopunite program",
                     ""];
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return world.getBalls(1, 1) == 60 &&
            robot.getAvenue() == 1 &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_for_fetch_60_from_matrix_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_for_fetch_60_from_matrix_solution
      :passivecode: true
      
      from karel import *
      for i_kolona in range(4):         # cetiri puta ponovi ciscenje kolone
          napred()                      #     udji u sledecu kolonu
          levo()                        #     okreni se na sever
          for i_red in range(3):        #     idi do gornje ivice i usput pokupi
              napred()                   
              for i_loptica in range(5): 
                  uzmi()                  

          desno(); desno()              #     okreni se na jug
          for i_red in range(3):        #     idi do donje ivice
              napred()                   

          levo()                        #     okreni se na istok

      levo()                            #     okreni se na zapad
      levo()                           
      for i_kolona in range(4):         # vrati se na pocetno polje
          napred()

      for i_loptica in range(60):       # ostavi sve loptice
          ostavi()



Сакупи лоптице на степеницама
'''''''''''''''''''''''''''''
.. level:: 3

.. questionnote::

   Карел поново треба да заврши у доњем десном углу, а успут треба да
   узме све лоптице.

Да би се решиo овај задатак, можеш у претходни програм да убациш петље
за узимање лоптица. Покушај да ископираш и преправиш претходни
програм.

.. karel:: Karel_for_stairs_and_balls_constant
   :blockly:

   {
      setup:function() {

         var Y = 4;
         var X = 2 * Y - 1;
         var world = new World(X, Y);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");

         // Vertical walls
         for (let y = 1; y < Y; y++) world.addNSWall(y, y, 1); // low left
         for (let y = 1; y < Y; y++) world.addNSWall(X - 1 - y, y, 1); // low right
         for (let y = 3; y <= Y; y++) world.addNSWall(y - 2, y, 1); // high left
         for (let y = 2; y <= Y; y++) world.addNSWall(X + 1 - y, y, 1); // high right
         
         // Horizontal walls
         for (let y = 1; y < Y - 1; y++) world.addEWWall(y + 1, y, 1); // low left
         for (let y = 2; y < Y; y++) world.addEWWall(y - 1, y, 1); // high left
         for (let y = 1; y < Y - 1; y++) world.addEWWall(X - 1 - y, y, 1); // low right
         for (let y = 1; y < Y; y++) world.addEWWall(X + 1 - y, y, 1); // high right
         
         // Balls
         for (let y = 2; y <= Y; y++) {
            world.putBalls(y - 1, y, 3);
            world.putBalls(y, y, 4);
         }
         for (let y = 1; y < Y; y++) {
            world.putBalls(X - y, y, 2);
            world.putBalls(X + 1 - y, y, 3);
         }

         var robot = new Robot();
         
         var code = ["from karel import *",
                     "# napisite program",
                     ""];
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return robot.getBalls() == 36 &&
            robot.getAvenue() == world.getAvenues() &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_for_stairs_and_balls_constant_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_for_stairs_and_balls_constant_solution
      :passivecode: true
      
      from karel import *
      levo()                                 # ka severu
      for i_stepenik in range(3):            # 3 puta ponovi
          napred(); desno()
          for i_loptica in range(3):
              uzmi()
          napred(); levo() #    popni se jedan stepenik 
          for i_loptica in range(4):
              uzmi()
      
      desno(); desno()                       # ka jugu
      
      for i_stepenik in range(3):            # 3 puta ponovi
          napred(); levo()
          for i_loptica in range(2):
              uzmi()
          napred(); desno() #    sidji jedan stepenik 
          for i_loptica in range(3):
              uzmi()          

Препоне
'''''''
.. level:: 3

.. questionnote::

   Помози роботу да прескочи препоне и покупи лоптицу.

   
.. karel:: Карел_препоне
    :blockly:

    {
        setup: function() {

            function random(n) {
                return Math.floor(n * Math.random());
        }
        
            var dim = 8;
            var world = new World(dim, dim);

            world.putBall(dim - random(Math.floor(dim / 2)), 1);
            for (var i = 1; i <= dim; i++)
            world.addNSWall(i, 1, random(dim - 1) + 1);

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


.. reveal:: Карел_препоне_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   Једно могуће решење (не и једино) је следеће.               

   .. activecode:: Карел_препоне_решење
      :passivecode: true

      from karel import *
      while not ima_loptica_kod_sebe():
          levo()
          while moze_napred():
              napred()
          desno()
          napred()
          desno()
          while moze_napred():
              napred()
          if ima_loptica_na_polju():
             uzmi()
          levo()
    
              
