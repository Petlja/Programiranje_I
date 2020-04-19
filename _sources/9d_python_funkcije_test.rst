Тест
====

Питање 1.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. fillintheblank:: funк_1

   Шта ће бити резултат извршавања следећег кода?

   .. code-block:: python

	 def obim(a):
		return 4 * a
	 print(obim(6))

   Одговор: |blank|

   - :^\s*24\s*$: Тачно
     :x: Одговор није тачан.
      

Питање 2.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: funк2
    :answer_a: return a * a
    :feedback_a: Тачно
    :answer_b: return а * 2
    :feedback_b: Нетачно    
    :answer_c: а * а
    :feedback_c: Нетачно    
    :answer_d: return kvadrat
    :feedback_d: Нетачно    
    :correct: a

    Коју од понуђених линија кода треба додати на обележено место да би на исправан начин била дефинисана функција која израчунава квадрат добијеног броја? Изабери тачан одговор:

    .. code-block:: python

     def stepen(a):

     _________________

Питање 3.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. fillintheblank:: funк3

   Шта ће бити резултат извршавања следећег кода?

   .. code-block:: python

	def f(a):
		return - 3 * a
	print(f(0) - f(-1))

   Одговор: |blank|

   - :^\s*\-3\s*$: Тачно
     :x: Одговор није тачан.
      

Питање 4.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. fillintheblank:: funк4

   Шта ће бити резултат извршавања следећег кода?

   .. code-block:: python

    def f(a):
   	return 2 * a + 3
  
    print(f(-2) - f(f(2)))

   Одговор: |blank|

   - :^\s*\-18\s*$: Тачно
     :x: Одговор није тачан.
      
Питање 5.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. fillintheblank:: funк5

   За коју ће вредност додељену променљивој m Пајтон окружење при покретању исписати 15?

   .. code-block:: python

    def f(a):
    	if a % 5 == 0:
    		return 2 * a
    	else:
      		return a + 1

    m = int(input("unesi ceo broj"))
    print(f(m))

   Одговор: |blank|

   - :^\s*14\s*$: Тачно
     :x: Одговор није тачан.
      
      




Питање 6.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: funк6
    :multiple_answers:
    :answer_a: return s, return m
    :feedback_a: Нетачно    
    :answer_b: return s, m
    :feedback_b: Тачно
    :answer_c: (s, m)
    :feedback_c: Нетачно    
    :answer_d: return (s, m)
    :feedback_d: Тачно
    :correct: ['b', 'd']

    Дат је задатак у којем се тражи да се за време које је Алекса провео у читању књиге дато у минутима испише исто време изражено у сатима 
	и минутима. Коју од понуђених линија кода треба додати на обележено место да би на исправан начин била дефинисана функција, 
	а програм за унето време исписивао тачан резултат? Изабери тачан одговор: 

    .. code-block:: python

     def vreme(a):
     	s = a // 60
     	m = a % 60
     	____________
     x = int(input("Unesi koliko minuta je Aleksa citao knjigu"))
     (s,m) = f(x)
     m = int(input("unesi ceo broj"))
     print(s, m)


Питање 7.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: funк7
    :answer_a: 33 "33"
    :feedback_a: Нетачно    
    :answer_b: 33 "1122"
    :feedback_b: Тачно
    :answer_c: 1122 "1122"
    :feedback_c: Нетачно    
    :answer_d: 33 33
    :feedback_d: Нетачно    
    :answer_e: Пајтон окружење ће пријавити грешку при извршавању датог програма.
    :feedback_e: Нетачно    
    :correct: b

    Шта ће бити резултат извршавања следећег програма? Изабери тачан одговор: 

    .. code-block:: python

      def f(l,n):
      	return l + n
  
      print(f(11,22)," ",f("11","22"))


Питање 8.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. fillintheblank:: funк8

   Наведи ознаку функције која за дати двоцифрен број враћа збир цифара јединица и десетица.

   (1) 

   .. code-block:: python      
  
    def dvocifren(a):
    	d = a // 10
    	j = a % 10
    return sum(j, d)

   (2) 

   .. code-block:: python

    def dvocifren(a):
      d = a // 10
      j = a % 10
      return (j, d)

   (3) 

   .. code-block:: python

    def dvocifren(a):
      d = a // 10
      j = a % 10
      return j + d

   Одговор: |blank|

   - :^\s*3\s*$: Тачно
     :x: Одговор није тачан.
      
      


Питање 9.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: fun_skuprazlicitihznakova
    :answer_a: return len(set(tekst))
    :feedback_a: Нетачно    
    :answer_b: return set(tekst) 
    :feedback_b: Тачно
    :answer_c: return len(tekst) 
    :feedback_c: Нетачно    
    :answer_d: Ниједан од понуђених одговора није тачан.
    :feedback_d: Нетачно    
    :correct: b

    Коју од понуђених линија кода можеш додати следећој дефиницији функције да би она исписивала скуп 
	различитих карактера који се налазе у датом тексту? Изабери тачан одговор:

    .. code-block:: python

     def karakteri(tekst):
     _________________________

Питање 10.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. fillintheblank:: funk10

   Дат је недовршен Пајтон програм. 

   .. code-block:: python

    import turtle
  
    def preskoci(duzina):
        ______________

    for i in range(9):
        turtle.forward(25)
        preskoci(25)

   Која од понуђених дефиниција процедуре preskoci ће уклапањем дати програм којим се исцртава 
   хоризонтална испрекидана линија? (Ако има више одговарајућих, одабери ону која има мање програмских линија)

   (1)  
   
   .. code-block:: python

    turtle.penup()
    turtle.forward(duzina)
    turtle.pendown()

   (2)
   
   .. code-block:: python 

    turtle.penup()
    turtle.forward(duzina)

   (3)  
   
   .. code-block:: python
    
    turtle.penup(25)

   Одговор: |blank|

   - :^\s*1\s*$: Тачно
     :x: Одговор није тачан.
      
