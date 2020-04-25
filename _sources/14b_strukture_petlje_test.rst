Тест
============================

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

     for broj in lista:
     	print(broj)

Питање 2.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: sp2
    :answer_a: Проверава да ли се дата листа дужине b.
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
    :answer_a: За сваку земљу која је у речнику исисује се површина те земље.
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
    :answer_b: i i in range(broj_ocena)
    :feedback_b: Тачно    
    :answer_c: i in range(broj_ocena):
    :feedback_c: Нетачно    
    :correct: b

    Шта би требало дописати на црти тако да се у програму учитава број оцена ученика, затим и подединачне оцене и да се на крају израчуна просек ученика.

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
    :answer_a: i in range(ocene)
    :feedback_a: Нетачно
    :answer_b: i in range(broj_ocena)
    :feedback_b: Тачно    
    :answer_c: i in range(broj_ocena):
    :feedback_c: Нетачно    
    :correct: b

    Шта би требало дописати на црти тако да се у програму учитава број оцена ученика, затим и подединачне оцене и да се на крају израчуна просек ученика.

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
    :answer_a: i in range(6),  broj > 10
    :feedback_a: Нетачно
    :answer_b: i in lista, broj > 10
    :feedback_b: Нетачно    
    :answer_c: broj in lista, broj > 10
    :feedback_c: Тачно    
    :correct: c

    Шта би требало дописати на црти тако да се исписују сви елементи листе већи од 10? Изабери тачан одговор:

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

    Шта би требало дописати на црти тако да наредни код буде решенје следећег задатка:

    *Наталија има 1000 динара. Жели да купи чоколаде које коштају 120 динара, чипс који кошта 89 динара или кока-коле које коштају 135 динара. 
    Ако буде куповала све производе исте врсте, напиши програм који одређује колико производа може да купи и колико јој динара остаје.* 
	
    Изабери тачан одговор:

    .. code-block:: python

     proizvodi = (("чоколада", 120), ("чипс", 89), ("кока-кола", 135))
     for _________ in proizvodi:
     	komada = 1000 // cena
     	ostalo = 1000 % cena
     print(proizvod, "-", "комада:", komada, "остаје:", ostalo, "динара")





