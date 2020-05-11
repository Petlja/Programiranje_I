Tест
====

Питање 1.
~~~~~~~~~

.. mchoice:: grananje2
    :answer_a: Да 
    :feedback_a: Тачно
    :answer_b: Не
    :feedback_b: Нетачно    
    :correct: a

    Написана је наредба `if` :
  
    .. code-block:: python
    
        from karel import *
        if mozeNapred():
            napred()
        else:
            levo()

    Да ли је ова наредба написана у складу са правилима програмског језика Пајтон? Изабери тачан одговор:

Питање 2.
~~~~~~~~~

.. mchoice:: grananje1
    :multiple_answers:
    :answer_a: 1 
    :feedback_a: Тачно
    :answer_b: 2 
    :feedback_b: Нетачно    
    :answer_c: 3        
    :feedback_c: Тачно
    :answer_d: 4
    :feedback_d: Нетачно    
    :correct: a
    
    Извршавањем којих од наредних програма ће робот ако може да пређе на наредно поље покупити лоптицу са тог поља (подразумева се да је на сваком пољу лоптица)?
    Изабери тачан одговор:
    
    (1)
    
    .. code-block:: python
    
        from karel import *
        if mozeNapred():
            napred()
            uzmi()

    (2)        
  
    .. code-block:: python
    
        from karel import *
        if mozeNapred():
            napred()
        uzmi()

    (3)
  
    .. code-block:: python
    
        from karel import *
        if mozeNapred()
            napred()
            uzmi()

    (4)
  
    .. code-block:: python
    
        from karel import *
        if mozeNapred():
        napred()
            uzmi()


Питање 3.
~~~~~~~~~

.. mchoice:: grananje3
    :answer_a: Ако постоје лоптице на пољу, робот ће узети све, у супротном ће оставити једну.    
    :feedback_a: Нетачно
    :answer_b: Ако постоје лоптице на пољу, робот ће узети једну, у супротном ће оставити једну.    
    :feedback_b: Тачно
    :answer_c: Ако постоје лоптице на пољу, робот ће узети једну.    
    :feedback_c: Нетачно
    :answer_d: Ако нема лоптица на пољу, робот ће узети једну.    
    :feedback_d: Нетачно
    :correct: ['b']

    Дата је наредба `if` :

    .. code-block:: python
    
        from karel import *
        if ima_loptica_na_polju():
            uzmi()    
        else:
            ostavi()

    Шта је резултат извршавања следеће наредбе? Изабери тачан одговор.


Питање 4.
~~~~~~~~~

.. mchoice:: grananje
    :answer_a: 1
    :feedback_a: Нетачно
    :answer_b: 2
    :feedback_b: Тачно
    :answer_c: 3
    :feedback_c: Нетачно
    :answer_d: 4
    :feedback_d: Нетачно
    :correct: b

    Извршавањем којег од наредних делова кода ће робот прво извршити проверу да ли има бар једну лоптицу код себе, а затим оставити једну лоптицу на пољу на ком се налази?
      
    (1)
    
    .. code-block:: python

        ima_loptica_kod_sebe()
            ostavi()
      
    (2)
    
    .. code-block:: python

        if (ima_loptica_kod_sebe()):
            ostavi()    
          
    (3)
    
    .. code-block:: python

        while (ima_loptica_kod_sebe()):
            ostavi()  
      
    (4)
    
    .. code-block:: python

        if (broj_loptica_kod_sebe()):
            ostavi()   
    
Питање 5.
~~~~~~~~~

.. mchoice:: grananje5
    :answer_a: 1
    :feedback_a: Нетачно
    :answer_b: 2
    :feedback_b: Нетачно
    :answer_c: 3
    :feedback_c: Tачно
    :answer_d: 4
    :feedback_d: Нетачно
    :answer_e: 5
    :feedback_e: Нетачно
    :correct: ['c']

    Извршавањем којег од наредних делова кода ће робот прво извршити проверу да ли има бар једну лоптицу на пољу на коме се налази, а затим узети једну лоптицу?
      
    (1)
    
    .. code-block:: python

        ima_loptica_kod_sebe():
            uzmi()
      
    (2)
    
    .. code-block:: python

        if (ima_loptica_na_polju()):
            ostavi()    
          
    (3)
    
    .. code-block:: python

        if (ima_loptica_na_polju()):
            uzmi()  
      
    (4)
    
    .. code-block:: python

        while (ima_loptica_na_polju()):
            ostavi()  
      
    (5)
    
    .. code-block:: python

        if (broj_loptica_kod_sebe()):
            uzmi()