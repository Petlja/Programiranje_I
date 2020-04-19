Тест
====

Питање 1.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: pi1
    :answer_a: Проверава да ли је последња цифра броја 0.
    :feedback_a: Нетачно
    :answer_b: Проверава да ли је последња цифра броја 2.
    :feedback_b: Нетачно    
    :answer_c: Проверава да ли је број паран.
    :feedback_c: Тачно    
    :answer_d: Проверава да ли је број непаран.
    :feedback_d: Нетачно    
    :correct: c

    Шта је резултат извршавања следећег кода? Изабери тачан одговор:

    .. code-block:: python

     if n % 2 == 0:
     	print("jeste")
     else:
     	print("nije")

Питање 2.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: pi2
    :answer_a: 3
    :feedback_a: Тачно
    :answer_b: 6
    :feedback_b: Нетачно    
    :answer_c: 2
    :feedback_c: Нетачно    
    :correct: a

    Колика је вредност променљиве `a` након извршавања следећег кода ? Изабери тачан одговор:

    .. code-block:: python

     a = 6
     if a % 2 == 0:
     	a = a // 2
     else:
     	a = a % 10
     print(a)

Питање 3.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: pi3
    :answer_a: Ако је а паран број већи или једнак од 10, испиши број за 1 већи од њега, у супротном, испиши број а. 
    :feedback_a: Тачно
    :answer_b: Ако је а непаран број већи или једнак од 10, испиши број за 1 већи од њега, у супротном, испиши количник броја а и броја 10.
    :feedback_b: Нетачно    
    :answer_c: Ништа од понуђеног.
    :feedback_c: Нетачно    
    :correct: a

    Следећи код је решење ког задатка? Изабери тачан одговор:

    .. code-block:: python

     if (a % 2 == 0) and (a => 10):
     	print(a+1)
     else:
     	print(a % 10)

Питање 4.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: pi4
    :answer_a: Биће исписан текст 'ne mozes da predjes ulicu'.
    :feedback_a: Тачно
    :answer_b: Биће исписан текст 'predji ulicu'.
    :feedback_b: Нетачно    
    :answer_c: Биће исписан текст 'plavo'.
    :feedback_c: Нетачно    
    :answer_d: Ниједан од понуђених одговора није тачан.
    :feedback_d: Нетачно    
    :correct: a

    Шта ће бити резултат извршавања следећег кода? Изабери тачан одговор:

    .. code-block:: python

     semafor = 'plavo'
     if (semafor == 'zeleno'):
     	print('predji ulicu')
     else:
     	print('ne mozes da predjes ulicu')

Питање 5.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. fillintheblank:: pi5

   Шта ће бити резултат извршавања следећег кода?

   .. code-block:: python

    a = -1
    b = -1
    if (a > b):
    	print(a)
    else:
    	print(b)

   Одговор: |blank|

   - :^\s*\-1\s*$: Тачно
     :x: Одговор није тачан.

Питање 6.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: pi6
    :answer_a: Istinito = true
    :feedback_a: Нетачно    
    :answer_b: Istinito = False
    :feedback_b: Нетачно    
    :answer_c: Istinito = True
    :feedback_c: Тачно
    :answer_d: Istinito = false
    :feedback_d: Нетачно    
    :answer_e: Istinito = T 
    :feedback_e: Нетачно    
    :correct: c

    Која од наведених линија имену Istinito додељује истинитосну вредност ТАЧНО? Изабери тачан одговор:

Питање 7.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: pi7
    :answer_a: Исписаће текст Ispravno без обзира на вредност која је уписана у ime.
    :feedback_a: Тачно
    :answer_b: Исписаће текст Neispravno без обзира на вредност која је уписана у ime.
    :feedback_b: Нетачно    
    :answer_c: У зависности од тога да ли је унета вредност исправна или не биће исписана реч Ispravno, односно Neispravno.
    :feedback_c: Нетачно    
    :correct: a
	
    Шта ће бити резултат извршавања следећег кода? Изабери тачан одговор:

    .. code-block:: python

     ime = input("Unesi ime")
     if True:
     	print("Ispravno")
     else:
     	print("Neispravno") 

Питање 8.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: pi8
    :answer_a: 40
    :feedback_a: Нетачно 
    :answer_b: -40
    :feedback_b: Тачно        
    :answer_c: 10
    :feedback_c: Нетачно   
    :answer_d: 50
    :feedback_d: Нетачно
    :correct: b

    Шта је резултат извршавања следећих наредби? Изабери тачан одговор:

    .. code-block:: python

     a = 10
     b = 50
     if (( a >= 10) or (b > 70)) and (a + b > 50):
     	print(a - b)
     else:
     	print(2 * a - b)

Питање 9.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: pi9
    :answer_a: 40
    :feedback_a: Нетачно 
    :answer_b: -30
    :feedback_b: Тачно         
    :answer_c: -40
    :feedback_c: Нетачно   
    :answer_d: -80
    :feedback_d: Нетачно
    :correct: b

    Шта је резултат извршавања следећих наредби? Изабери тачан одговор:

    .. code-block:: python

     a = 10
     b = 50
     if (( a > 10) or (b > 70)) and (a + b > 50):
     	print(a - b)
     else:
     	print(2 * a - b)

Питање 10.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: pi10
    :answer_a: 4
    :feedback_a: Нетачно 
    :answer_b: 5
    :feedback_b: Нетачно         
    :answer_c: 6
    :feedback_c: Тачно   
    :answer_d: 2
    :feedback_d: Нетачно    
    :correct: c

    Шта је резултат извршавања следећих наредби? Изабери тачан одговор:

    .. code-block:: python

     s = 1
     n = 15
     if n % 2 == 1:
     	s = s + n % 10
     else:
     	s = s + n // 10
     print(s)


