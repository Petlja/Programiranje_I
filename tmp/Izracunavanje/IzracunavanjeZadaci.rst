Израчунавања - Додатни задаци за вежбу
######################################


Основне аритметичке операције и примена - задаци
::::::::::::::::::::::::::::::::::::::::::::::::

  
Једначина
'''''''''
.. level:: 1

.. questionnote::

   Напиши програм који решава једначине у којима је позната разлика и
   умањеник, а израчунава се непознати умањилац. На пример, ако је
   Маша имала 1374 динара пре него што је ушла у продавницу, а сада
   има 728 динара, колико је пара потрошила у продавници?

.. activecode:: непознати_умањилац_тест
   :runortest: umanjenik, razlika, umanjilac

   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   umanjenik = 1374
   razlika = 728
   # -*- acsection: main -*-
   umanjilac = 0    # popravi resenje
   # -*- acsection: after-main -*-
   print(umanjilac)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for umanjenik, razlika, umanjilac in [(548, 272, 276), (942, 207, 735)]:
             self.assertEqual(acMainSection(umanjenik = umanjenik, razlika = razlika)["umanjilac"],umanjilac,"Ако је једначина %s - x = %s, тада је x = %s." % (umanjenik, razlika, umanjilac))
   myTests().main()

Провери да ли је твој програм израчунао тачно колико је пара Маша потрошила.
   
.. fillintheblank:: fill_једначина_умањилац
		    
   Колико је решење?

   - :^646$: Тачан одговор
     :.*: Покушај поново

Програм, наравно, треба да ради исправно и када се улазни подаци
промене. Тестирај га на основу тест-примера које смо припремили.
	  
Обућа
'''''
.. level:: 1
  
.. questionnote::

   У једној фабрици обуће прошле године је произведено 356.000 пари
   ципела и 247.923 пара чизама. Напиши програм који израчунава колико
   је пари ципела произведено више него пари чизама и колико је укупно
   произведено пари обуће и колико је укупно произведено комада
   обуће. Напиши програм тако да исправно ради и када у бројеви дати у
   задатку другачији.

.. activecode:: обућа

   pari_cipela = 356000
   pari_cizama = 247923
   # dopuni rešenje

Провери да ли је програм добро израчунао

.. fillintheblank:: fill_обућа1
		    
   Колико има више пари ципела него пари чизама?
      
   - :^108077$: Тачан одговор
     :.*: Одузми број пари чизама од броја ципела

.. fillintheblank:: fill_обућа2

   Колико укупно има пари ципела и чизама?

   - :^603923$: Тачан одговор
     :.*: Сабери број пари ципела и чизама

.. fillintheblank:: fill_обућа3
	  
   Колико укупно има комада обуће?

   - :^1207846$: Тачан одговор
     :.*: Помножи број пари ципела и чизама са два
		  
	      
.. reveal:: обућа_решење
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   .. activecode:: обућа_решење_код
    
      pari_cipela = 356000
      pari_cizama = 247923
      vise_pari_cipela = pari_cipela - pari_cizama
      print(vise_pari_cipela)
      ukupno_pari_obuce = pari_cipela + pari_cizama
      print(ukupno_pari_obuce)
      ukupno_komada_obuce = ukupno_pari_obuce * 2
      print(ukupno_komada_obuce)

Карте у возу
''''''''''''
.. level:: 1

.. questionnote::

   Кондуктер је једног дана прегледао карте са бројевима од 276,898 до
   277,236. Напиши програм који израчунава колико путника се тог дана
   возило возом?

.. activecode:: број_путника

   od_karte = 277236
   do_karte = 276898
   broj_karata = 0     # popravi ovaj red
   print(broj_karata)   

.. fillintheblank:: fill_број_путника
		    
      Колико се путника возило возом?

      - :^339$: Тачан одговор!
	:.*: Размисли како би се резултат израчунао да су продате карте од броја 3 до броја 7. Пази да не погрешиш за један.

   
.. reveal:: број_путника_решење
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   .. activecode:: број_путника_решење_код

      od_karte = 277236
      do_karte = 276898
      broj_karata = od_karte - do_karte + 1
      print(broj_karata)

Аутомобили
''''''''''
.. level:: 1
  
.. questionnote::

   Продавница половних аутомобила има 317 возила. Од тог броја 95 је
   потпуно исправно. Колико је потребно новца да сви аутомобили
   постану исправни, ако поправка једног аута кошта 9756 динара.

.. activecode:: аутомобили
   :runortest: automobili, ispravni, popravka_jednog, popravka_svih
		
   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   automobili = 317
   ispravni = 95
   popravka_jednog = 9756
   # -*- acsection: main -*-
   # dopuni ovde kod
   # -*- acsection: after-main -*-
   print(popravka_svih)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for automobili, ispravni, popravka_jednog, popravka_svih in [(442, 118, 11324, 3668976), (92, 83, 955, 8595)]:
             self.assertEqual(acMainSection(automobili = automobili, ispravni = ispravni, popravka_jednog = popravka_jednog)["popravka_svih"],popravka_svih,"Ако је у продавници било %s аутомобила, од којих је %s било исправно, а ако поправка једног кошта %s динара, поправка укупно кошта %s динара." % (automobili, ispravni, popravka_jednog, popravka_svih))
   myTests().main()
		
   
.. reveal:: аутомобили_решење_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење
   
   .. activecode:: аутомобили_решење

      automobili = 317
      ispravni = 95
      neispravni = automobili - ispravni
      popravka_jednog = 9756
      popravka_svih   = neispravni * popravka_jednog
      print(popravka_svih)


Сличице
'''''''
.. level:: 2

.. questionnote::

   Урош и Растко имају заједно 317 сличица. Растко и Павле имају
   заједно 295 сличица. Павле и Урош имају заједно 212 сличица. Напиши
   програм који израчунава и исписује колико сличица има свако од њих.

.. activecode:: сличице_у_паровима

   uros_i_rastko = 317
   rastko_i_pavle = 295
   pavle_i_uros = 212
   # dopuni resenje
   print(pavle, uros, rastko)

Провери да ли твој програм исправно израчунава решење.
   
.. fillintheblank:: fill_сличице_1
		    
      Колико сличица има Урош?

      - :^117$: Тачан одговор
	:.*: Покушај поново

.. fillintheblank:: fill_сличице_2
      
      Колико сличица има Растко?
      
      - :^200$: Тачан одговор
	:.*: Покушај поново

.. fillintheblank:: fill_сличице_3
      
      Колико сличица има Павле?
      
      - :^95$: Тачан одговор
	:.*: Покушај поново
      
   
.. reveal:: сличице_помоћ
   :showtitle: Прикажи малу помоћ
   :hidetitle: Сакриј малу помоћ

   Израчунај прво колико сви заједно имају сличица.
		
.. reveal:: сличице_решење
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   .. activecode:: сличице_у_паровима_решење

      uros_i_rastko = 317
      rastko_i_pavle = 295
      pavle_i_uros = 212
      zajedno = (uros_i_rastko + rastko_i_pavle + pavle_i_uros) // 2
      pavle = zajedno - uros_i_rastko
      uros = zajedno - rastko_i_pavle
      rastko = zajedno - pavle_i_uros
      print(pavle, uros, rastko)

Провери да ли твој програм и даље ради када се измене вредности
улазних података. Израчунај колико Павле има сличица.

.. activecode:: slicice_test
   :runortest: rastko_i_pavle, uros_i_rastko, pavle_i_uros, pavle
		
   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   uros_i_rastko = 317
   rastko_i_pavle = 295
   pavle_i_uros = 212
   # -*- acsection: main -*-
   # dopuni ovde kod
   # -*- acsection: after-main -*-
   print(pavle)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for rastko_i_pavle, uros_i_rastko, pavle_i_uros, pavle in [(73, 94, 81, 30), (103, 75, 94, 61)]:
             self.assertEqual(acMainSection(rastko_i_pavle = rastko_i_pavle, uros_i_rastko = uros_i_rastko, pavle_i_uros = pavle_i_uros)["pavle"],pavle,"Ако Растко и Павле имају %s сличица, Урош и Растко %s сличица, а Павле и Урош %s сличица, тада Павле има %s сличица." % (rastko_i_pavle, uros_i_rastko, pavle_i_uros, pavle))
   myTests().main()
      

Целобројно и реално дељење - задаци
:::::::::::::::::::::::::::::::::::

Израз
'''''
.. level:: 1

.. questionnote::

   Израчунај вредност :math:`14 - \frac{-4 - (-13,2)}{19 -  2,1 - 7\cdot 2,5}` у Python-у.

.. activecode:: Сложени_израз_са_дељењем_2

  print()  # popravi ovaj red

Израз
'''''
.. level:: 1
  
.. questionnote::

   Број 345 увећај 76 пута, па добијени резултат увећај за количник
   бројева 141126 и 258 (први број јесте дељив са другим). Који се
   резултат добија? Задатак реши једним изразом (немој да рачунаш
   пешке).

.. activecode:: операције

   print()   # у заграде упиши израз

Провери да ли је твој програм израчунао тачно решење.
   
.. fillintheblank:: fill_израз3
		    
   Колико је решење?
   
   - :^26767$: Тачан одговор
     :.*: Покушај поново
      
  
Сложенија једначина
'''''''''''''''''''
.. level:: 2

.. questionnote::

   Софија је замислила један број. Помножила га је са 1.345, а затим
   је добијени производ сабрала са 1.742.435 и добила је резултат
   3.402.165.  Који је број Софија замислила (пусти да то твој програм
   израчуна и немој ништа да рачунаш са стране)?

Претпоставимо да је Софија замислила број :math:`x`. Тада важи да је
:math:`x \cdot 1345 + 1742435 = 3402165`. Изрази :math:`x` из претходне
једначине и допуни наредни програм тако да га израчуна.

.. activecode:: сложенија_једначина

  x = 0 # ovde napiši rešenje
  print(x)

.. fillintheblank:: fill_сложенија_једначина

   Колико је решење?
		    
   - :^1234$: Тачан одговор
     :.*: Одузми 1742435 од резултата, па добијену разлику подели са 1345
  
Оловке
''''''
.. level:: 2
      
.. questionnote::

   Сташа је 16 оловака платила 3408 динара. Колико ће платити 21 оловку?

.. activecode:: оловке_израз

   print() # у заграде упиши израз

Провери да ли твој програм исправно израчунава решење.
   
.. fillintheblank:: fill_оловке
		    
   Колико кошта 21 оловка?

   - :^4473$: Тачан одговор!
     :.*: Покушај поново
   
   
Куповина
''''''''
.. level:: 1
   
.. questionnote::
   
   Ана има 8460 динара. Петину новца је потрошила у књижари, а трећину
   укупне суме у самопослузи. Колико новца је остало Ани?

.. activecode:: књижара_самопослуга
   :runortest: novac, ostalo

   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   novac  = 8460
   # -*- acsection: main -*-
   # dopuni ovde kod
   # -*- acsection: after-main -*-
   print(ostalo)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for novac, ostalo in [(1110, 518), (1380, 644)]:
             self.assertEqual(acMainSection(novac = novac)["ostalo"],ostalo,"Ако је Ана имала %s динара, остало јој је %s динара." % (novac, ostalo))
   myTests().main()
	       
		
   
.. reveal:: књижара_самопослуга_решење_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење
   
   .. activecode:: књижара_самопослуга_решење

      novac = 8460
      knjizara = novac/5
      samoposluga = novac/3
      ostalo = novac - (knjizara + samoposluga)
      print(ostalo)

   Решење смо могли добити и помоћу једног израза.
   
   .. activecode:: књижара_самопослуга_израз
    
      print(8460 - (8460 / 5 + 8460 / 3))

Фабрика гума
''''''''''''
.. level:: 1
   
.. questionnote::

   У првом полугодишту фабрика је произвела 3800 гума, а у другом три пута
   више. Четвртина укупне производње за ту годину је продата. Колико гума још
   није продато.

.. activecode:: гуме
   :runortest: prvo, neprodato

   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   prvo = 3800
   # -*- acsection: main -*-
   # dopuni kod na ovom mestu
   # -*- acsection: after-main -*-
   print(neprodato)
   ====   
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for prvo, neprodato in [(4200, 12600), (5550, 16650)]:
             self.assertEqual(acMainSection(prvo = prvo)["neprodato"],neprodato,"Ако у првом полугодишту произведно %s гума, непродато је остало %s." % (prvo, neprodato))
   myTests().main()
   
.. reveal:: гуме_решење_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење
   
   .. activecode:: гуме_решење
    
      prvo = 3800
      drugo = prvo * 3
      ukupno = prvo + drugo
      prodato = ukupno / 4
      neprodato = ukupno - prodato
      print(neprodato)

Кантице џема
''''''''''''
.. level:: 1
   
.. questionnote::

   Бака је скувала 2480 грама џема, а мама два пута више. Сав џем су
   спаковале у шест једнаких кантица. Колико грама џема има у свакој
   кантици. Напиши програм тако да исправно ради и када се зада
   другачија маса џема коју је бака направила.

.. activecode:: кантице_џема
   :runortest: baka, u_kantici

   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   baka = 2480
   # -*- acsection: main -*-
   # dopuni program
   # -*- acsection: after-main -*-
   print(u_kantici)
   ====   
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for baka, u_kantici in [(848, 424), (200, 100)]:
             self.assertEqual(acMainSection(baka = baka)["u_kantici"],u_kantici,"Ако је Бака направила  %s грама џема, у кантици има %s грама." % (baka, u_kantici))
   myTests().main()

.. reveal:: кантице_џема_решење_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење
   
   .. activecode:: кантице_џема_решење
    
      baka = 2480
      mama = baka*2
      ukupno = baka + mama
      u_kantici = ukupno / 6
      print(u_kantici)

.. questionnote::

   Напиши програм који израчунава збир цифара датог двоцифреног броја.


.. activecode:: збир_цифара
   :runortest: broj, zbir

   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   broj = 58
   # -*- acsection: main -*-
   
   # -*- acsection: after-main -*-
   print(zbir)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for broj, zbir in [(58, 13), (84, 12), (12, 3), (33, 6), (80, 8)]:
             self.assertEqual(acMainSection(broj = broj)["zbir"],zbir,"Збир цифара броја %s је %s." % (broj, zbir))
   myTests().main()
   
   
.. reveal:: збир_цифара_решење_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   .. activecode:: збир_цифара_решење

      broj = 58
      desetica = broj // 10
      jedinica = broj % 10
      zbir = desetica + jedinica
      print(zbir)

Број станова по спрату
''''''''''''''''''''''
.. level:: 2
   
.. questionnote::

   У једној згради на сваком спрату има исти број станова, осим у
   приземљу, где је остављен већи простор за ходник, па су станови
   мањи и има их мање него на осталим спратовима. Напиши програм који
   од корисника тражи да унесе укупан број станова у згради и број
   станова по спрату и исписује колико има станова у приземљу и колики
   је број спратова (не рачунајући приземље).

Ако имамо :math:`n` спратова (не рачунајући приземље) и на сваком
спрату :math:`s` станова, а у приземљу :math:`p` станова, тада је
укупан број станова :math:`u` једнак :math:`n \cdot s + p`, при чему
знамо да је :math:`0 \leq p < s`. Отуда следи да је :math:`n` целобројни
количник укупног броја станова и броја станова по спрату, а да је
:math:`p` остатак при том дељењу. Теби остаје да исправиш програм тако
да од корисника тражи да унесе улазне податке и да на крају кориснику
пријавиш одговарајуће резултате - потруди се да током уноса података и
уз резултате испишеш и пропратни текст да би кориснику било што
јасније шта твој програм ради.

.. activecode:: број_станова_по_спрату

   ukupno_stanova = 0    # ispravi ovaj red tako da korisnik unosi broj stanova
   stanova_po_spratu = 0 # ispravi ovaj red tako da korisnik unosi broj stanova po spratu
   broj_spratova       = ukupno_stanova // stanova_po_spratu
   stanova_u_prizemlju = ukupno_stanova % stanova_po_spratu
   print()               # ispravi ovaj red tako da se korisniku ispišu rezultati u razumljivom obliku
      

Размена цифара
''''''''''''''
.. level:: 2

.. questionnote::

   Напиши програм који размењује цифру хиљада и стотина унетог
   броја. Нпр. за унети број 123456 програм исписује 124356.

.. activecode:: размена_цифара

   n = int(input())
   c2 = 0   # popravi tako da se odredjuje cifra stotina
   c3 = 0   # popravi tako da se odredjuje cifra hiljada
   m = 0    # popravi tako da se razmenjuju cifre
   print(m)
   
.. reveal:: размена_цифара_решење_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење
   
   .. activecode:: размена_цифара_решење

      n = int(input())
      c2 = (n // 100) % 10 
      c3 = (n // 1000) % 10
      m = n - c2*100 - c3*1000 + c3*100 + c2*1000
      print(m)
      
Уграђене функције - задаци
::::::::::::::::::::::::::

Апсолутна вредност унетог реалног броја
'''''''''''''''''''''''''''''''''''''''
.. level:: 1

.. questionnote::

   Напиши програм који израчунава апсолутну вредност унетог реалног
   броја.

.. activecode:: апсолутна_вредност

   broj = float(input())
   print(broj) # ispravi ovaj red
   

Старија и млађа ћерка
'''''''''''''''''''''
.. level:: 1
   
.. questionnote::

   Марија има две ћерке. Напиши програм који на основу њихових година
   одређује и исписује колико година има старија, а колико година има
   млађа од њих.

.. activecode:: старија_и_млађа_ћерка
   :runortest: godine1, godine2, starija, mladja

   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   godine1 = 13
   godine2 = 8
   # -*- acsection: main -*-
   
   # -*- acsection: after-main -*-
   print(starija, mladja)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for godine1, godine2, starija, mladja in [(3, 5, 5, 3), (13, 8, 13, 8), (4, 2, 4, 2), (7, 15, 15, 7)]:
             self.assertEqual((acMainSection(godine1 = godine1, godine2 = godine2)["starija"], acMainSection(godine1 = godine1, godine2 = godine2)["mladja"]),(starija, mladja),"Ако је број година Маријиних ћерки %s и %s, тада старија има %s, а млађа %s." % (godine1, godine2, starija, mladja))
   myTests().main()

.. reveal:: старија_и_млађа_ћерка_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење
   
   .. activecode:: старија_и_млађа_ћерка_решење
    
      godine1 = 13
      godine2 = 8
      starija = max(godine1, godine2)
      mladja = min(godine1, godine2)
      print(starija, mladja)

Разлика у годинама између две ћерке
'''''''''''''''''''''''''''''''''''
.. level:: 1
      
.. questionnote::

   Напиши програм који одређује колика је разлика у годинама између
   две Маријине ћерке.

   
.. activecode:: старија_и_млађа_ћерка_разлика
   :runortest: godine1, godine2, razlika

   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   godine1 = 13
   godine2 = 8
   # -*- acsection: main -*-
   
   # -*- acsection: after-main -*-
   print(razlika)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for godine1, godine2, razlika in [(3, 5, 2), (13, 8, 5), (4, 2, 2), (7, 15, 8)]:
             self.assertEqual((acMainSection(godine1 = godine1, godine2 = godine2)["razlika"]),razlika,"Ако је број година Маријиних ћерки %s и %s, тада је разлика њихових година %s." % (godine1, godine2, razlika))
   myTests().main()

.. reveal:: старија_и_млађа_ћерка_разлика_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   Једно решење можемо добити ако употребимо решење претходног задатка
   да бисмо одредили колико година има старија, а колико млађа ћерка,
   и онда се израчуна њихова разлика.
	       
   .. activecode:: старија_и_млађа_ћерка_разлика_решење1
    
      godine1 = 13
      godine2 = 8
      starija = max(godine1, godine2)
      mladja = min(godine1, godine2)
      razlika = starija - mladja
      print(razlika)

   Једноставније решење је ако израчунамо апсолутну вредност разлике
   њихових година.

   .. activecode:: старија_и_млађа_ћерка_разлика_решење2
    
      godine1 = 13
      godine2 = 8
      razlika = abs(godine1 - godine2)
      print(razlika)

Разлика у годинама између најстаријег и најмлађег сина
''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. level:: 1
      
.. questionnote::

   Срђан има три сина. Напиши програм који одређује колика је разлика
   у годинама између најстаријег и најмлађег.

.. activecode:: најстарији_и_најмлађи_син
   :runortest: godine1, godine2, godine3, razlika

   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   godine1 = 13
   godine2 = 8
   godine3 = 10
   # -*- acsection: main -*-
   
   # -*- acsection: after-main -*-
   print(razlika)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for godine1, godine2, godine3, razlika in [(3, 5, 9, 6), (13, 8, 10, 5), (4, 2, 4, 2), (17, 7, 9, 10)]:
             self.assertEqual(acMainSection(godine1 = godine1, godine2 = godine2, godine3 = godine3)["razlika"],razlika,"Ако је број година Срђанових синова %s, %s и %s, тада је распон њихових година %s." % (godine1, godine2, godine3, razlika))
   myTests().main()

.. reveal:: најстарији_и_најмлађи_син_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење
   
   .. activecode:: најстарији_и_најмлађи_син_решење
    
      godine1 = 13
      godine2 = 8
      godine3 = 10
      najstariji = max(godine1, godine2, godine3)
      najmladji = min(godine1, godine2, godine3)
      razlika = najstariji - najmladji
      print(razlika)

Разлика вредности цифара
''''''''''''''''''''''''
.. level:: 2

.. questionnote::

   Напиши програм који одређује за колико се разликују мања и већа
   цифра у запису двоцифреног броја.

.. activecode:: разлика_цифара
   :runortest: broj, razlika

   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   broj = 58
   # -*- acsection: main -*-
   
   # -*- acsection: after-main -*-
   print(razlika)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for broj, razlika in [(58, 3), (84, 4), (12, 1), (33, 0)]:
             self.assertEqual(acMainSection(broj = broj)["razlika"],razlika,"Разлика цифара броја %s је %s." % (broj, razlika))
   myTests().main()
   
   
   
.. reveal:: разлика_цифара_решење_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   .. activecode:: разлика_цифара_решење

      broj = 58
      desetica = broj // 10
      jedinica = broj % 10
      razlika = max(desetica, jedinica) - min(desetica, jedinica)
      print(razlika)
      
Дефинисање функција - задаци
::::::::::::::::::::::::::::

Обим троугла
''''''''''''
.. level:: 1

  
.. questionnote::

   Дефиниши функцију која израчунава обим троугла ако су познате
   дужине његове три странице. Употреби је да израчунаш обим
   Питагориног троугла коме су дужине страница 3, 4 и 5.

.. activecode:: обим_троугла_три_странице

   def obim_trougla(a, b, c):
       return 0   # ispravi ovaj red

   print(obim_trougla(0, 0, 0)) # ispravi ovaj red

Миље у километре
''''''''''''''''
.. level:: 1
   
.. questionnote::

   У САД се за мерење растојања између градова користе миље. Једна
   миља има 1,609 километара. Дефиниши функцију која на основу
   растојања у миљама израчунава растојање у километрима. Употреби је
   након тога да прерачунаш 3 миље, 5 миља и 7.5 миља у километре.


.. activecode:: миље_у_километре

   def milje_u_kilometre(mi):
       return 0   # ispravi ovaj red

   print(milje_u_kilometre(3))
   # dopuni kod

Степени Фаренхајта у степене Целзијуса
''''''''''''''''''''''''''''''''''''''
.. level:: 1

.. questionnote::

   У САД се температура мери у степенима Фаренхајта. 32 степена
   Фарехнајта је 0 степни Целзијуса. Сваких наредних 9 степени
   Фаренхајта додаје 5 степени Целзијуса (тако је 41 степен Фаренхајта
   једнак 5 степени Целзијуса, 50 степни Фаренхајта једнаки су 10
   степени Целзијуса итд.). Дефиниши функцију која на основу степени
   Фаренхајта одређује температуру у степенима Целзијуса.

.. activecode:: фаренхајти_у_целзијусе

   def farenhajt_u_celzijus(f):
       c = 0     # ispravi ovaj red
       return c
   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
          for (f, c) in [(32, 0), (41, 5), (50, 10), (68, 20), (99, 37.2222222222)]:
             self.assertAlmostEqual(farenhajt_u_celzijus(f), c, 5, "%s степени Фаренхајта једнако је %s степени Целзијуса." % (f, c))

   myTests().main()

Функција за обим и површину круга
'''''''''''''''''''''''''''''''''
.. level:: 2
                
.. questionnote::

   Дефиниши функцију која израчунава обим и површину круга по
   формулама :math:`O = 2\cdot r\cdot \pi` и :math:`P = r^2\pi`. Број
   :math:`\pi` можеш добити помоћу ``math.pi``.
         

.. activecode:: обим_и_површина_кругаa

   def obim_i_povrsina_kruga(r):
       return (0, 0)    # ispravi ovaj red
  
   (O, P) = obim_i_povrsina_kruga(1)
   print(O, P)

Скраћивање разломака
''''''''''''''''''''
.. level:: 2
   
.. questionnote::

   Дефиниши функцију којом се врши скраћивање датог
   разломка. Претпостави да на располагању имаш функцију која одређује
   НЗД два броја.

.. activecode:: скраћивање_разломка

   def nzd(a, b):
       while b != 0:
           a, b = b, a % b
       return a

   def skrati(a, b):
       return (0, 0)   # ispravi ovaj red

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
          self.assertEqual(skrati(16, 6), (8, 3), "16/6 = 8/3")
          self.assertEqual(skrati(24, 16), (3, 2), "24/16 = 3/2")
          self.assertEqual(skrati(9, 5), (9, 5), "9/5 = 9/5")
   myTests().main()
   
