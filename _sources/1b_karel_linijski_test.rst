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
     
    .. image:: ../_images/karel1.png      
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
     
    .. image:: ../_images/karel1_1.png      
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
     
    .. image:: ../_images/karel3.png 
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

