7.5. Вежбање
############

Ова лекција није много тешка, али је прилично обимна, па је сасвим
могуће да неки од приказаних задатака нисте стигли да проанализирате
током часа. Ако има таквих задатака, уради их сада, у склопу домаћег
задатка. Након тога уради и наредне задатке. Додатне задаткеза вежбу
можеш пронаћи `овде <IzracunavanjeZadaci.html>`_.

Израз
'''''
   
.. questionnote::

   Збир бројева 23765 и 7825 умањи 45 пута, па добијени број повећај
   за 1609. Колики је резултат?  Задатак реши једним изразом (немој да
   рачунаш пешке).

.. activecode::	израз_2

   print() # у заграде упиши израз

Провери да ли је твој програм израчунао тачно решење.
   
.. fillintheblank:: fill_израз2
		    
   Колико је решење?
   
   - :^2311$: Тачан одговор
     :.*: Покушај поново
   
Тркачи
''''''
   
.. questionnote::

   Васа је прешао 2347 метара. Воја 987 метара више од Васе, а Милош два
   пута више од Воје. Колико су метара укупно прешли?

.. activecode:: три_тркача
   :runortest: vasa, ukupno
    
   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   vasa  = 2347
   # -*- acsection: main -*-
   # dopuni ovde kod
   # -*- acsection: after-main -*-
   print(ukupno)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for vasa, ukupno in [(2462, 12809), (773, 6053)]:
             self.assertEqual(acMainSection(vasa = vasa)["ukupno"],ukupno,"Ако је Васа претрчао %s метара, укупно су претрчали %s метара." % (vasa, ukupno))
   myTests().main()
   
.. reveal:: тркачи_решење_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење
   
   .. activecode:: три_тркача_решење
    
      vasa  = 2347
      voja  = vasa + 987
      milos = voja * 2
      ukupno = vasa + voja + milos
      print(ukupno)


Технике које смо до сада научили довољне су нам да бисмо решили велики број
математичких задатака. Размотримо неколико.

   
Године маме и тате
''''''''''''''''''

.. questionnote::

   Милица има 4 године, њена мама има 7 пута више година него она, а њен
   тата има 8 пута више година него она. Колико је година Миличин тата старији
   од њене маме?
   
.. parsonsprob:: godine

   Поређај делове кода тако да представљају исправно решење овог задатка.
   -----
   milica = 4
   =====
   mama = 7 * milica
   tata = 8 * milica
   =====
   razlika = tata - mama
   =====
   print(razlika)

   
Река Морава
'''''''''''

.. questionnote::

   Велика Морава је дугачка 185km и настаје од Јужне Мораве, која је
   90km дужа, и Западне Мораве, која је 123km дужа од ње. Колика је
   укупна дужина ове три реке?


.. activecode:: морава

   velika_morava = 185
   juzna_morava = velika_morava + 90
   zapadna_morava = velika_morava + 123
   ukupno = ??? # ispravi ovaj red
   print(ukupno)

Немањићи
''''''''

.. questionnote:: 

  Стефан Немањић је постао краљ Србије 1217 и владао је 11
  година. После њега је Радослав владао до 1234. године, па Владислав,
  који је владао 9 година и предао престо брату Урошу Првом, који је
  владао до 1276. У којим временским периодима су владали ови српски
  краљеви?

.. activecode:: немањићи
		
  Stefan_pocetak = 1217
  Stefan_kraj = 1217 + 11
  Radoslav_pocetak = Stefan_kraj
  Radoslav_kraj = 1234
  Vladislav_pocetak = 0
  Vladislav_kraj = 0
  Uros_pocetak = 0
  Uros_kraj = 0
  print("Стефан:", Stefan_pocetak, "-", Stefan_kraj)
  print("Радослав:", Radoslav_pocetak, "-", Radoslav_kraj)
  print("Владислав:", Vladislav_pocetak, "-", Vladislav_kraj)
  print("Урош:", Uros_pocetak, "-", Uros_kraj)

Исправи претходни програм тако да исправно израчуна периоде у којима
су владали краљеви. Ако све урадиш како треба добићеш следеће резултате:

::

   Стефан: 1217 - 1228
   Радослав: 1228 - 1234
   Владислав: 1234 - 1243
   Урош: 1243 - 1276


Једначина
'''''''''

.. questionnote::

   Напиши програм који израчунава који број треба додати броју 123780
   да се добије број 321732.

Нажалост, Python не може директно да решава једначине. Ти мораш да
напишеш израз којим се непозната вредност израчунава на основу
познатих, а онда ти он може помоћи у рачунању.

.. activecode:: непознати_сабирак

   prvi_sabirak = 123780
   zbir = 321732
   drugi_sabirak = 0    # popravi resenje
   print(drugi_sabirak)

Провери да ли је твој програм израчунао тачно решење.
   
.. fillintheblank:: fill_једначина
		    
   Колико је решење?

   - :^197952$: Тачан одговор
     :.*: Од збира одузми познати сабирак"

Ако у решењу нису коришћене вредности, већ само називи променљивих,
програм би требало да исправно решава задатке и за друге
бројеве. Тестирај га на тест-примерима које смо припремили.

.. activecode:: непознати_сабирак_тест
   :runortest: prvi_sabirak, zbir, drugi_sabirak

   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   prvi_sabirak = 123780
   zbir = 321732
   # -*- acsection: main -*-
   drugi_sabirak = 0    # popravi resenje
   # -*- acsection: after-main -*-
   print(drugi_sabirak)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for prvi_sabirak, zbir, drugi_sabirak in [(100, 230, 130), (200, 942, 742)]:
             self.assertEqual(acMainSection(prvi_sabirak = prvi_sabirak, zbir = zbir)["drugi_sabirak"],drugi_sabirak,"Ако је једначина %s + x = %s, тада је x = %s." % (prvi_sabirak, zbir, drugi_sabirak))
   myTests().main()

