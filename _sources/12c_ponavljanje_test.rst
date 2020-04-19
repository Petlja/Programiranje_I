Тест
====

Питање 1.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: pit1
    :answer_a: 0, 1, 3, 6, 10
    :feedback_a: Тачно
    :answer_b: 0, 1, 2, 3, 4
    :feedback_b: Нетачно    
    :answer_c: 10
    :feedback_c: Нетачно    
    :answer_d: 15
    :feedback_d: Нетачно    
    :correct: a

    Шта је резултат извршавања следећег кода? Изабери тачан одговор:

    .. code-block:: python

     s = 0
     for i in range(5):
     	s = s + i
     	print(s)

Питање 2.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: pit2
    :answer_a: 1
    :feedback_a: Тачно
    :answer_b: 2
    :feedback_b: Нетачно    
    :answer_c: 3
    :feedback_c: Нетачно    
    :correct: a

    Која од следећих наредби исисује три пута `Здраво, свете!` ? Изабери тачан одговор:

    (1)
	
    .. code-block:: python
	
     for i in range(3):
     	print("Здраво, свете!")

    (2)
	
    .. code-block:: python
	
     for i in range(3):
     print("Здраво, свете!")

    (3)
	
    .. code-block:: python
	
     for i in range(3)
     	print("Здраво, свете!")

Питање 3.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. fillintheblank:: pit3

   Шта ће бити резултат извршавања наредног кода? Изабери тачан одговор:

   .. code-block:: python

    for i in range(9,12,8):
    	print(i)

   Одговор: |blank|

   - :^\s*9\s*$: Тачно
     :x: Одговор није тачан.

Питање 4.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: pit4
    :answer_a: 15
    :feedback_a: Нетачно 
    :answer_b: 21
    :feedback_b: Тачно   
    :answer_c: 10
    :feedback_c: Нетачно    
    :answer_d: 14
    :feedback_d: Нетачно    
    :correct: b

    Шта је резултат извршавања следећег кода? Изабери тачан одговор:

    .. code-block:: python

     s = 0
     for i in range(7):
     	s = s + i
     print(s)

Питање 5.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: pit5
    :answer_a: 12
    :feedback_a: Нетачно 
    :answer_b: 6
    :feedback_b: Нетачно       
    :answer_c: 24
    :feedback_c: Нетачно    
    :answer_d: 0
    :feedback_d: Тачно
    :correct: d

    Шта је резултат извршавања следећег кода? Изабери тачан одговор:

    .. code-block:: python

     p = 0
     for i in range(4):
     	p = p * i
     print(p)

Питање 6.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: pit6
    :answer_a: само једном
    :feedback_a: Нетачно 
    :answer_b: 10 пута
    :feedback_b: Нетачно       
    :answer_c: неће бити исписана
    :feedback_c: Тачно    
    :answer_d: бесконачно много пута
    :feedback_d: Нетачно
    :correct: c

    Колико пута ће бити исписана реченица "Zdravo, svete!"? Изабери тачан одговор:

    .. code-block:: python

     while 1 < 0:
     	print("Zdravo, svete!")

Питање 7.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: pit7
    :answer_a: 0
    :feedback_a: Нетачно 
    :answer_b: 15
    :feedback_b: Нетачно       
    :answer_c: 10
    :feedback_c: Тачно    
    :answer_d: 5
    :feedback_d: Нетачно
    :correct: c

    Шта је резултат извршавања следећих наредби? Изабери тачан одговор:

    .. code-block:: python

     s = 0
     a = 5
     while a > 0:
     	a = a - 1
     	s = s + a
     print(s)

Питање 8.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: pit8
    :answer_a: Исписаће се бројеви 5, 10, 15, 20, ..., 95
    :feedback_a: Нетачно 
    :answer_b: Исписаће се бројеви 5, 10, 15, 20, ..., 100
    :feedback_b: Тачно        
    :answer_c: Исписаће се бројеви 100, 95, ..., 10, 5
    :feedback_c: Нетачно   
    :answer_d: Исписаће се бројеви 1, 5, 10, 15, 20, ..., 100
    :feedback_d: Нетачно
    :correct: b

    Шта је резултат извршавања следећих наредби? Изабери тачан одговор:

    .. code-block:: python

     b = 5
     while b <= 100:
     	print(b)
     	b = b + 5

Питање 9.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: pit9
    :answer_a: Исписују се цифра јединица унетог броја n.
    :feedback_a: Нетачно 
    :answer_b: Исписују се цифре унетог броја n.
    :feedback_b: Тачно        
    :answer_c: Ништа од понуђеног.
    :feedback_c: Нетачно   
    :correct: b

    Шта је резултат извршавања следећих наредби? Изабери тачан одговор:

    .. code-block:: python

     n = int(input("Unesi broj:"))
     while n > 0:
     	print(n % 10)
     	n = n // 10

Питање 10.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: pit10
    :answer_a: Исписује се производ цифара унетог броја n.
    :feedback_a: Нетачно 
    :answer_b: Исписују се цифре унетог броја n.
    :feedback_b: Тачно        
    :answer_c: Исписује се сума цифара унетог броја n.
    :feedback_c: Тачно   
    :correct: c

    Шта је резултат извршавања следећих наредби? Изабери тачан одговор:

    .. code-block:: python

     s = 0
     n = int(input("Unesi broj:"))
     while n > 0:
     	s = n % 10
     	n = n // 10
     print(s)

