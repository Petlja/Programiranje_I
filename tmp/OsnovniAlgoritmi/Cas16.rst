Час 16 - Основни алгоритми - пресликавање, филтрирање, претрага
###############################################################

   
Пресликавање
------------

У неким ситуацијама потребно је применити једну те исту формулу на
више различитих вредности. Такве задатке смо и до сада сретали.


Површине свих квадрата
''''''''''''''''''''''

.. questionnote::

   Напиши програм који исписује таблицу површина квадрата за све
   дужине странице од 1 до 10.

Један начин да се то уради је да у петљи прођемо кроз све вредности од
1 до 10 и да у телу петље за сваку ту вреднос израчунамо квадрат и
испишемо га. 

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

Обими троуглова
'''''''''''''''
      
Слично можемо израчунати и обиме троуглова чије су дужине страница
дате у листи. 
  
.. activecode:: обими_троуглова

  def obim(a, b, c):
      # ispravi naredni red tako da ispravno izračunava obim
      return 0

  trouglovi = [(3, 4, 5), (5, 12, 13), (7, 24, 25)]
  for trougao in trouglovi:
      print(obim(*trougao))

Приметимо један детаљ у претходном задатку. Функција прима три
параметра, ``a``, ``b`` и ``c``, а чланови листе су уређене тројке.
Да би се уређена тројка распаковала и да би се функцији проследила три
параметра, употребљен је симбол ``*``.

Ципирипи
''''''''

Током 1980-их година постојала је једна симпатична реклама за крем
Ципирипи у којој је у тексту песмице сваки самогласник (``а``, ``е``,
``и``, ``о``, ``у``) мењан у ``и``.

.. youtube:: JWorYHJiWnQ
    :width: 560
    :align: center

Напиши програм који извршава ту трансформацију текста.
	    
.. activecode:: ципирипи

   # funkcija sve samoglasnike pretvara u "i", a ostala slova ne menja
   def samoglasnici_u_i(slovo):
       if slovo in {"a", "e", "i", "o", "u"}:
           return ""    # ispravi ovaj red
       else:
           return ""    # ispravi ovaj red

   tekst = """
   daj cipiripi, daj cipiripi
   od čokolade i lešnika
   jer nema ničeg lepšeg
   od cipiripija
   """

   for slovo in tekst:
       print(samoglasnici_u_i(slovo), end='')

Пресликавње компрехенсијом
''''''''''''''''''''''''''

Језик Python нуди и посебан начин да се нека формула примени на сваки
елемент листе или скупа. У математици сте виђали запис :math:`\{a^2\
|\ a \in S\}`, који означава скуп квадрата бројева :math:`a` за све
вредности :math:`a` које припадају скупу :math:`S`. Овоме одговара
запис ``{a * a for a in S}``, а уместо скупова могу се користити и
листе ``[a * a for a in S]``. Приметимо да спољашње заграде одређују
да ли се гради скуп или листа вредности, да се уместо усправне црте
користи реч ``for`` а уместо симбола :math:`\in` реч ``in``. На тај
начин можемо одредити површине квадрата чије су странице дате у листи
и без коришћења класичне петље.
     
.. activecode:: површине_квадрата_3
   
  stranice = [13, 18, 43, 11, 8]
  povrsine = [a * a for a in stranice]
  print(povrsine)

Поново је могуће користити и помоћну функцију за израчунавање
површине, а могуће је као изворну листу употребити и функцију
``range``.
  
.. activecode:: површине_квадрата_4
   
  def povrsina(a):
      return a * a

  # ispravi naredni red tako što ćeš pozvati funkciju za površinu
  povrsine = [ _ for a in range(1, 10)]
  print(povrsine)
      
Филтрирање
----------

У многим задацима је потребно одредити који од неколико датих
елемената задовољавају неки дати услов. Посматрајмо, на пример,
наредни задатак.

Аква парк
'''''''''

.. questionnote::

   У аква-парку на тобоган могу да иду само ђаци који су високи бар
   140 центиметара. Ако су познате висине неколико деце, испиши имена
   оних који могу да користе тобоган.

Ако је дат мали број деце (на пример, троје), јасно је да је ово само
једноставна вежба гранања.

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

Додавањем грана ``else`` можемо уједно и пријавити ко од њих не може
на тобоган.

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

Приметимо да се за свако дете понавља исти код, тако да је задатак
много боље решити уз помоћ петље (чак и када је број деце
мали). Исправи услов у наредном програму тако да ради исто као и
претходни.
      
.. activecode:: ко_може_на_тобоган_2

   for i in range(3):
       visina = int(input("Kolika je tvoja visina:"))
       if True:  # ispravi ovaj uslov
           print visina, "može na tobogan"

Сви парни бројеви
'''''''''''''''''
           
.. questionnote::

   Као део софтвера који обучава децу елементарној математици
   постављен нам је задатак да напишемо део програма који одређује све
   парне бројеве у некој датој листи.

Структура програма је поново иста - петља која пролази кроз све
елементе серије и гранање унутар петље којим се проверава да ли текући
елемент задовољава услов. У овом примеру потребно је проверити да ли
је број паран, што се, подсећамо те, може урадити тако што се провери
да ли је његов остатак при дељењу са 2 једнак нули. Поправи наредни
програм у складу са тим.
	
.. activecode:: парни_бројеви

   brojevi = [5, 3, 2, 1, 8, 4, 7, 6]
   for broj in brojevi:
       if True:  # popravi ovu liniju tako što ćeš proveriti da li je broj paran
           print("Paran: ", broj)

Сви самогласници
''''''''''''''''
           
.. questionnote::	 

   Напиши програм који пријављује све самогласнике који се јављају у
   датој линији текста.

Структура програма је опет иста - у петљи пролазимо слово по слово
речи и у телу петље за свако слово провервамо да ли је самогласник.
	 
.. activecode:: самогласници

   rec = input("Unesi jednu reč:")
   # popravi narednu liniju tako da se u petlji prolazi slovo po slovo reči
   for _ in _:
       # popravi narednu liniju tako što ćeš proveriti da li je slovo samoglasnik 
       if True:
           print("Samoglasnik:", slovo)

Филтрирање помоћу компрехенсије
'''''''''''''''''''''''''''''''

Слично као што смо за пресликавање користили запис који подсећа на
скупове у математици и за филтрирање је могуће учинити нешто слично.
У математици можемо користити запис :math:`\{x\ |\ x \in S, P(x)\}`
што означава скуп свих оних елемената :math:`x` који припадају скупу
:math:`S` и уз то задовољавају и неко својство :math:`P`. На пример,
скуп позитивних елемената скупа целих бројева :math:`Z` се може
означити са :math:`\{x\ |\ x \in Z, x > 0\}`. У језику Python подржан
је веома сличан запис. ``{x for x in S if P(x)}`` означава скуп свих
елемената ``x`` који припадају ``S`` и за које важи услов
``P``. Слично, ``[x for x in S if P(x)]`` означава листу таквих
елемената. На пример, листа парних елемената из листе ``l`` се може
изградити са ``[x for x in l if x % 2 == 0]``.

.. questionnote::

   Дата је листа температура у току неколико дана. Направи листу оних
   температура које су током тог периода биле изнад нуле.
   
.. activecode:: негативне_температуре

   temperature = [2, -1, 0, -8, -10, -1, 4, 5, 8, 6]
   # ispravi naredni red tako što ćeš umesto _ staviti odgovarajuće reči
   negativne_temperature = [t _ t _ temperature _ t > 0]
   print(negativne_temperature)


Комбиновање елементарних алгоритама
-----------------------------------
           
Алгоритам филтрирања се може једноставно комбиновати са алгоритмима
које смо раније описали (сабирања, множења, бројања, налажења минимума
и максимума).

Број самогласника
'''''''''''''''''

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

Број лоптица испред Карела
''''''''''''''''''''''''''
   
.. questionnote::

   Карел се налази на почетку лавиринта и занима га колико се лоптица
   налази испред њега. Напиши програм који му у томе помаже.

   Робот се помера једно по једно поље све до краја лавиринта. За
   свако поље се проверава да ли на њему постоји лоптица и ако
   постоји, тада је робот yзима и увећава бројач лоптица за један.
   
.. karel:: карел_broji_loptice
   
   {
      setup: function() {
           function random(n) {
              return Math.floor(n * Math.random());
	   }

           var dim = 3 + random(3);
	   var world = new World(dim, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           var robot = new Robot();
           numBalls = 0;
           for (var k = 2; k <= dim; k++)
              if (random(2) == 0) {
                 world.putBall(k, 1);
                 numBalls++;
              }
	   
	   var code = ["from karel import *",
	                   "broj = 0",
			   "while moze_napred():",
			   "    napred()",
			   "    # dodaj proveru da li se na ovom polju nalazi loptica",
			   "izgovori(broj)"];
	   return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
           return robot.getBalls() == numBalls && numBalls == parseInt(robot.lastMessage);
      }
   }

Просечан број поена такмичара који су се квалификовали
''''''''''''''''''''''''''''''''''''''''''''''''''''''
   
.. questionnote::

   На такмичењу су учествовали ђаци и позната је листа која садржи
   имена ученика и освојени број поена. На наредни ниво такмичења су
   се пласирали сви они ученици који су освојили 50 и више
   поена. Напиши програм који израчунава просечан број поена ученика
   који су се пласирали даље.

Основна структура програма је поново заснована на филтрирању. У петљи
се пролази кроз листу парова, у телу петље се врши провера да ли се
ученик пласирао (провером његовог броја поена) и ако јесте, онда се
врши ажурирање броја пласираних и збира поена свих пласираних
такмичара.

.. activecode:: просек_такмичара_који_су_се_пласирали_1

   takmicari = [("Pera", 38), ("Milica", 74), ("Laza", 65), ("Jovana", 44)]
   broj = 0
   zbir = 0
   for (ime, poeni) in takmicari:
       # Dopuni ovaj deo programa:
       # proveri da li se takmičar plasirao i ako jeste, ažuriraj
       # broj i zbir poena onih koji su se plasirali
   print("Prosek:", zbir / broj)


Коришћењем компрехенсије задатак можемо решити још једноставније, тако
што ћемо прво изградити листу поена такмичара који су се пласирали, а
онда наћи просек елемената те листе (тако што ћеш збир елемената те
листе поделити њеним бројем елемената, тј. њеном дужином) - тај
последњи део задатака теби препуштамо да допуниш.
   
.. activecode:: просек_такмичара_који_су_се_пласирали_2
   
   takmicari = [("Pera", 38), ("Milica", 74), ("Laza", 65), ("Jovana", 44)]
   poeni_plasiranih = [poeni for (ime, poeni) in takmicari if poeni >= 50]
   prosek = 0
   print("Prosek:", prosek)
   

Претрага
--------

Претрагом можемо проверити да ли у листи постоји елемент који
задовољава неки услов (на пример, да ли међу бројевима постоји неки
број који је паран или да ли међу речима постоји нека која почиње
самогласником). Веома слични проблеми томе су да се провери да ли сви
елементи листе задовољавају неки услов (на пример, да ли су сви
бројеви позитивни), да ли постоји неки елемент који не задовољава
услов или да ли ниједан од елемената не задовољава услов. Могуће је
одређивати и на којој се позицији налази елемент који задовољава услов
и слично.

Да ли су сви одлични?
'''''''''''''''''''''

На пример, да бисмо проверили да ли су сва три другара одлични ученици
и могу да уђу бесплатно на базен, можемо употребити следећи услов.

.. activecode:: pretraga_svi_odlicni

   prosek_ognjen = 4.75
   prosek_mira = 5.00
   prosek_jelica = 5.00
   if prosek_pera >= 4.50 and prosek_mira >= 4.50 and prosek_jelica >= 4.50:
       print("Svi učenici su odlični")
   else:
       print("Nisu svi učenici odlični")

Слично, проверу да ли је бар један од ученика одличан, могли бисмо
реализовати на следећи начин.

.. activecode:: pretraga_postoji_odlican

   prosek_ognjen = 4.25
   prosek_mira = 4.75
   prosek_jelica = 5.00
   if prosek_pera >= 4.50 or prosek_mira >= 4.50 or prosek_jelica >= 4.50:
       print("Bar jedan od učenika jeste odličan")
   else:
       print("Nijedan učenik nije odličan")

Нагласимо једну важну особину израчунавања логичких услова који су
повезани везником ``and`` тј. *и* или везником ``or`` тј. *или* - они
су "лењи". Услови се проверавају редом, један по један, сдесна
налево. Пошто је у претходном програму Огњенов просек мањи од
``4.50``, још не знамо да ли је бар неко од ученика одличан и потребно
је прећи на проверу наредног ученика. Међутим, када се утврди да је
Мира одличан ученик (пошто је њен просек већи од ``4.50``), тада већ
знамо да је бар један од три ученика одличан и нема потребе вршити
даље провере (потпуно је небитно колики просек оцена има
Јелица). Оператор ``or`` је дакле, лењ, што значи да када се приликом
израчунавања израза облика ``a or b`` утврди да је први део ``a``
тачан, тада се други део ``b`` уопште ни не израчунава (цео израз има
вредност тачно). Слично, ако бисмо приликом провере да ли су сви
ученици одлични утврдили да неки од њих није одличан, знали бисмо да
није тачно да су сви ученици одлични и даље провере не би требало
вршити. Дакле, и опетатор ``and`` је лељ, што значи да када се
приликом израчунавања израза облика ``a and b`` утврди да је први део
``a`` нетачан, тада се други део ``b`` уопште ни не израчунава (цео
израз има вредност нетачно).

Претпоставимо сада да желимо да одредимо да ли су сви ученици чији су
просеци оцена дати у једној листи одлични. Један од начина да се то
уради је да се употреби библиотечка функција ``all`` која добија листу
истинитосних вредности и враћа вредност ``True`` ако су све вредности
у листи ``True`` тј. вредност ``False`` ако то није случај (тј. ако у
листи постоји бар једна вредност ``False``). Поређење редом свих
просека са 4.50 тј. добијање листе логичких вредности које одговарају
томе да ли је сваки од ученика одличан можемо остварити помоћу
компрехенсије.

.. activecode:: сви_одлични_all

   proseci = [4.75, 4.67, 5.00, 4.25, 5.00]
   if all(prosek >= 4.50 for prosek in proseci):
       print("Svi su odlični")
   else:
       print("Nisu svi odlični")

Слично, да бисмо проверили да ли постоји бар један одличан ученик
можемо употребити библиотечку функцију ``any`` којом се проверава да
ли је бар један елемент листе логичких вредности једнак ``True``.

.. activecode:: постоји_одличан_any

   proseci = [4.35, 3.50, 2.87]
   if any(prosek >= 4.50 for prosek in proseci):
       print("Bar jedan od učenika jeste odličan")
   else:
       print("Nijedan učenik nije odličan")
     
Прикажимо сада како да без употребе библиотечких функција проверимо да
ли су сви ученици одлични. Чуваћемо логичку променљиву ``svi_odlicni``
која ће на крају примене алгоритма имати вредност ``True`` тј. тачно,
ако и само ако су сви ученици одлични.  На почетку претпостављамо да
су сви ученици одлични (и у то ћемо веровати све док не пронађемо
ученика који није одличан) и у складу са тим вредност променљиве
``svi_odlicni`` иницијализујемо на ``True``. Након тога проверавамо
један по један просек из листе и ако је мањи од ``4.50``, тада смо
пронашли ученика који није одличан и у складу са тим вредност
променљиве ``svi_odlicni`` мењамо на ``False``.  На крају, у
зависности од вредности променљиве ``svi_odlicni`` исписујемо коначан
резултат.

.. activecode:: сви_одлични_листа

   proseci = [4.75, 4.67, 5.00, 4.25, 5.00]
   
   svi_odlicni = True
   for prosek in proseci:
       if prosek < 4.50:
           svi_odlicni = False
	
   if svi_odlicini:
       print("Svi su odlični")
   else:
       print("Nisu svi odlični")

Приметимо да овај поступак донекле одговара поступку израчунавања
збира, производа, минимума и максимума и слично. Проверу да ли су сва
три ученика одлична извршили смо помоћу израза облика ``prosek1 >= 4.5
and prosek2 >= 4.5 and prosek3 >= 4.5``. Дакле, комбинују се три
истинитосне вредности применом оператора ``and``, веома слично као што
смо обим троугла израчунали комбиновањем три бројевне (нумеричке)
вредности коршћењем оператора ``+``.  Један од начина да се израчуна
обим био је да се његова вредност прво иницијализује на вредност
``0``, а да се затим на то додаје једна по једна дужина
странице. Вредност ``0`` је одабрана као вредност која не утиче на
збир (када додамо било који број на вредност ``0`` добија се баш тај
број). Слични поступак може се применити и на проверу услова да ли су
сви ученици одлични.

.. activecode:: сви_одлични_1

   svi_odlicni = True
   svi_odlicni = svi_odlicni and prosek1 >= 4.50
   svi_odlicni = svi_odlicni and prosek2 >= 4.50
   svi_odlicni = svi_odlicni and prosek3 >= 4.50

Иницијална вредност ``True`` је у овом случају опет таква да не утиче
на резултат тј. таква вредност да када се она оператором ``and`` тј.
логичким и искомбинује са било којим логичким изразом, добија се
вредност тог логичког израза (вредност израза облика ``True and
uslov`` је иста као и вредност израза ``uslov``).

Ефекат доделе ``svi_odlicni = svi_odlicni and prosek >= 4.5`` је такав
да ако је променљива ``svi_odlicni`` имала вредност ``False``, онда је
и десна страна ``False`` и та додела нема никаквог ефекта. Ако
променљива ``svi_odlicni`` има вредност ``True`` и ако је ученик
одличан, онда је вредност десне стране ``True`` и додела ни тада нема
никаквог ефекта. Једини случај у којем додела има ефекат је када
променљива ``svi_odlicni`` има вредност ``True``, а када ученик није
одличан, јер се тада вредност променљиве ``svi_odlicni`` мења на
``False``. Зато се претходни алгоритам може изразити и на следећи
начин.

.. activecode:: сви_одлични_2

   svi_odlicni = True
   if prosek1 < 4.50:
       svi_odlicni = False
   if prosek2 < 4.50:
       svi_odlicni = False
   if prosek3 < 4.50:
       svi_odlicni = False

Програм који је проверавао да ли су сви ученици чији су просеци дати у
листи одлични једноставно је уопштење овога на више елемената уз
увођење петље којом се обрађује један по један елемент.

Постоји још један аспект који може да допринесе ефикаснијем
извршавању. Наиме, већ смо причали да су оператори ``and`` и ``or``
лењи и да израчунавају само онолико колико им је потребно да би
одредили коначан резултат. Када у петљи наиђемо на ученика који није
одличан јасно је да нису сви ученици одлични и да нема потребе
проверавати остале ученике. Дакле, чим се пронађе један ученик чији је
просек оцена мањи од ``4.50`` и када се вредност променљиве
``svi_odlicni`` постави на ``false``, петља може да се прекине. Један
начин да се то уради је да се наведе наредба ``break``.

.. activecode:: сви_одлични_break
		
   proseci = [4.75, 4.67, 5.00, 4.25, 5.00]
   
   svi_odlicni = True
   for prosek in proseci:
       if prosek < 4.50:
           svi_odlicni = False
           break
	
   if svi_odlicini:
       print("Svi su odlični")
   else:
       print("Nisu svi odlični")

Други начин је да се уместо петље ``for`` употреби петља ``while`` у
којој ће се мењати индекси у листи. Основно решење уз употребу петље
``while`` може се формулисати на следећи начин.

.. activecode:: сви_одлични_while
		
   svi_odlicni = True
   i = 0
   while i < len(proseci):
       if proseci[i] < 4.50:
           svi_odlicni = False
       i = i + 1

Рани прекид (који одговара лењом израчунавању) можемо остварити тако
што се услов петље ојача тиме да су сви до тада виђени ученици одлични
чиме се обезбеђује да се петља заврши чим променљива ``svi_odlicni``
добије вредност ``false`` (или када индекс ``i`` достигне дужину
листе).

.. activecode:: сви_одлични_while_1
		
   svi_odlicni = True
   i = 0
   while i < len(proseci) and svi_odlicni:
       if proseci[i] < 4.50:
           svi_odlicni = False
       i = i + 1

Као што смо већ видели, провера да ли постоји бар један елемент који
задовољава неки услов се формулише веома слично, једино што се уместо
оператора ``and`` који представља логичко *и* користи оператор ``or``
који представља логичко *или*. Најједноставнији и најјдиректнији начин
био је да се неколико услова повежу оператором ``or``. Међутим, да
бисмо обрадили већи број елемената, можемо употребити и логичку
променљиву ``postoji_odlican`` и ажурирати је. Размисли о томе шта
треба да буде њена иницијална вредност.

.. activecode:: постоји_одличан_1

   proseci = [3.75, 4.25, 4.55]
   
   postoji_odlican = # postavi ovde inicijalnu vrednost
   postoji_odlican = postoji_odlican or proseci[0] >= 4.50
   postoji_odlican = # dopuni ovaj red po uzoru na red iznad i red ispod
   postoji_odlican = postoji_odlican or proseci[2] >= 4.50

   if postoji_odlican:
       print("Bar jedan učenik je odličan")
   else:
       print("Nijedan učenik nije odličan")

Слично као што је додела ``svi_odlicni = svi_odlicni and prosek >=
4.50`` имала ефекта само ако променљива ``svi_odlicni`` имала вредност
``False`` и ако је просек мањи ``4.50``, тако и додела
``postoji_odlican = postoji_odlican or prosek >= 4.50`` има ефекта
само ако променљива ``postoji_odlican`` има вредност ``False`` и ако
је ученик одличан тј. ако је просек већи или једнак ``4.50``. Измени
претходни програм у складу са тим.

.. activecode:: постоји_одличан_2

   proseci = [3.75, 4.25, 4.55]
   
   postoji_odlican = False
   if    # dopuni ovaj red
       postoji_odlican = True
   if    # dopuni ovaj red
       postoji_odlican = True
   if    # dopuni ovaj red
       postoji_odlican = True

   if postoji_odlican:
       print("Bar jedan učenik je odličan")
   else:
       print("Nijedan učenik nije odličan")

На крају, претходни програм можемо организовати и помоћу петље и тако
га уопштити на већи број ученика.
   
.. activecode:: постоји_одличан_листа

   proseci = [3.50, 4.00, 3.75, 4.25]
   
   postoji_odlican =    # dopuni ovaj red - postavi inicijalnu vrednost
   for    # dopuni ovaj red - popravi petlju for
       if prosek >= 4.50:
           postoji_odlican =    # dopuni ovaj red - azuriraj vrednost promenljive
	 
   if postoji_odlican:
       print("Postoji odličan")
   else:
       print("Ne postoji odličan")

Допуни претходни програм наребом ``break`` тако да се израчунавање
прекине чим је могуће.

Да ли на свим пољима постоји лоптица?
'''''''''''''''''''''''''''''''''''''

На крају, проверимо колико смо разумели претрагу тако што ћемо помоћи
Карелу да провери да ли се на свим пољима испред њега налазе лоптице.
Проверу да ли постоји лоптица на пољу на ком се робот налази можеш
извршити позивом ``ima_loptica_na_polju()``.

.. karel:: карел_проверава_1

   
   {
      setup: function() {
           function random(n) {
              return Math.floor(n * Math.random());
	   }
      
	   var world = new World(6, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
	   for (var k = 2; k <= 6; k++)
                  if (random(5) > 0)
                     world.putBall(k, 1);
           var robot = new Robot();
	   robot.setInfiniteBalls(true);
	   
	   var code = ["from karel import *",
	                   "# dopuni naredni red",
	                   "sva_polja_sadrze_loptice = ",
			   "while moze_napred():",
			   "    napred()",
			   "    # dopuni kod na ovom mestu",
			   "if sva_polja_sadrze_loptice:",
			   "    izgovori('Sva polja sadrze loptice')",
			   "else:",
			   "    izgovori('Ne sadrze sva polja loptice')"];
	   return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
           var sve = true;
	   for (var k = 2; k <= 6; k++)
               if (world.getBalls(k, 1) == 0)
                  sve = false;
	   if (sve)
               return robot.lastMessage == "Sva polja sadrze loptice";
	   else
	       return robot.lastMessage == "Ne sadrze sva polja loptice";
      }
   }

Покрени претходни програм неколико пута, да би се уверио да ради и у
ситуацијама када су сва поља попуњена лоптицама и када нису.

Помози му сада да провери да ли постоји бар једно поље са лоптицом
испред њега.
   
.. karel:: карел_проверава_2

   
   {
      setup: function() {
           function random(n) {
              return Math.floor(n * Math.random());
	   }
      
	   var world = new World(6, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
	   for (var k = 2; k <= 6; k++)
                  if (random(5) == 0)
                     world.putBall(k, 1);
           var robot = new Robot();
	   robot.setInfiniteBalls(true);
	   
	   var code = ["from karel import *",
	                   "# dopuni naredni red",
	                   "postoji_loptica = ",
			   "while moze_napred():",
			   "    napred()",
			   "    # dopuni kod na ovom mestu",
			   "if postoji_loptica:",
			   "    izgovori('Postoji polje sa lopticom')",
			   "else:",
			   "    izgovori('Ne postoji polje sa lopticom')"];
	   return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
           var postoji = false;
	   for (var k = 2; k <= 6; k++)
               if (world.getBalls(k, 1) > 0)
                  postoji = true;
	   if (postoji)
               return robot.lastMessage == "Postoji polje sa lopticom";
	   else
	       return robot.lastMessage == "Ne postoji polje sa lopticom";
      }
   }


