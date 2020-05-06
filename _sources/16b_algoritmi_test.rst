Тест
============================

Питање 1.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: к1
    :answer_a: Исписују се бројеви до n чија је цифра јединица већа од 2.
    :feedback_a: Тачно
    :answer_b: Исписују се парни бројеви до n.
    :feedback_b: Нетачно    
    :answer_c: Исписују се бројеви већи од 2.
    :feedback_c: Нетачно    
    :correct: a

    Шта је резултат извршавања селдећег програма? Изабери тачан одговор:

    (1)

    .. code-block:: python

     n = int(input())
     while n > 0:
     	if n % 10 > 2:
        	print(n)
     	n = n - 1

Питање 2.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: к2
    :answer_a: За сваку дату страницу израчунава се површина квадрата са том странице.
    :feedback_a: Тачно
    :answer_b: израчунава се површина квадрата.
    :feedback_b: Нетачно    
    :answer_c: Ништа од наведеног.
    :feedback_c: Нетачно    
    :correct: a

    Шта је резултат извршавања селдећег програма? Изабери тачан одговор:

    .. code-block:: python

     def povrsina(a):
     	return a * a

     stranice = [13, 18, 43, 11, 8]
     for a in stranice:
     	print("Stranica:", a, "Povrsina:", povrsina(a))



Питање 3.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: к3
    :answer_a: Oд унета три броја исписује се број који је мањи од 12.
    :feedback_a: Нетачно
    :answer_b: Oд унета три броја исписује се број који је већи од 12.
    :feedback_b: Тачно    
    :answer_c: Ништа од наведеног.
    :feedback_c: Нетачно    
    :correct: b

    Шта је резултат извршавања следећег кода? Изабери тачан одговор:

    .. code-block:: python

     for i in range(3):
     visina = int(input("Unesi broj:"))
     if visina > 12:  
        print (visina)

Питање 4.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: к4
    :answer_a: :
    :feedback_a: Нетачно
    :answer_b: for
    :feedback_b: Тачно    
    :answer_c: >
    :feedback_c: Нетачно    
    :correct: b

    Шта би требало написати на место ___ како би се из листе издвојиле и исписале само температуре веће од 0?

    .. code-block:: python

     temperature = [2, -1, 0, -8, -10, -1, 4, 5, 8, 6]
     negativne_temperature = [t __ t in temperature if t > 0]
     print(negativne_temperature)


Питање 5.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: m5
    :answer_a: i
    :feedback_a: Нетачно
    :answer_b: or
    :feedback_b: Нетачно    
    :answer_c: and
    :feedback_c: Тачно    
    :correct: c

    Шта би требало написати на место ___ како би код био исправан?

    .. code-block:: python

     prosek_ognjen = 4.75
     prosek_mira = 5.00
     prosek_jelica = 5.00
     if prosek_pera >= 4.50 ___ prosek_mira >= 4.50 ___ prosek_jelica >= 4.50:
     	print("Svi učenici su odlični")
     else:
     	print("Nisu svi učenici odlični")

Питање 6.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: k6
    :answer_a: 55 55 55 55 55 90 80
    :feedback_a: Тачно
    :answer_b: 1 23 3 45 17 55 55
    :feedback_b: Нетачно    
    :answer_c: 1 23 3 45 17 90 88
    :feedback_c:     
    :correct: a

    Шта је резултат извршавања следећег кода ако је унети број n = 55? Изабери тачан резултат:

    .. code-block:: python

     lista = [1, 23, 3, 45, 17, 90, 88]
     n = int(input("Unesi broj:"))
     for i in lista:
     	print (max(i, n))

Питање 7.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: k7
    :answer_a: Исписују се бројеви: 0, 2, 4, 6, 8, 10, ..., 98, 100.
    :feedback_a: Нетачно
    :answer_b: Исписују се бројеви: 2, 4, 6, 8, 10, ..., 98.
    :feedback_b: Нетачно    
    :answer_c: Исписују се бројеви: 2, 4, 6, 8, 10, ..., 98, 100.
    :feedback_c: Тачно    
    :correct: c

    Шта би требало дописати на црти тако да се исписују сви елементи листе већи од 10? Изабери тачан одговор:

    .. code-block:: python

     i = 2
     while i <= 100:
     	print(i)
     	i = i + 2

Питање 8.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: k8
    :answer_a: 1
    :feedback_a: Нетачно
    :answer_b: 2
    :feedback_b: Тачно    
    :answer_c: 3
    :feedback_c: Нетачно    
    :correct: b

    Шта је резултат извршавања следећег кода ако је унети елемент 66? Изабери тачан одговор:

    .. code-block:: python

     lista = [1, 23, 3, 45, 17, 90, 88]
     n = int(input("Unesi broj:"))
     for i in lista:
     	print (max(i, n), min(i,n))

    (1)
	
    .. code-block:: python
	
     1 66
	 
     23 66
	 
     3 66
	 
     45 66
	 
     17 66
	 
     66 90
	 
     66 88
	 
    (2)
	
    .. code-block:: python
	
     66 1
	 
     66 23
	 
     66 3
	 
     66 45
	 
     66 17
	 
     90 66
	 
     88 66

    (3)
	
    .. code-block:: python
	
     66, 1
	 
     66, 23
	 
     66, 3
	 
     66, 45
	 
     66, 17
	 
     90, 66
	 
     88, 66


Питање 9.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: к9
    :answer_a: Исписују се први паран број листе l.
    :feedback_a: Нетачно
    :answer_b: Исписују се сви парни бројеви листе l.
    :feedback_b: Тачно    
    :answer_c: Ништа наведено.
    :feedback_c: Нетачно    
    :correct: b

    Шта је резултат извршавања следећег кода? Изабери тачан одговор:

    .. code-block:: python

     s = 0
     l = [1, 23, 45, 67, 22, 67, 89]
     for i in lista:
     	if i % 2 == 0:
        	print(i)

Питање 10.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: к10
    :answer_a: 171
    :feedback_a: Нетачно    
    :answer_b: 177
    :feedback_b: Нетачно    
    :answer_c: 184 
    :feedback_c: Тачно
    :answer_d: Ниједан од понуђених одговора није тачан. 
    :feedback_d: Нетачно    
    :correct: c

    Шта је резултат извршавања следећег кода? Изабери тачан одговор:

    .. code-block:: python

     najvisi = max(max(max(173, 171), 184), 177)
     print(najvisi)



