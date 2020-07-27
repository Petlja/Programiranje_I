Тест
############

~~~~~~~~      
Питање 1
~~~~~~~~


.. mchoice:: karel_osnovno_1
    :answer_a: Налазиће се на истом пољу.
    :feedback_a: Тачно
    :answer_b: Налазиће се на пољу (3,5).
    :feedback_b: Нетачно    
    :answer_c: Налазиће се на пољу (5,5).
    :feedback_c: Нетачно    
    :correct: a
    
    Робот у лавиринту на слици се налази на пољу (4,5). 
     
    .. image:: ../../_images/karel1.png      
       :align: center
     
    На ком ће се пољу наћи робот извршавањем следеће наредбе?
     
    .. code-block:: python
        
       levo()


~~~~~~~~~      
Питање 2
~~~~~~~~~

.. mchoice:: karel_osnovno_2
    :answer_a: Извршавањем програма 1.
    :feedback_a: Нетачно    
    :answer_b: Извршавањем програма 2.
    :feedback_b: Тачно
    :answer_c: Извршавањем било ког од дата два програма робот стиже на исто поље (3,3).
    :feedback_c: Нетачно    
    :correct: b

    Робот у лавиринту на слици се налази на пољу (5,3). 
     
    .. image:: ../../_images/karel1_1.png      
       :align: center
     
    Након извршавања којег од наредних програма ће се робот наћи на пољу (3,3)?
     
    Програм 1.
    
    .. code-block:: python
        
        from karel import *
        levo()
        napred()
        levo()
        napred()
     
    Програм 2.
    
    .. code-block:: python
        
        from karel import *
        levo()
        levo()
        napred()
        napred()

~~~~~~~~      
Питање 3
~~~~~~~~

.. fillintheblank:: karel_osnovno_3

   Нека је Карел робот у положају као на слици.
    
   .. image:: ../_images/karel2.png   
      :align: center
    
   Поређај команде тако да робот на најкраћи начин стигне до рупе.
    
   (1) 
     .. code-block:: python
       
       levo()
    
   (2) 
     .. code-block:: python
       
       napred()
    
    
   (Одговор упиши навођењем редних бројева команди у одговарајућем редоследу, нпр. 1221)
    
    
   - :^\s*121112\s*$: Тачно
     :x: Одговор није тачан.
	    
~~~~~~~~      
Питање 4
~~~~~~~~

.. mchoice:: karel_nazad
    :answer_a: Робот ће се померити за два поља на лево и бити на пољу (1,1).
    :feedback_a: Нетачно    
    :answer_b: Робот ће се окренути за 180 степени и налазити се на пољу на ком се налазио и пре извршавања датог кода.        
    :feedback_b: Тачно
    :answer_c: Робот ће се померити за два поља на десно и бити на пољу (5,1).
    :feedback_c: Нетачно    
    :answer_d: Ниједан од понуђених одговора није тачан.     
    :feedback_d: Нетачно    
    :correct: b
    
    Нека је Карел робот у положају као на слици.
     
    .. image:: ../../_images/karel3.png 
       :align: center
     
    У ком положају ће се наћи робот након извршавања следећег дела кода:
     
    .. code-block:: python
        
       desno(); desno();


~~~~~~~~      
Питање 5
~~~~~~~~

.. mchoice:: karel_nazad_2
    :answer_a: Робот ће се померити за два поља лево и бити на пољу (1,1).
    :feedback_a: Нетачно    
    :answer_b: Робот ће се налазити се на пољу на ком се налазио и пре извршавања датог кода. 
    :feedback_b: Тачно
    :answer_c: Робот ће се померити за два поља десно и бити на пољу (5,1).       
    :feedback_c: Нетачно    
    :answer_d: Ниједан од понуђених одговора није тачан.     
    :feedback_d: Нетачно    
    :correct: b
    
    Нека је Карел робот у положају као на слици.
     
    .. image:: ../_images/karel3.png 
       :align: center
     
    На ком пољу ће се робот наћи након извршавања следећег дела кода:
     
    .. code-block:: python
        
       napred(); levo(); levo(); napred();


Питање 6.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: karel_for_range
    :answer_a: for i in range:
    :feedback_a: Нетачно    
    :answer_b: for i in range()
    :feedback_b: Нетачно    
    :answer_c: for i in range(4):
    :feedback_c: Тачно
    :answer_d: for i in (1,4): 
    :feedback_d: Нетачно    
    :correct: c
    
    Која од наредних наредби је прави облик коришћења  петље for којом се описује понављање 4 пута: 



Питање 7.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: karel_for
    :answer_a: napred(); napred(); desno(); napred(); desno();
    :feedback_a: Нетачно    
    :answer_b: napred(); napred(); napred(); desno();
    :feedback_b: Нетачно    
    :answer_c: napred(); desno(); napred(); desno(); napred(); 
    :feedback_c: Тачно
    :answer_d: napred(); desno(); desno(); napred(); 
    :feedback_d: Нетачно    
    :correct: c

    Нека je дат следећи део кода.

    .. code-block:: python

       for i in range(2):
          napred()
          desno()
       napred()

    Који од наредних кодова ће дати исти резултат при извршавању? Изабери тачан одговор:

Питање 8.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mchoice:: karel_for2
    :answer_a: napred(); napred(); desno(); napred(); desno();
    :feedback_a: Нетачно    
    :answer_b: napred(); napred(); napred(); desno();
    :feedback_b: Нетачно    
    :answer_c: napred(); desno(); napred(); desno(); napred(); 
    :feedback_c: Нетачно    
    :answer_d: napred(); desno(); desno(); napred(); 
    :feedback_d: Тачно
    :correct: d

    Нека je дат следећи део кода.

    .. code-block:: python

       napred() 
       for i in range(2):
           desno()
       napred()

    Који од наредних кодова ће дати исти резултат при извршавању? Изабери тачан одговор:

Питање 9.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. mchoice:: karel_dve_petlje
    :answer_a: Програм (1)
    :feedback_a: Нетачно    
    :answer_b: Програм (2)
    :feedback_b: Нетачно    
    :answer_c: Програм (3)
    :feedback_c: Нетачно    
    :answer_d: Програм (4)
    :feedback_d: Тачно
    :correct: d
    
    Нека је Карел робот у положају као на слици
     
    .. image:: ../_images/karel7.png 
       :align: center
     
    Извршавањем којих од наредних програма ће робот проћи кроз цео лавиринт, caкупити свих пет лоптица и убацити их у рупу? 
     
    (1)
      .. code-block:: python
     
        from karel import *   
        napred()    
        for i in range(5):    
          uzmi()
          for i in range(5):
          ostavi()
      
    (2)
      .. code-block:: python
     
        from karel import *   
        napred()    
        for i in range(5):    
          uzmi()
          napred()
          for i in range(5):
          ostavi()
     
    (3)
      .. code-block:: python
     
        from karel import *   
        napred()    
        for i in range(5):    
          uzmi()
          napred()
          ostavi()
     
    (4)
      .. code-block:: python
     
        from karel import *   
        napred()    
        for i in range(5):    
          uzmi()
        napred()
        for i in range(5):
          ostavi()
      

Питање 10.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. fillintheblank:: karel_jedna_petlja

   Нека је Карел робот у положају као на слици
    
   .. image:: ../../_images/karel7.png 
      :align: center
    
   и нека је његов задатак да caкупи свих пет лоптица и убаци их у рупу. 
   Дат је недовршен програм који би требало да представља решење роботовог задатка. 
    
   .. code-block:: python
    
       from karel import *   
       napred()    
       for i in range(5):    
         ____________
          
         ____________
    
   У блоку for петље недостаје неколико команди. Допуни тело петље навођењем неких од наредних команди у одговарајућем редоследу тако да ће робот извршавањем допуњеног програма обaвити свој задатак.
    
   (1)
     .. code-block:: python
    
       napred() 
    
   (2)
     .. code-block:: python
    
       levo()
    
   (3)
     .. code-block:: python
    
       uzmi()  
    
   (4)
     .. code-block:: python
    
       ostavi()
    
   Од могућих решења, одабрати оно које подразумева најмањи број команди и у коме Карел оставља лоптицу чим дође до поља.
   (Одговор упиши навођењем редних бројева команди распоређених у одговарајући редослед, нпр. 12213)
    	 
   - :^\s*31422122\s*$: Тачно
     :x: Одговор није тачан.


