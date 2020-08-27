19.1. Квиз - структуре података и алгоритми
===========================================

Питање 1.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: sp1
    :answer_a: 1
    :feedback_a: Тачно
    :answer_b: 2
    :feedback_b: Нетачно    
    :answer_c: 3
    :feedback_c: Нетачно    
    :correct: a

    На који од следећих начин се исписују елементи листе ``lista = [1,22,43,5]``? Изабери тачан одговор:

    (1)

    .. code-block:: python

     for broj in lista:
     	print(broj)

    (2)

    .. code-block:: python

     for broj in lista:
     print(broj)

    (3)

    .. code-block:: python

     for broj in lista
     	print(broj)

Питање 2.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: sp2
    :answer_a: Проверава да ли је дата листа дужине b.
    :feedback_a: Нетачно
    :answer_b: Проверава да ли се унети број налази у листи датих бројева.
    :feedback_b: Тачно    
    :answer_c: Ништа од наведеног.
    :feedback_c: Нетачно    
    :correct: b

    Шта је резултат извршавања следећег кода? Изабери тачан одговор:

    .. code-block:: python

     brojevi = [3, 4, 17, 21, 23, 27, 33]
     b = int(input("Unesi broj: "))
     for i in brojevi:
     	if i == b:
    		print("da")

Питање 3.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: sp3
    :answer_a: За сваку земљу која је у речнику исисује се само површина те земље.
    :feedback_a: Нетачно
    :answer_b: Исписује се списак земаља тако што се прво испише назив земље, па површина земље.
    :feedback_b: Тачно    
    :answer_c: Исписује се списак земаља.
    :feedback_c: Нетачно    
    :correct: b

    Шта је резултат извршавања следећег кода? Изабери тачан одговор:

    .. code-block:: python

     povrsine = {"Srbija": 88361,
            "Hrvatska": 56594,
            "Crna Gora": 13812,
            "Bosna i Hercegovina": 51197,
            "Slovenija": 20273,
            "Makedonija": 25713}
     for zemlja in povrsine:
    	print("Naziv: ", zemlja, "Površina: ", povrsine[zemlja])

Питање 4.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: sp4
    :answer_a: i in range(ocene)
    :feedback_a: Нетачно
    :answer_b: i in range(broj_ocena)
    :feedback_b: Нетачно    
    :answer_c: i in range(broj_ocena):
    :feedback_c: Тачно    
    :correct: c

    Шта треба да стоји на месту црте, да би програм правилно рачунао просек унетих оцена?

    .. code-block:: python

     broj_ocena = int(input("Unesi broj ocena:"))
     ocene = []
     for ________________:
    	ocena = int(input("Unesi ocenu:"))
    	ocene.append(ocena)
     prosek = sum(ocene) / len(ocene)
     print("Prosek:", prosek)

Питање 5.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: sp5
    :answer_a: Ученику се рачуна закључна оцена из предмета.
    :feedback_a: Нетачно
    :answer_b: Проверава се коју је последњу оцену добио ученик.
    :feedback_b: Нетачно    
    :answer_c: Ученику се рачуна закључна оцена из предмета у зависности од тога коју ће последњу оцену ученик добити.
    :feedback_c: Тачно    
    :correct: c

    Шта је резултат извршавања следећег кода?

    .. code-block:: python

     ocene = [3, 5, 4, 2]
     zbir = sum(ocene)
     for poslednja_ocena in (1, 2, 3, 4, 5):
    	zakljucna = round((zbir + poslednja_ocena) / 5)
    	print("Ako dobije", poslednja_ocena,
        	"biće mu zaključena ocena", zakljucna_ocena)


Питање 6.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: sp6
    :answer_a: i
    :feedback_a: Нетачно
    :answer_b: i // 4
    :feedback_b: Нетачно    
    :answer_c: i % 4
    :feedback_c: Тачно    
    :correct: c

    Шта би требало дописати на црти тако да програм исписује смену свих годишњих доба током 5 година?

    .. code-block:: python

     godisnja_doba = ["пролеће", "лето", "јесен", "зима"]
     for i in range(5 * len(godisnja_doba)):
     	print(godisnja_doba[________])   #  ispravi ovaj red
		
Питање 7.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: sp7
    :answer_a: i in range(7),  broj > 10
    :feedback_a: Нетачно
    :answer_b: i in lista, broj > 10
    :feedback_b: Нетачно    
    :answer_c: broj in lista, broj > 10
    :feedback_c: Тачно    
    :correct: c

    Шта би требало дописати на цртама тако да се исписују сви елементи листе већи од 10? Изабери тачан одговор:

    .. code-block:: python

     lista = [12, 3, 45, 67, 90, 102]
     for ___________________________:
     	if _________________________:
			print(broj)

Питање 8.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: sp8
    :answer_a: i in range(3):
    :feedback_a: Нетачно
    :answer_b: proizvod in proizvodi
    :feedback_b: Нетачно    
    :answer_c: (proizvod, cena) in proizvodi
    :feedback_c: Тачно    
    :correct: c

    Шта би требало дописати на црти тако да наредни код буде решење следећег задатка:

    *Наталија има 1000 динара. Жели да купи чоколаде које коштају 120 динара, чипс који кошта 89 динара или кока-коле које коштају 135 динара. 
    Ако буде куповала све производе исте врсте, напиши програм који одређује колико производа може да купи и колико јој динара остаје.* 
	
    Изабери тачан одговор:

    .. code-block:: python

     proizvodi = (("чоколада", 120), ("чипс", 89), ("кока-кола", 135))
     for _____________________
     	komada = 1000 // cena
     	ostalo = 1000 % cena
     print(proizvod, "-", "комада:", komada, "остаје:", ostalo, "динара")


Питање 9.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: а9
    :answer_a: Исписују се бројеви до n чија је цифра јединица већа од 2.
    :feedback_a: Тачно
    :answer_b: Исписују се парни бројеви до n.
    :feedback_b: Нетачно    
    :answer_c: Исписују се бројеви већи од 2.
    :feedback_c: Нетачно    
    :correct: a

    Шта је резултат извршавања следећег програма? Изабери тачан одговор:

    (1)

    .. code-block:: python

     n = int(input())
     while n > 0:
     	if n % 10 > 2:
        	print(n)
     	n = n - 1

Питање 10.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: а10
    :answer_a: За сваку дату страницу израчунава се површина квадрата са том страницом.
    :feedback_a: Тачно
    :answer_b: израчунава се површина квадрата.
    :feedback_b: Нетачно    
    :answer_c: Ништа од наведеног.
    :feedback_c: Нетачно    
    :correct: a

    Шта је резултат извршавања следећег програма? Изабери тачан одговор:

    .. code-block:: python

     def povrsina(a):
     	return a * a

     stranice = [13, 18, 43, 11, 8]
     for a in stranice:
     	print("Stranica:", a, "Povrsina:", povrsina(a))



Питање 11.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: а11
    :answer_a: Oд унета три броја исписује се један број који је већи од 12.
    :feedback_a: Нетачно
    :answer_b: Oд унета три броја исписује се сваки број који је већи од 12.
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

Питање 12.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: а12
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


Питање 13.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: а13
    :answer_a: i
    :feedback_a: Нетачно
    :answer_b: or
    :feedback_b: Нетачно    
    :answer_c: and
    :feedback_c: Тачно    
    :correct: c

    Шта би требало написати на место сваке црте, како би код био исправан?

    .. code-block:: python

     prosek_ognjen = 4.75
     prosek_mira = 5.00
     prosek_jelica = 5.00
     if prosek_pera >= 4.50 ___ prosek_mira >= 4.50 ___ prosek_jelica >= 4.50:
     	print("Svi učenici su odlični")
     else:
     	print("Nisu svi učenici odlični")

Питање 14.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: а14
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

Питање 15.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: а15
    :answer_a: Исписују се бројеви: 0, 2, 4, 6, 8, 10, ..., 98, 100.
    :feedback_a: Нетачно
    :answer_b: Исписују се бројеви: 2, 4, 6, 8, 10, ..., 98.
    :feedback_b: Нетачно    
    :answer_c: Исписују се бројеви: 2, 4, 6, 8, 10, ..., 98, 100.
    :feedback_c: Тачно    
    :correct: c

    Шта исписује следећи програм? Изабери тачан одговор:

    .. code-block:: python

     i = 2
     while i <= 100:
     	print(i)
     	i = i + 2

Питање 16.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: а16
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


Питање 17.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: а17
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

Питање 18.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: а18
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











