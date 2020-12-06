8.5. Вежбање
############

На крају ти остављамо неколико задатака за вежбу. Оне задатке које не
стигнеш да урадиш на часу уради за домаћи задатак.


Полице са књигама
'''''''''''''''''

.. questionnote::

   На првој полици има 150 књига. На другој има дупло мање него на
   првој, а на трећој три пута мање него на другој. Колико је укупно
   књига на полицама.

.. activecode:: Полице_са_књигама

  polica1 = 150
  polica2 = polica1 / 2
  polica3 = polica2 / 3
  ukupno = polica1 + polica2 + polica3
  print(ukupno)

Приметимо да се као резултат добија број ``250.0`` уместо ``250``. То
је због тога што се након примене операције реалног дељења (операције
``/``) добије увек резултат у облику реалног броја. Пошто је број
књига цео број и пошто је број 150 дељив и са 2, а број 75 са 3 (иначе
задатак не би имао смисла) на овом месту је било могуће употребити и
операцију целобројног дељења о којој ће више речи бити у наставку.


Прочитане стране књиге
''''''''''''''''''''''

.. questionnote::

   Књига има 282 стране. Марко је првог дана прочитао трећину, другог
   дана половину остатка, а трећег књигу прочитао до краја. Колико
   страна је прочитао ког дана? Напиши програм тако да исправно ради
   и ако је број страна првог дана другачији.

.. activecode:: Читање
   :runortest: broj_strana, prvi_dan, drugi_dan, treci_dan
   :enablecopy:

   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   broj_strana = 282
   # -*- acsection: main -*-
   prvi_dan = 0      # ispravi ovaj red
   drugi_dan = 0     # ispravi ovaj red
   treci_dan = 0     # ispravi ovaj red
   # -*- acsection: after-main -*-
   print(prvi_dan, drugi_dan, treci_dan)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for broj_strana, dan in [(369, 123), (333, 111)]:
             self.assertEqual(acMainSection(broj_strana = broj_strana)["prvi_dan"],dan,"Ако књига има %s страна, први дан је прочитано %s страна." % (broj_strana,dan))
             self.assertEqual(acMainSection(broj_strana = broj_strana)["drugi_dan"],dan,"Ако књига има %s страна, други дан је прочитано %s страна." % (broj_strana,dan))
             self.assertEqual(acMainSection(broj_strana = broj_strana)["treci_dan"],dan,"Ако књига има %s страна, трећи дан је прочитано %s страна." % (broj_strana,dan))
   myTests().main()
   

.. reveal:: пресек_решење11
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   Марко је прочитао 94 стране сваког дана. Првог дана је прочитао
   трећину и остале су му две трећине. Другог дана је прочитао пола од
   тога тј. опет трећину и за трећи дан му је остала последња трећина.
	       
   .. activecode:: Читање_решење

      broj_strana = 282		
      prvi_dan = broj_strana / 3
      drugi_dan = (broj_strana - prvi_dan) / 2
      treci_dan = broj_strana - prvi_dan - drugi_dan
      print(treci_dan)


Разломак у мешовити број
''''''''''''''''''''''''

.. questionnote:: 

   Бројилац разломка је 37, а именилац је 12. Преведи овај разломак у
   мешовит број.

Важи да је :math:`37 = 3 \cdot 12 + 1`, па је :math:`\frac{37}{12} =
\frac{3 \cdot 12 + 1}{12} = 3 \frac{1}{12}`. У општем случају када
разломак :math:`\frac{a}{b}` преводимо у мешовит број потребно је да
бројилац напишемо у облику :math:`a = q \cdot b + r`, при чему мора да
важи да је :math:`0 \leq r < b` и тада се добија межовити број
:math:`q \frac{r}{b}`. Број :math:`q` је целобројни количник бројева
:math:`a` и :math:`b`, док је :math:`r` остатак при њиховом дељењу.

.. activecode:: Мешовит_број

   brojilac = 37
   imenilac = 12
   mesoviti_ceo_deo = 0  # ispravi ovaj red
   mesoviti_brojilac = 0 # ispravi ovaj red
   mesoviti_imenilac = 0 # ispravi ovaj red
   print(mesoviti_ceo_deo, "celih i", mesoviti_brojilac, "/", mesoviti_imenilac)

Наравно, резултат треба да буде ``3 celih i 1 / 12``.
      
.. reveal:: пресек_решење31
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење
      
   .. activecode:: Мешовит_број_решење

      brojilac = 37
      imenilac = 12
      mesoviti_ceo_deo = brojilac // imenilac
      mesoviti_brojilac = brojilac % imenilac
      mesoviti_imenilac = imenilac
      print(mesoviti_ceo_deo, "celih i", mesoviti_brojilac, "/", mesoviti_imenilac)
