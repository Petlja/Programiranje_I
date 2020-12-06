9.4. Вежбање
############

На крају ти остављамо неколико задатака за вежбу. Оне задатке које не
стигнеш да урадиш на часу уради за домаћи задатак.


Време чекања на станици
'''''''''''''''''''''''

.. questionnote::

   Јелена је дошла аутобусом на станицу у s1 сати и m1 минута, док је
   Иванин аутобус стигао у s2 сати и m2 минута. Колико је сати и
   минута она која је прва стигла чекала ону која је друга стигла?

И у овом задатку се тражи да се израчуна растојање између два
временска тренутка за које се не зна који је први, а који други. Као
што смо приказали раније, рачунање растојања се своди на рачунање
апсолутне вредности разлике, а рад са сатима и минутима лакше обављамо
ако прво претворимо све у минуте, затим израчунамо број минута колико
су се чекале и након тога то претворимо у сате и минуте.
   
.. activecode:: чекање_на_станици
   :runortest: s1, m1, s2, m2, s, m
      
   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   s1 = int(input())
   m1 = int(input())
   s2 = int(input())
   m2 = int(input())
   # -*- acsection: main -*-
   vreme1 = 0  # pretvori u ovom redu s1 sati i m1 minuta u minute
   vreme2 = 0  # pretvori u ovom redu s2 sati i m2 minuta u minute
   vreme = 0   # izracunaj u ovom redu duzinu cekanja u minutima
   s = 0       # u ovom redu izracunaj broj sati cekanja
   m = 0       # u ovom redu broj minuta cekanja
   # -*- acsection: after-main -*-
   print(s, m)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):

       def testOne(self):
          for (s1, m1, s2, m2, s, m) in [(9, 35, 12, 12, 2, 37), (11, 40, 12, 10, 0, 30), (10, 15, 8, 50, 1, 25)]:
             self.assertEqual((acMainSection(s1 = s1, m1 = m1, s2 = s2, m2 = m2)["s"], acMainSection(s1 = s1, m1 = m1, s2 = s2, m2 = m2)["m"]),  (s, m) ,"Ако је Јелена стигла у %s:%s, а Ивана у %s:%s, онда је Јелена чекала Ивану %s сата и %s минута." % (s1, m1, s2, m2, s, m))
   myTests().main()

.. reveal:: чекање_на_станици_решење1
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   .. activecode:: чекање_на_станици_решење2
		
      s1 = int(input())
      m1 = int(input())
      s2 = int(input())
      m2 = int(input())
      vreme1 = s1*60 + m1
      vreme2 = s2*60 + m2
      vreme = abs(vreme1 - vreme2)
      s = vreme // 60
      m = vreme % 60
      print(s, "sati i", m, "minuta")

Менхетн растојање
'''''''''''''''''
      
.. questionnote::

   Менхетн, део града Њујорка је организован у авеније у правцу
   север-југ и улице у правцу isток-запад. Размак између две улице је
   80m, а између две авеније је 275m. Ако се Том налази на углу улице
   :math:`u_1` и авеније :math:`a_1` и жели да стигне на угао улице
   :math:`u_2` и авеније :math:`a_2`, колико ће метара морати да
   пређе.

.. image:: ../../_images/manhattan_distance.png
   :width: 500px   
   :align: center

Том има више начина да стигне са једног на друго место (може да иде
цик-цак, на разне начине), међутим, пређено растојање је исто као када
би прво ишао улицом :math:`u_1` све док не дође до угла са авенијом
:math:`a_2`, а затим да се креће авенијом :math:`а_2` све док не дође
до угла са улицом :math:`u_2`. Дакле, потребно је израчунати растојање
између авенија :math:`a_1` и :math:`a_2` (да би се оно добило у
метрима потребно је помножити апсолутну разлику између њихових редних
бројева размаком између суседних авенија) и на то додати растојање
између улица :math:`u_1` и :math:`u_2` (да би се оно добило у метрима
потребно је помножити апсолутну разлику између њихових редних бројева
размаком између суседних улица).
	   
Исправи наредни код тако да коректно израчуна пређени пут (наравно, програм
треба да ради и када се улазни подаци промене или учитају са улаза).
	   
.. activecode:: менхетн
   :runortest: ulica1, avenija1, ulica2, avenija2, rastojanje, razmak_ulica, razmak_avenija

   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   razmak_ulica = 80	
   razmak_avenija = 275
   ulica1 = 51
   avenija1 = 6
   ulica2 = 58
   avenija2 = 3
   # -*- acsection: main -*-
   rastojanje = abs(avenija1 - avenija2) * 0 + \
                0 * razmak_ulica
   # -*- acsection: after-main -*-
   print(rastojanje)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):

       def testOne(self):
          for (ulica1, avenija1, ulica2, avenija2, razmak_ulica, razmak_avenija, rastojanje) in [(3, 5, 8, 4, 80, 275, 675), (1, 7, 2, 4, 80, 275, 905), (9, 4, 11, 2, 80, 275, 710), (4, 8, 1, 5, 80, 275, 1065)]:
             self.assertEqual((acMainSection(ulica1 = ulica1, avenija1 = avenija1, ulica2 = ulica2, avenija2 = avenija2, razmak_ulica = razmak_ulica, razmak_avenija = razmak_avenija)["rastojanje"]),  rastojanje , "Растојање између тачака (%s, %s) и (%s, %s) је %s." % (ulica1, avenija1, ulica2, avenija2, rastojanje))
   myTests().main()
   

Приметимо да је формула у претходном примеру била веома дугачка и
проценили смо да је прегледније да је одштампамо кроз више редова. Да
бисмо нагласили да се нека наредба наставља и у следећој линији на
крај линије стављамо симбол ``\``.

.. reveal:: менхетн_решење1
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   .. activecode:: менхетн_решење2

      ulica1 = 51
      avenija1 = 6
      ulica2 = 58
      avenija2 = 3
      razmak_ulica = 80		
      razmak_avenija = 275
      rastojanje = abs(avenija1 - avenija2) * razmak_avenija + \
                   abs(ulica1 - ulica2) * razmak_ulica
      print(rastojanje)

Просек 3 броја
''''''''''''''

.. questionnote::

   Димитрије, Ања, Ивона и Марко су високи редом 165, 162, 158 и
   171 cm. Пријављују трочлану екипу за школски турнир у кошарци и у
   формулару је неопходно да наведу просечну висину своје екипе, али
   се још нису одлучили ко ће сачињавати екипу. Дефиниши функцију за
   израчунавање просека три броја, а затим испиши просечне висине за
   сваку од 4 могуће варијанте трочлане екипе.

   
.. activecode:: просек3броја

   # definiši funkciju prosek koja izračunava prosek 3 data broja
   def ...

   dimitrije = 165
   anja = 162
   ivona = 158
   marko = 171
   print("Anja, Ivona, Marko:", prosek(anja, ivona, marko))
   print("Dimitrije, Ivona, Marko:", prosek(dimitrije, ivona, marko))
   # dopuni program za preostale dve kombinacije
