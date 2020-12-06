1.3. Квиз
#########

~~~~~~~~      
Питање 1
~~~~~~~~

.. fillintheblank:: karel_osnovno_3

   Нека је Карел робот у положају као на слици.
    
   .. image:: ../../_images/karel2.png   
      :align: center
    
   Поређај команде тако да робот на најкраћи начин стигне до рупе.
    
   (1) 
     .. code-block:: python
       
       levo()
    
   (2) 
     .. code-block:: python
       
       napred()
    
    
   (Одговор упиши навођењем редних бројева команди у одговарајућем редоследу, нпр. 1221)
    
    
   - :^\s*121112|\s*$: Тачно
     :x: Одговор није тачан.
	    
~~~~~~~~      
Питање 2
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
Питање 3
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
     
    .. image:: ../../_images/karel3.png 
       :align: center
     
    На ком пољу ће се робот наћи након извршавања следећег дела кода:
     
    .. code-block:: python
        
       napred(); levo(); levo(); napred();

~~~~~~~~~
Питање 4
~~~~~~~~~

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


~~~~~~~~~
Питање 5
~~~~~~~~~

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
