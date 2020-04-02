Тест
#####

Питање 1.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: karel_while_3
    :answer_a: Да
    :feedback_a: Тачно    
    :answer_b: Не
    :feedback_b: Нетачно    
    :correct: a
    
    Да ли је следећа наредба `if` исправно записана. Изабери тачан одговор:
	
	.. code-block:: python
	
	  if moze_napred():
		napred()
	  else:
		ostavi()

Питање 2.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: karel_while_4
    :answer_a: Да
    :feedback_a: Тачно    
    :answer_b: Не
    :feedback_b: Нетачно    
    :correct: b
    
    Да ли је следећа наредба `while` исправно записана. Изабери тачан одговор:
	
	.. code-block:: python
	
	  while moze_napred()
		napred()
		uzmi()
		levo()

Питање 3.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: karel_pitanje_8
    :answer_a: Бројачка петља
    :feedback_a: Тачно    
    :answer_b: Петља са провером услова на почетку
    :feedback_b: Нетачно    
    :answer_c: Гранање
    :feedback_c: Нетачно
    :correct: a
    
    Шта од понуђених одговора користимо ако унапред знамо да робот мора да покупи 10 лоптица?

Питање 4.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: karel_while_1
    :answer_a: 1
    :feedback_a: Нетачно    
    :answer_b: 2
    :feedback_b: Нетачно    
    :answer_c: 3
    :feedback_c: Тачно
    :answer_d: 4 
    :feedback_d: Нетачно    
    :correct: c
    
    Који од наредних програма описује кретање робота кроз лавиринт тако да покупи све лоптице испред себе и пренесе их у одгорајуће рупе испред?
	
	.. image:: ../_images/karel3_1.png 
   	   :align: center
	
	(1)
	
	.. code-block:: python
	
	  while moze_napred():
		napred()
	  while ima_loptica_na_polju():
		uzmi()
		napred()
	  while ima_loptica_kod_sebe():
			ostavi()

	(2)
	
	.. code-block:: python
	
	  while moze_napred():
		napred()
	  	while ima_loptica_na_polju():
			uzmi()
			napred()
	  	while ima_loptica_kod_sebe():
			ostavi()

	(3)
	
	.. code-block:: python
	
	  while moze_napred():
		napred()
	  	while ima_loptica_na_polju():
			uzmi()
		napred()
	  	while ima_loptica_kod_sebe():
			ostavi()

	(4)
	
	.. code-block:: python
	
	  while moze_napred():
		napred()
	  	while ima_loptica_na_polju():
			uzmi()
			napred()
	  		while ima_loptica_kod_sebe():
				ostavi()


Питање 5.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: karel_for_1
    :answer_a: napred(); napred(); desno(); napred(); desno();
    :feedback_a: Нетачно    
    :answer_b: napred(); napred(); napred(); desno();
    :feedback_b: Нетачно    
    :answer_c: napred(); desno(); napred(); desno(); napred(); 
    :feedback_c: Тачно
    :answer_d: napred(); desno(); desno(); napred(); 
    :feedback_d: Нетачно    
    :correct: c
    
    Погледај део кода који је дат, а затим одговори шта је резултат извршавања овог кода.

	.. code-block:: python
     
	 for i in range(2):
	 	napred()
		desno()
	 napred()

Питање 6.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: karel_for_3
    :answer_a: napred(); napred(); desno(); napred(); desno();
    :feedback_a: Нетачно    
    :answer_b: napred(); napred(); napred(); desno();
    :feedback_b: Нетачно    
    :answer_c: napred(); desno(); napred(); desno(); napred(); 
    :feedback_c: Нетачно    
    :answer_d: napred(); desno(); desno(); napred(); 
    :feedback_d: Тачно
    :correct: d

	Нека je дат следећи део кода. Погледај код, па одговори шта је резултат извршавања овог кода.

	.. code-block:: python

  	 napred() 
  	 for i in range(2):
	 	desno()
  	 napred()

Питање 7.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: karel_zacaran_1
    :answer_a: 1
    :feedback_a: Нетачно    
    :answer_b: 2
    :feedback_b: Нетачно    
    :answer_c: 3
    :feedback_c: Нетачно    
    :answer_d: 4
    :feedback_d: Тачно
    :correct: d

	Испред робота је зачарани лавиринт такав да се дужина лавиринта мења, али се испред Карела на сваком пољу увек налази по 4 лоптице. Којим од наредних програма робот сакупља све лоптице испред себе?
	
	.. image:: ../_images/karel3_2.png 
   	   :align: center

	(1)
	
	.. code-block:: python
	 
	 while moze_napred():
	 	napred():
		for i in range(4):
			uzmi()

	(2)
	
	.. code-block:: python
	 
	 while moze_napred():
	 	napred()
		for i in range(4)
			uzmi()

	(3)
	
	.. code-block:: python
	 
	 while moze_napred():
	 	napred()
	 for i in range(4)
	 	uzmi()

	(4)
	
	.. code-block:: python
	 
	 while moze_napred():
	 	napred()
		for i in range(4):
			uzmi()

Питање 8.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: karel_lavirint_8
    :answer_a: 1
    :feedback_a: Нетачно    
    :answer_b: 2
    :feedback_b: Тачно    
    :answer_c: 3
    :feedback_c: Нетачно    
    :answer_d: 4
    :feedback_d: Нетачно
    :correct: b

	Испред робота је лавиринт као на слици, који од наредних програма ће помоћи роботу да покупи све лоптице испред себе?
	
	.. image:: ../_images/karel3_3.png 
   	   :align: center

	(1)
	
	.. code-block:: python
	 
	 for i in range(5):
	 	napred():
		for i in range(3):
			uzmi()

	(2)
	
	.. code-block:: python
	 
	 for i in range(3):
	 	napred()
		for i in range(5):
			uzmi()


	(3)
	
	.. code-block:: python
	 
	 for i in range(5):
		for i in range(3):
		    napred()
			uzmi()


	(4)
	
	.. code-block:: python
	 
	 for i in range(3):
		for i in range(5):
		    napred()
			uzmi()



Питање 9.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: karel_pitanje_9
    :answer_a: Робот је на једном пољу иза поља са кога је пошао (поље лево од полазног).
    :feedback_a: Нетачно    
    :answer_b: Робот је на пољу испред поља са кога је пошао (поље десно од полазног).
    :feedback_b: Нетачно    
    :answer_c: Робот се вратио у првобитни положај, али окренут је на супротну страну.
    :feedback_c: Нетачно    
    :answer_d: Робот се вратио у првобитни положај.
    :feedback_d: Тачно
    :correct: d

	Робот је у празном лавиринту и окренут је на десно. Шта је резултат извршавања следећег низа наредби? Изабери тачан одговор:

	.. code-block:: python

  	 for i in range(2):
	 	napred()
		levo()
		levo()
