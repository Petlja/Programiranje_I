5.3. Функције
#############

.. infonote::
    Угнежђене петље се могу избећи, а програми се могу учинити много
    разумљивијим ако се уведу функције за цртање основних облика. Такође,
    функције имају и друге примене и доносе вишеструку корист током програмирања а то ће бити
    објашњено касније.

Функција за цртање многоугла
'''''''''''''''''''''''''''''

Приметимо да се цртање многоугла (каже се и *полигона*) јавило у више
различитих програма. Стога је корисно дефинисати **функцију** која служи за
цртање многоугла. Параметри те функције биће број страница полигона
и дужина једне странице.


.. activecode:: функција
   :passivecode: true

   # procedura za crtanje pravilnog poligona
   # parametri su broj stranica poligona n i duzina stranice a
   def poligon(n, a):
       for i in range(n):             # n puta ponovi:
           turtle.forward(a)          #    idi napred a koraka
	   turtle.right(360 / n)      #    okreni se za spoljasnji ugao n-tostranog pravilnog poligona
   
Дефиниција функције започета је кључном речју ``def``, након чега је
наведен назив функције (у нашем примеру, то је био ``poligon``), а
потом параметри функције у заградама (када их има више раздвајају се зарезима). 
Параметри су јој потребни да би могла да изврши задатак. Након двотачке, наведен је
програмски код који чини тело функције, увучен у односу на прву
линију (слично као што је и тело наредби ``for``, ``while`` и ``if``
увек увучено). Тело сачињавају наредбе које се извршавају сваки пут
када се функција позове.

Дефинисањем функције дефинисали смо заправо нову наредбу коју можемо
користити у програму. Након ове дефиниције, квадрат чија је страница дужине 100
пиксела нацртаћемо тако што наведемо ``poligon(4, 100)``, а шестоугао
димензије 50 тако што наведемо ``poligon(6, 50)``. Са функцијом за
цртање многоугла на располагању, наш програм за цртање три квадрата
различите боје је доста једноставније написати и постаје доста
разумљивији.

.. activecode:: полигон_функција
   :nocodelens:
   :enablecopy:
		
   import turtle

   # definisemo proceduru za crtanje pravilnog poligona
   # parametri su broj stranica poligona n i duzina stranice a
   def poligon(n, a):
       for i in range(n):             # n puta ponovi:
           turtle.forward(a)          #    idi napred a koraka
	   turtle.right(360 / n)      #    okreni se za spoljasnji ugao n-tostranog pravilnog poligona

   for i in range(3):                 # 3 puta ponovi:
       poligon(4, 50)                 #   nacrtaj kvadrat dimenzije 50 koraka
       turtle.right(360 / 3)          #   kvadrati su pravilno rasporedjeni duž punog kruga, pa se okreni za 120 stepeni

Покушај да измениш претходни програм тако да уместо квадрата црта три
шестоугла дужине страница 80 пиксела.
       
Четири квадрата
'''''''''''''''

.. questionnote::

   Напиши програм у којем корњача црта облик који се састоји од четири
   квадрата, како је приказано на наредној слици.
   
   .. image:: ../../_images/kornjaca-cetiri-kvadrata.png
      :align: center

Дефиниши функцију за цртање квадрата, а затим размисли како су ти
квадрати међусобно распоређени, тј. колико треба да се окрене корњача
након што заврши са цртањем сваког квадрата.

.. activecode:: четири_квадрата
   :nocodelens:
   :enablecopy:
   :playtask:

   import turtle
   n = 100
   # dopuni resenje
   ====
   import turtle
   n = 100
   for j in range(4):
       for i in range(4):
           turtle.forward(n)
           turtle.left(90)
       turtle.left(90)
   
   
.. reveal:: четири_квадрата_решење
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   Решење са петљом у петљи.
	       
   .. activecode:: четири_квадрата_1
      :nocodelens:

      import turtle
      n = 100
      for j in range(4):
          for i in range(4):
              turtle.forward(n)
              turtle.left(90)
          turtle.left(90)

   Решење са помоћном функцијом за цртање квадрата.
	 
   .. activecode:: четири_квадрата_2
      :nocodelens:

      import turtle

      def kvadrat(n):
          for i in range(4):
              turtle.forward(n)
              turtle.left(90)

      n = 100
      for i in range(4):
          kvadrat(n)
	  turtle.left(90)

