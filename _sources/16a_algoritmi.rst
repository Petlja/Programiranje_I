Основни алгоритми - пресликавање, филтрирање, претрага
======================================================

Пресликавање
~~~~~~~~~~~~

У неким ситуацијама потребно је применити једну те исту формулу на више различитих вредности. Такве задатке смо и до сада сретали.
Површине свих квадрата

Површине свих квадрата

.. questionnote::

   Напиши програм који исписује таблицу површина квадрата за све
   дужине странице од 1 до 10.

Један начин да се то уради је да у петљи прођемо кроз све вредности од 1 до 10 и да у телу петље за сваку ту вреднос израчунамо квадрат и испишемо га.

.. activecode:: површине_квадрата_1

  for a in range(1, 10):
      print("Stranica:", a, "Povrsina:", a * a)

Израчунавање површине може бити и урађено уз помоћ посебне функције.

.. activecode:: површине_квадрата_2

  def povrsina(a):
      return a * a

  stranice = [13, 18, 43, 11, 8]
  for a in stranice:
      print("Stranica:", a, "Povrsina:", povrsina(a))

Погледај и следеће задатке:

- `Обим троугла <https://petlja.org/biblioteka/r/lekcije/prirucnik-python-gim/osnovnialgoritmi-cas16#id6>`__
- `Ципирипи <https://petlja.org/biblioteka/r/lekcije/prirucnik-python-gim/osnovnialgoritmi-cas16#id8>`__

Филтрирање
~~~~~~~~~~

У многим задацима је потребно одредити који од неколико датих елемената задовољавају неки дати услов. Посматрајмо, на пример, наредни задатак.

Аква парк

.. questionnote::

   У аква-парку на тобоган могу да иду само ђаци који су високи бар
   140 центиметара. Ако су познате висине неколико деце, испиши имена
   оних који могу да користе тобоган.

Ако је дат мали број деце (на пример, троје), јасно је да је ово само једноставна вежба гранања.

.. activecode:: ко_може_на_тобоган_1

   pera = 135
   if pera >= 140:
       print pera, "može na tobogan"
   ivana = 142
   if ivana >= 140:
       print ivana, "može na tobogan"
   laza = 146
   if laza >= 140:
       print mika, "može na tobogan"

Додавањем грана else можемо уједно и пријавити ко од њих не може на тобоган.

.. activecode:: ко_може_на_тобоган_1_else

   pera = int(input("Kolika je tvoja visina:"))
   if pera >= 140:
       print pera, "može na tobogan"
   else:
       print pera, "ne može na tobogan"
   ivana = 142
   if ivana >= 140:
       print ivana, "može na tobogan"
   else:
       print ivana, "ne može na tobogan"
   laza = 146
   if laza >= 140:
       print mika, "može na tobogan"
   else:
       print laza, "ne može na tobogan"

Приметимо да се за свако дете понавља исти код, тако да је задатак много боље решити уз помоћ петље (чак и када је број деце мали). Исправи услов у наредном програму тако да ради исто као и претходни.

.. activecode:: ко_може_на_тобоган_2

   for i in range(3):
       visina = int(input("Kolika je tvoja visina:"))
       if True:  # ispravi ovaj uslov
           print visina, "može na tobogan"

Погледај и следеће задатке:

- `Сви парни бројеви <https://petlja.org/biblioteka/r/lekcije/prirucnik-python-gim/osnovnialgoritmi-cas16#id17>`__
- `Сви самогласници <https://petlja.org/biblioteka/r/lekcije/prirucnik-python-gim/osnovnialgoritmi-cas16#id19>`__

Комбиновање елементарних алгоритама
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Алгоритам филтрирања се може једноставно комбиновати са алгоритмима које смо раније описали (сабирања, множења, бројања, налажења минимума и максимума).
Број самогласника

.. questionnote::

   Напиши програм који израчунава и исписује број самогласника у
   унетој линији текста.

.. activecode:: број_самогласника

   rec = input("Unesi jednu reč:")
   broj_samoglasnika = 0
   for slovo in rec:
       if slovo.lower() in {'a', 'e', 'i', 'o', 'u'}:
           # popravi naredni red tako da ažurira ispravno broj samoglasnika
           broj_samoglasnika = 0
   print("Broj samoglasnika:", broj_samoglasnika)

Погледај и следеће задатке:

- `Број лоптица Карела <https://petlja.org/biblioteka/r/lekcije/prirucnik-python-gim/osnovnialgoritmi-cas16#id26>`__
- `Просечан број поена такмичара који су се квалификовани <https://petlja.org/biblioteka/r/lekcije/prirucnik-python-gim/osnovnialgoritmi-cas16#id27>`__

Претрага
~~~~~~~~
Претрагом можемо проверити да ли у листи постоји елемент који задовољава неки услов (на пример, да ли међу бројевима постоји неки број који је паран или да ли међу речима постоји нека која почиње самогласником). Веома слични проблеми томе су да се провери да ли сви елементи листе задовољавају неки услов (на пример, да ли су сви бројеви позитивни), да ли постоји неки елемент који не задовољава услов или да ли ниједан од елемената не задовољава услов. Могуће је одређивати и на којој се позицији налази елемент који задовољава услов и слично.
Да ли су сви одлични?

На пример, да бисмо проверили да ли су сва три другара одлични ученици и могу да уђу бесплатно на базен, можемо употребити следећи услов.

.. activecode:: pretraga_svi_odlicni

   prosek_ognjen = 4.75
   prosek_mira = 5.00
   prosek_jelica = 5.00
   if prosek_pera >= 4.50 and prosek_mira >= 4.50 and prosek_jelica >= 4.50:
       print("Svi učenici su odlični")
   else:
       print("Nisu svi učenici odlični")

Слично, проверу да ли је бар један од ученика одличан, могли бисмо реализовати на следећи начин.

.. activecode:: pretraga_postoji_odlican

   prosek_ognjen = 4.25
   prosek_mira = 4.75
   prosek_jelica = 5.00
   if prosek_pera >= 4.50 or prosek_mira >= 4.50 or prosek_jelica >= 4.50:
       print("Bar jedan od učenika jeste odličan")
   else:
       print("Nijedan učenik nije odličan")

