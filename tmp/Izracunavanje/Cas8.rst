Час 8 - Цели и реални бројеви, дељење
#####################################


Цели и реални бројеви
---------------------

До сада смо у задацима користили само природне бројеве. Језик Python
подржава и рад са целим бројевима (који укључују и негативне
вредности) и они се записују на исти начин као у математици. На
пример, вредност израза ``3 - 8`` је ``-5`` док је вредност израза
``(-3) - (-8)`` број ``5``. На енглеском се цели бројеви називају
*integers*, па се за променљиве и изразе чија је вредност целобројна
каже да су типа **int**.

Реалне бројеве је такође веома једноставно користити, једино што се,
уместо децималног зареза на који смо навикли у математици, мора
користити децимална тачка. Тако се, на пример, број *2,5* записује као
``2.5``. За реалне бројеве у рачунару се каже да су записани у облику
*покретног зареза* (енгл. *floating point*), па се за променљиве и
изразе чија је вредност реална кажу да су вредност типа **float**.

Решимо сада и неколико задатака који укључују и рад са бројевима који
нису природни.


Бајкалско језеро
''''''''''''''''
.. level:: 1

.. questionnote::

   Бајкалско језеро у Русији је најдубље језеро на свету. Оно је
   криптодепресија јер се његово дно (најнижа тачка) налази на 1,181
   километара испод нивоа мора, а површина му се налази на 456 метара
   надморске висине. Израчунај његову највећу дубину у метрима.


.. activecode:: бајкалско_језеро

  nivo_povrsine = 456
  nivo_dna = -1.181 * 1000
  dubina = nivo_povrsine - nivo_dna
  print(dubina)  

.. infonote::

   Криптодепресија је удубљење испуњено водом, чија је површина изнад
   нивоа мора, а дно испод нивоа мора. Потиче од грчке речи крипто,
   што значи скривен или тајан, и речи депресија, што у географији
   представља израз за предео нижи од нивоа површине
   мора. Криптодепресије су углавном језера. Највећа криптодепресија
   на свету је управо Бајкалско језеро, а у Европи је то језеро
   Ладога. На Балканском полуострву највећа криптодепресија је
   Скадарско језеро на граници Црне Горе и Албаније. Криптодепресије
   обично настају када се раседи и расцепи у земљиној кори испуне
   водом.

Куповина намирница
''''''''''''''''''
.. level:: 1

.. questionnote::

   Марко је купио 0,45 kg саламе, 0,25 kg сира и два паковања од по
   0,3 kg шунке. Колико је тешка кеса коју носи кући?

.. activecode:: маса_производа

  salama = 0.45
  sir = 0.25
  sunka = 0.3
  print(salama + sir + 2 * sunka)

Банковни рачун
''''''''''''''
.. level:: 1

.. questionnote::

   Ђура је уплатио летовање пре него што је добио плату и ушао је у тзв.
   дозвољени минус тј. након те уплате дуговао је банци 12.376,5 динара.
   Три дана касније на рачун му је уплаћена плата од 43.386,9 динара.
   Колико му је тада било стање на рачуну.


Допуни наредни програм тако да коректно решава тражени задатак   

.. activecode:: банковни_рачун

  stanje_pre = 
  uplata = 
  stanje_posle = 
  print(stanje_posle)

Након покретања, програм треба да испише вредност ``31010.4``.

.. reveal:: пресек_решење1
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   .. activecode:: банковни_рачун_решење

      stanje_pre = -12376.5
      uplata = 43386.9
      stanje_posle = stanje_pre + uplata
      print(stanje_posle)

Исправи сада програм тако да се почетно стање и износ уплате учитава
на почетку рада програма. Подсетимо се, учитавање реалног броја може
се извршити помоћу ``float(input("..."))``.


.. reveal:: пресек_решење2
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   .. activecode:: банковни_рачун_решење_1

      stanje_pre = float(input("Unesi početno stanje:"))
      uplata = ???
      stanje_posle = stanje_pre + uplata
      print(stanje_posle)

      
Реално дељење
-------------

У наставку ћемо се посветити операцији дељења. У већини програмских
језика разликују се два облика дељења: **реално** и
**целобројно**. Резултат (количник) реалног дељења је реалан број (на
пример, када се 13 реално дели са 4, добија се количник 3,25), док је
код целобројног дељења количник увек цео број, при чему је могуће да
постоји и целобројни остатак (на пример, када се 13 целобројно дели са
4, добија се количник 3 и остатак 1).

Реалним дељењем се могу делити и реални и цели бројеви, а резултат је
реалан број. На пример, ако се користи реално дељење тада је *7,5 :
2,5* једнако *3* док је *5 : 2* једнако *2,5*. Реално дељење се у
језику Python3 обележава знаком ``/``. Тако је вредност израза ``7.5 /
2.5`` једнака ``3.0``.

Провери своје знање наредним питањем.

.. fillintheblank:: fill_проценат

      Вредност израза ``4.5 / 5`` је |blank|
      
      - :0.9: Tачно
        :0,9: Тачно, али уместо децималног зареза треба ставити децималну тачку
        :.*: Нетачно

Посматрајмо наредни једноставан задатак у којем ћемо употребити реално
дељење.

Просек скокова у даљ
''''''''''''''''''''
.. level:: 1
	   
.. questionnote::

  Скакач у даљ је у квалификацијама у првој серији скочио 8,12, у
  другој 8,23, а у трећој 8,17 метара. Колико је износио његов
  просечни скок?

  
Просек (каже се и аритметичка средина) неколико бројева једнак је
количнику њиховог збира и њиховог броја. Са просеком сте се сигурно
већ срели када сте рачунали просек својих оцена. Дакле, да бисмо решили
овај задатак потребно је сабрати дужине сва три скока и поделити са
три.

.. activecode:: Просек_скокова

  skok1 = 8.12
  skok2 = 8.23
  skok3 = 8.17
  prosek = (skok1 + skok2 + skok3) / 3
  print(prosek)

Сложени израз из збирке из математике
'''''''''''''''''''''''''''''''''''''
.. level:: 1

.. questionnote::

   У једној збирици из математике за шести разред јавља се задатак у
   коме се тражи да се израчуна вредност израза 1 + (3 - (-4)) : 2 +
   0,7. Израчунај ту вредност у Python-у.

   
.. activecode:: Сложени_израз_са_дељењем

  print(1 + (3 - (-4)) / 2 + 0.7)


.. questionnote::

   Израчунај вредност израза :math:`7 + \frac{4 - (-5)}{(-3) \cdot 2 -
   7}` у Python-у.

.. activecode:: Сложени_израз_са_дељењем_1

  print()  # popravi ovaj red

Ако урадиш све како треба, добићеш резултат ``6.3076923076923075``.
   

Полице са књигама
'''''''''''''''''
.. level:: 1

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
  
Поскупљења и појефтињења
''''''''''''''''''''''''
.. level:: 2

.. questionnote::

   Цена хлеба је била 35 динара, затим је поскупела 10%. Млеко је
   коштало 100 динара, али је сада на снижењу и продаје се по 20%
   нижој цени. Колико коштају три хлеба и два млека?

   
*Проценат* (каже се и *посто*) се у математици обележава знаком %
и означава стоти део нечега. На пример, када напишемо 10% броја 200,
мислимо заправо на десет стотих делова броја 200, што знамо да је
заправо :math:`\frac{10}{100} \cdot 200` тј. 20. Дакле, запамтимо,
запис *p%* је просто скраћеница за запис
:math:`\frac{p}{100}`. Провери да ли ово разумеш.


.. fillintheblank:: fill_проценат_2
		    
    20% броја 80 је број |blank|

    - :16: Тачно
      :x: 20% од 80 је 20 стотина од 80

Ако је цена *c*, тада је *p* процената те цене једнако *p* стотих
делова те цене тј. :math:`\frac{p}{100} \cdot c`. Када се каже да је
производ поскупео *p* процената, то значи да му је цена порасла за *p*
процената, тј. да је она увећана за *p* својих стотих делова. Ако је
цена пре поскупљења била *c*, тада је након поскупљења она једнака
:math:`c + \frac{p}{100} \cdot c` тј. :math:`c \cdot (1 +
\frac{p}{100})`. Слично, ако је производ појефтинио *p* процената, то
значи да му је цена снижена за *p* процената, тј. да је почетна цена
умањена за *p* својих стотина и једнака је :math:`c - \frac{p}{100}
\cdot c` тј. :math:`c \cdot (1 - \frac{p}{100})`. На основу овога,
задатак се лако може решити.

.. activecode:: поскупљење_и_појефтињење

   hleb_pre = 35
   hleb_posle = hleb_pre + (10 / 100) * hleb_pre
   mleko_pre = 100
   mleko_posle = mleko_pre - (20 / 100) * mleko_pre
   racun = 3 * hleb_posle + 2 * mleko_posle
   print(racun)

Приметимо и да ако је неки производ поскупео 10%, тада је његова нова
цена једнака старој цени помноженој бројем :math:`1 + \frac{10}{100} =
1,1`, а да ако је појефтинио 20%, тада је његова нова цена једнака
старој цени помноженој бројем :math:`1 - \frac{20}{100} = 0,8`.

Група радника
'''''''''''''
.. level:: 2

.. questionnote::

   :math:`n` радника уради посао за :math:`s` сати. Написати програм
   којим се одређује за колико сати ће посао бити завршен ако се
   прикључи још :math:`m` радника?

Један начин да се задатак реши је да се прво израчуна колико је
радник-сати потребно да се заврши цео посао. Пошто сваки од :math:`n`
радника ради :math:`s` сати, за завршетак посла потребно је :math:`n
\cdot s` радник-сати (један радник би сам посао радио :math:`n\cdot s`
сати). Ако посао треба да заврши :math:`n+m` радника, тада ће се посао
завршити :math:`n+m` пута брже него када радни један радник, тј. посао
ће бити завршен за :math:`\frac{n\cdot s}{n+m}` сати.

Други начин да се задатак реши је да се примени пропорција. Уколико
ради више радника потребно је мање дана, па је потребно применити
обрнуту пропорцију. Ако са :math:`x` обележимо број сати за које посао
уради већа група радника, тада важи да је :math:`n : (n+m) = x : s`
(са обе стране једнакости вредности су поређане од мање ка
већој). Одатле опет закључујемо да је :math:`x = \frac{n\cdot s}{n
+ m}`.

.. activecode:: група_радника

   # unosimo podatke
   n = int(input("Koliko radnika radi:"))
   s = float(input("Za koliko sati bi završili posao da rade sami:"))
   m = int(input("Koliko će im se radnika pridružiti:"))
   # izračunavamo rezultat
   s1 = ???   # ispravi ovaj red
   # prikazujemo rezultat
   print(s1)

Провери свој програм тако што провериш да ли за улазе ``2``, ``4``,
``2`` исписује ``2.0``, док за улазе ``3``, ``5``, ``3`` исписује
``2.5``.

  
Целобројно дељење
-----------------
  
Целобројно дељење обично подразумева дељење целих бројева и као
резултат се одређују целобројни количник и остатак при дељењу. На
пример, ако се целобројно деле бројеви *14* и *3* тада се добија
целобројни количник *4* и остатак *2*.

.. level:: 2
   :container:
      
   У општем случају, целобројни количник и остатак при дељењу бројева
   :math:`a` и :math:`b` су бројеви :math:`q` и :math:`r` такви да је
   :math:`a = q \cdot b + r` и :math:`0 \leq r < b`. Приметимо да ова
   веза важи у примеру дељења :math:`14` и :math:`3` важи управо ова
   веза тј. важи да је :math:`14 = 4 \cdot 3 + 2`, при чему је
   :math:`0 \leq 2 < 3`. Други услов каже да остатак мора бити мањи од
   делиоца тј. да количник мора бити што је могуће већи. Тај услов је
   веома важан (на пример, важи да је :math:`14 = 3 \cdot 3 + 5`,
   међутим, нећемо рећи да је целобројни количник :math:`3` а остатак
   :math:`5` јер број :math:`5` није мањи од делиоца).

Кроз наредно питање провери колико разумеш операције целобројног
дељења и остатка при дељењу.

.. fillintheblank:: fill1412
		    
    При дељењу бројева 13 и 5 целобројни количник је |blank| а остатак је |blank|

    - :2: Тачно
      :x: Важи да је 13 = 2 · 5 + 3
    - :3: Тачно
      :x: Важи да је 13 = 2 · 5 + 3

У језику Python3 операција **целобројног дељења** се означава са
``//``, а операција израчунавања **остатка при дељењу** се означава са
``%``.

.. infonote::

   У математици се знак % користи да означи проценат (стоти део
   нечега). Коришћење истог знака за остатак при дељењу је заправо
   несрећна околност и треба бити обазрив да се та два заправо
   неповезана појма случајно не помешају.


Дакле, оператором ``/`` се израчунава реални, оператором ``//``
целобројни количник, а оператором ``%`` остатак при дељењу. Провери колико
ово разумеш.

.. dragndrop:: дељење
    :feedback: Покушај поново
    :match_1: 27 / 10|||2.7
    :match_2: 27 // 10|||2
    :match_3: 27 % 10|||7

    Превлачењем упари изразе са њиховим вредностима.

.. dragndrop:: дељење1
    :feedback: Покушај поново
    :match_1: 43 / 8|||5.375
    :match_2: 43 // 8|||5
    :match_3: 43 % 8|||3
    
    Упари изразе са њиховим вредностима.

Покажимо једноставну примену израчунавања целобројног количника и остатка
на следећем задатку.

Подела чоколадних бананица
''''''''''''''''''''''''''
.. level:: 1

.. questionnote::

   У школи се организује новогодишња приредба за децу. Од пара које су
   зарадили тако што су организовали сајам својих рукотворина купили
   су неколико крем бананица које желе да равномерно поделе свој деци
   (тако да свако дете добије исти број бананица). Ако се зна колико
   ће деце доћи на приредбу, колико ће свако дете добити бананица, a
   колико ће бананица остати нерасподељено?


.. activecode:: чоколадне_бананице

   broj_dece = int(input("Koliko će dece doći na priredbu: "))
   ukupno_bananica = int(input("Koliko ukupno ima bananica: "))
   bananica_po_detetu = ukupno_bananica // broj_dece
   ostalo_bananica = ukupno_bananica % broj_dece
   print("Svako će dete dobiti", bananica_po_detetu, "bananica.")
   print("Ostaće", ostalo_bananica, "bananica.")

Приметимо и да смо број преосталих бананица могли израчунати и тако
што од укупног броја бананица одузмемо број бананица које су подељене
деци (а то је производ броја деце и броја бананица које је свако дете
добило) тј. помоћу израза ``ukupno_bananica - broj_dece *
bananica_po_detetu``. Ипак, коришћење оператора ``%`` којим се
израчунава остатак је једноставније решење.

Ево једног сличног задатка, за вежбу.

Разломак у мешовити број
''''''''''''''''''''''''
.. level:: 1

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


Целобројно дељење - конверзија јединица
---------------------------------------


Целобројни количник и остатак често користимо када желимо да
прерачунавамо јединице. Размотримо следећих неколико задатака.

Конверзија центиметара у метре и центиметре
'''''''''''''''''''''''''''''''''''''''''''
.. level:: 1

.. questionnote::

   Напиши програм који на основу дате дужине у центиметрима израчунава
   исту дужину у метрима и центиметрима. На пример, ако је дужина 178
   центиметара, програм израчунава да је то 1 метар и 78 центиметара.

Пошто у једном метру има 100 центиметара, задатак се своди на
израчунавање целобројног количника и остатка при дељењу
са 100. Заиста, ако имамо :math:`m` метара и :math:`c` центиметара,
тада је укупан број центиметара једнак :math:`m\cdot 100 + c`, при
чему је :math:`0 \leq c < 100`.

.. activecode:: центиметри_у_метре_и_центиметре

  ukupno_centimetara = int(input("Unesi dužinu u centimetrima: "))
  metara = ukupno_centimetara // 100
  centimetara = ukupno_centimetara % 100
  print("Dužina je", metara, "m", centimetara, "cm")

Рецимо поново да је често решење до којег ученици самостално долазе и
оно у којем се преостали број центиметара рачуна као ``centimetara =
ukupno_centimetara - metara * 100``. Иако је ово решење исправно, на
располагању нам је оператор израчунавања остатака ``%`` и требало би
да се навикнемо да га користимо.

Конверзија милиметара у метре, дециметре, центиметре и милиметре
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. level:: 2

.. questionnote::

   Напиши програм који на основу дате дужине у милиметрима израчунава
   исту дужину у метрима, дециметрима, центиметрима и милиметрима. На
   пример, ако је дужина 1789 милиметара, програм израчунава да је то
   1 метар и 7 дециметара и 8 центиметара и 9 милиметара.

Један од начина је да прво, слично решењу претходног задатка одредимо
број метара и преосталих милиметара. Пошто у једном метру има 1000
милиметара, то можемо урадити израчунавањем целобројног количника и
остатка при дељењу са 1000. Тиме добијамо број метара и имамо даље
задатак да преостали број милиметара разложимо на дециметре,
центиметре и милиметре. Њега прво можемо разложити на дециметре и
преостале милиметре израчунавањем целобројног количника и остатка при
дељењу са 100 (јер у једном дециметру има 100 милиметара). На крају,
преостале милиметре можемо разложити на центиметре и милиметре
израчунавањем целобројног количника и остатка при дељењу са 10 (јер у
једном центиметру има 10 милиметара).
   
.. activecode:: центиметри_у_метре_дециметре_центиметре_и_милиметре

  duzina = int(input("Unesi dužinu u milimetrima: "))
  m = duzina // 1000
  ostalo_mm_1 = duzina % 1000
  dm = ostalo_mm_1 // 100
  ostalo_mm_2 = ostalo_mm_1 % 100
  cm = ostalo_mm_2 // 10
  mm = ostalo_mm_2 // 10
  print("Dužina je", m, "m", dm, "dm", cm, "cm", mm, "mm")

Ипак, задатак можемо решити и на мало систематичнији начин. Ако са
:math:`mm`, :math:`c`, :math:`d` и :math:`m` означимо редом број
милиметара, центиметара, дециметара и метара, тада је укупан број
милиметара једнак :math:`m \cdot 1000 + d \cdot 100 + c\cdot 10 +
mm`. Пошто су прва три сабирка дељива са 10, важи да се :math:`mm`
moже израчунати као остатак при дељењу укупног броја милиметара са 10.
Целобројни количник укупног броја милиметара са 10 је :math:`m \cdot
100 + d\cdot 10 + c`, па се зато број центиметара може израчунати тако
што се пронађе целобројни количник укупног броја милиметара са 10, а
затим остатак при дељењу тог броја са 10. Слично, целобројни количник
укупног броја милиметара са 100 једнак је :math:`m \cdot 10 + d`, па
се број дециметара може израчунати као остатак при дељењу тог количника
са 10. На крају, број метара једнак је целобројном количнику укупног броја
дециметара са 1000.

.. activecode:: центиметри_у_метре_дециметре_и_центиметре_1
		
  duzina = int(input("Unesi dužinu u milimetrima: "))
  mm = duzina % 10
  cm = (duzina // 10) % 10
  dm = (duzina // 100) % 10
  m  = duzina // 1000
  print("Dužina je", m, "m", dm, "dm", cm, "cm", mm, "mm")

Целобројно дељење - позициони запис броја
-----------------------------------------

Ако је укупан број центиметара био 123, тада је број метара 1, број
дециметара 2 и број центиметара 3. Решавањем претходног задатка смо
заправо одређивали појединачне цифре коришћене у запису тог
троцифреног броја. Приказана техника може бити уопштена тако да се
одређују све цифре и у запису дужих бројева.


Цифре броја
'''''''''''
.. level:: 2

.. questionnote::

   Чест начин откривања грешака при слању података је да се уз податке
   које треба послати, пошаљу и одређени контролни подаци, израчунати
   на основу самих података. Када прималац прими податке, он на основу
   примљених података поново израчунава контролне податке и упоређује
   их са контролним подацима које је примио. Ако се приликом преноса
   података, услед неких сметњи, подаци случајно измене, прималац ће
   то приметити тако што ће видети да се контролни подаци које је он
   израчунао неће поклопити са онима које је примио. Сви подаци се у
   рачунарима представљају помоћу бројева, а још од најранијег доба
   рачунарства као метода контроле коришћен је збир цифара. На пример,
   ако би податак који се шаље био број 12345, онда би се уз њега слао
   и контролни број 15 (збир 1 + 2 + 3 + 4 + 5). Ако би приликом слања
   нека цифра била случајно промењена (на пример, ако би прималац
   грешком примио број 12335) тада би се и контролни број
   највероватније разликовао (контролни број би у нашем примеру био
   14). Напиши програм који за дати петоцифрени број одређује његов
   контролни број (збир његових цифара).

.. activecode:: цифре_броја
   :runortest: broj, kontrolni_broj
   :enablecopy:
		
   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   broj = 12345
   # -*- acsection: main -*-
   c0 = (broj // 1) % 10
   c1 = (broj // 10) % 10
   c2 = 0 # ispravi ovaj red
   c3 = (broj // 1000) % 10
   c4 = 0 # ispravi ovaj red
   kontrolni_broj = c0 + c1 + c2 + c3 + c4
   # -*- acsection: after-main -*-
   print(kontrolni_broj)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for broj, kontrolni_broj in [(71425, 19), (33214, 13), (62040, 12)]:
             self.assertEqual(acMainSection(broj = broj)["kontrolni_broj"],kontrolni_broj,"За број %s контролни број је %s." % (broj, kontrolni_broj))
   myTests().main()
   

Приметимо да смо цифре броја одређивали веома слично као у претходном
задатку.  Цифре одређујемо сдесна налево, тако што делимо број са
тежином цифре (за цифру јединица број делимо са 1, десетица са 10,
стотина са 100 итд.) и проналазимо остатак при дељењу са 10.

.. infonote::

   Људи су контролу података примењивали и ручно, а сада рачунари
   обављају такве контроле у овиру прецизно задатих поступака –
   *протокола за размену података*. Иако је контролни збир
   најједноставнији начин контроле, он не може да открије грешке до
   којих може доћи услед случајне размене редоследа цифара (на пример,
   ако се уместо броја 12345 грешком пошаље број 12435, контролни збир
   оба броја ће бити исти и грешка неће бити примећена). Зато се
   уместо збира понекад користе изрази облика :math:`c_0 + 2c_1 +
   3c_2 + 4c_3 + 5c_4`. Покушај да измениш претходни програм тако да
   израчунава контролни број на овај начин.


Целобројно дељење - време и углови
----------------------------------

За разлику од бројева и јединица мере које записујемо у систему чија
је основа 10, при раду са временом и угловима користимо систем чија је
основа број 60. Тако један сат има 60 минута, а један минут 60
секунди. Слично један степен има 60 угаоних минута, а један угаони
минут има 60 угаоних секунди. Прикажимо сада кроз неколико задатака
како можемо у програмима вршити израчунавања у којима учествују време
и углови.

Конверзија сати и минута у минуте и обратно
'''''''''''''''''''''''''''''''''''''''''''
.. level:: 1

.. questionnote::

   Ако се зна колико је тренутно сати и минута, израчунај колико је
   минута протекло од претходне поноћи.

Пошто у једном сату има 60 минута, довољно је да помоножиш број сати
са 60 и на то да додаш број минута.

.. activecode:: сати_и_минути_у_минуте
   :runortest: sati, minuta, minuta_od_ponoci
   :enablecopy:

   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   sati = 2
   minuta = 60
   # -*- acsection: main -*-
   minuta_od_ponoci = 0 # ispravi ovaj red
   # -*- acsection: after-main -*-
   print(minuta_od_ponoci)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for sati, minuta, minuta_od_ponoci in [(14, 19, 859), (11, 13, 673), (23, 59, 1439)]:
             self.assertEqual(acMainSection(sati = sati, minuta = minuta)["minuta_od_ponoci"],minuta_od_ponoci,"У %s:%s протекло је %s минута од поноћи." % (sati, minuta, minuta_od_ponoci))
   myTests().main()
   
   
.. questionnote::

   Ако се зна колико је минута протекло од претходне поноћи, израчунај
   колико је тренутно сати и минута.

Ако са :math:`s` обележимо тренутни број сати, са :math:`m` тренутни
број минута, а са :math:`M` број минута протеклих од поноћи, тада важи
да је :math:`M = s \cdot 60 + m`, при чему за :math:`m` важи да је
број између :math:`0` и :math:`59`, што јасно указује на то да се
тражене вредности могу израчунати применом целобројног дељења.
   
.. activecode:: минути_у_сате_и_минуте
   :runortest: minuta_od_ponoci, sati, minuta
   :enablecopy:

   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   minuta_od_ponoci = 125
   # -*- acsection: main -*-
   sati = 0     # ispravi ovaj red
   minuta = 0   # ispravi ovaj red
   # -*- acsection: after-main -*-
   print(sati, minuta)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for sati, minuta, minuta_od_ponoci in [(14, 19, 859), (11, 13, 673), (23, 59, 1439)]:
             self.assertEqual(acMainSection(minuta_od_ponoci = minuta_od_ponoci)["sati"],sati,"У %s:%s протекло је %s минута од поноћи." % (sati, minuta, minuta_od_ponoci))
             self.assertEqual(acMainSection(minuta_od_ponoci = minuta_od_ponoci)["minuta"],minuta,"У %s:%s протекло је %s минута од поноћи." % (sati, minuta, minuta_od_ponoci))
   myTests().main()

Аутобус
'''''''
.. level:: 2

.. questionnote:: 

  Aутобус је кренуо са станице у 6 часова и 17 минута и путовао је 2
  сата и 55 минута. У колико сати и минута је стигао?

.. activecode::  време_путовања

   # sat i munut kada je autobus krenuo
   krenuo_sat = 6
   krenuo_min = 17
   # broj sati i minuta koliko je autobus putovao
   putovao_sat = 2
   putovao_min = 55
   # sabiramo minute i prenosimo sate ako je potrebno (ako su minuti bar 60)
   stigao_min = (krenuo_min + putovao_min) % 60;
   prenos = (krenuo_min + putovao_min) // 60;
   # sabiramo sate dodajuci prenos minuta
   stigao_sat = krenuo_sat + putovao_sat + prenos;
   print(stigao_sat, stigao_min)

Други начин да се реши задатак је да се прво све прерачуна у минуте,
да се сабирање изврши у минутима, а да се затим добијени минути
претворе назад у сате и минуте. Приликом превођења неког временског
тренутка у минуте израчунавамо заправо број минута протеклих од
претходне поноћи (или поднева, ако се сати рачунају само до 12). Тај
број минута се може добити тако што се број сати помножи бројем 60
(јер у једном сату има 60 минута) и на то дода број минута.
   
.. activecode:: време_путовања_1

   # sat i minut kada je autobus krenuo		
   krenuo_sat = 6
   krenuo_min = 17
   # broj sati i minuta koliko je autobus putovao
   putovao_sat = 2
   putovao_min = 55
   # trenutak polaska u minutima
   krenuo_u_minutima = krenuo_sat * 60 + krenuo_min
   # trajanje putovanja u minutima
   putovao_u_minutima = putovao_sat * 60 + putovao_min
   # trenutak dolaska u minutima
   stigao_u_minutima = krenuo_u_minutima + putovao_u_minutima
   # sat i minut dolaska
   stigao_sat = stigao_u_minutima // 60
   stigao_min = stigao_u_minutima % 60
   print(stigao_sat, stigao_min)

Криви торањ у Пизи
''''''''''''''''''
.. level:: 2

.. questionnote::

   Криви торањ у Пизи је нагнут и са земљом заклапа угао од 86 степени
   и 3 минута. Колико степени и минута је торањ нагнут, то јест,
   колико одступа од усправног положаја.


Прав угао има 90 степени тј. 90·60 минута. Ако угао од 86 степени и 3
минута преведемо у минуте и одузмемо га од правог угла добићемо
тражени угао у минутима. На крају ћемо израчунати целобројни количник
и остатак и тако добити тражени угао у степенима и минутама. Рецимо
још да смо у овом задатку заправо одређивали комплемент датог угла,
што је операција о којој је сигурно било речи на часовима математике.
Пошто се торањ с временом криви, твој програм треба исправно да ради и
ако је угао мало другачји.
   
.. activecode:: криви_торањ
   :runortest: alfa_stepeni, alfa_minuti, beta_stepeni, beta_minuti
   :enablecopy:

   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   # ugao pod kojim je nagnut toranj u stepenima i minutima
   alfa_stepeni = 86
   alfa_minuti = 3
   # -*- acsection: main -*-
   # prevodimo taj ugao u minute
   alfa_u_minutima = 0      # ispravi ovaj red
   # prav ugao u minutima
   prav_u_minutima = 90 * 60
   # komplement ugla u minutima
   beta_u_minutima = prav_u_minutima - alfa_u_minutima
   # komplement ugla u stepenima i minutima
   beta_stepeni = 0         # ispravi ovaj red
   beta_minuti = 0          # ispravi ovaj red
   # -*- acsection: after-main -*-
   print(beta_stepeni, "stepenа i", beta_minuti, "minuta")
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for (alfa_stepeni, alfa_minuti, beta_stepeni, beta_minuti) in [(86, 37, 3, 23), (85, 19, 4, 41)]:
             self.assertEqual(acMainSection(alfa_stepeni = alfa_stepeni, alfa_minuti = alfa_minuti)["beta_stepeni"],beta_stepeni,"Комплемент угла %s:%s је %s:%s." % (alfa_stepeni, alfa_minuti, beta_stepeni, beta_minuti))
             self.assertEqual(acMainSection(alfa_stepeni = alfa_stepeni, alfa_minuti = alfa_minuti)["beta_minuti"],beta_minuti,"Комплемент угла %s:%s је %s:%s." % (alfa_stepeni, alfa_minuti, beta_stepeni, beta_minuti))
   myTests().main()
     

Домаћи задатак
--------------

Ако на часу нисте стигли да урадите све задатке, уради их сада, у
склопу домаћег задатка. Након тога покушај да урадиш и наредних
неколико задатака.


Прочитане стране књиге
''''''''''''''''''''''
.. level:: 1

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

      

Повећање и смањење плата
''''''''''''''''''''''''
.. level:: 2

Ево опет једног сличног задатка за вежбу.

.. questionnote::

   Плате су прво смањене за десет процената, а онда су после неколико
   месеци те смањене плате повећане за 10 процената. Ако је у почетку
   плата била 50,000 динара, колика је она после смањења и повећања?

.. activecode:: плате
   :runortest: plata, povecana_plata
   :enablecopy:
      
   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   plata = 50000
   # -*- acsection: main -*-
   smanjena_plata = 0  # popravi ovaj red
   povecana_plata = 0  # popravi ovaj red
   # -*- acsection: after-main -*-
   print(povecana_plata)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for plata, povecana_plata in [(45123, 44671.77), (54321, 53777.79)]:
             self.assertEqual(acMainSection(plata = plata)["povecana_plata"],povecana_plata,"Ако је плата била %s динара, после повећања она износи %s динара." % (plata,povecana_plata))
   myTests().main()

   
Ако добијеш решење 49,500 значи да је све како треба, иако је тај
резултат мало неочекиван. Често се помисли да ће смањење и повећање за
по 10% да се пониште и да ће се плата вратити на полазну
вредност. Међутим, смањење је било 10% полазне величине од 50,000
динара тј. за 5,000 динара, док је повећање за 10% од смањене величине
од 45,000 динара тј. повећање је за 450 динара.
   
.. reveal:: пресек_решење21
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   .. activecode:: плате_решење

      plata = 50000
      smanjena_plata = plata - (10 / 100) * plata
      povecana_plata = smanjena_plata + (10 / 100) * smanjena_plata
      print(povecana_plata)

Преостало време видео-снимка
''''''''''''''''''''''''''''
.. level:: 2

.. questionnote::

   Апликација за пуштање видео-снимака нуди опцију приказа преосталог
   времена до краја снимка. Ако је познато трајање снимка у сатима,
   минутима и секундама и време протекло од почетка снимка, такође
   задато у сатима, минутима и секундама напиши програм који израчунава
   време до краја у сатима, минутима и секундама.

Најлакши начин да решиш задатак је да оба позната времена претвориш у
секунде, затим да тражено време израчунаш у секундама, а онда да
добијени резултат претвориш у сате, минуте и секунде. 

.. activecode:: време_до_краја_видеа
   :runortest: trajanje_sati, trajanje_minuta, trajanje_sekundi, od_pocetka_sati, od_pocetka_minuta, od_pocetka_sekundi, preostalo_sati, preostalo_minuta, preostalo_sekundi
   :enablecopy:
		
   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   trajanje_sati = 1
   trajanje_minuta = 23
   trajanje_sekundi = 14
   
   od_pocetka_sati = 0
   od_pocetka_minuta = 47
   od_pocetka_sekundi = 53

   # -*- acsection: main -*-
   # izracunaj trajanje u sekundama
   trajanje = 0
   
   # izracunaj vreme od pocetka videa u sekundama
   od_pocetka = 0

   # izracunaj preostalo vreme u sekundama
   preostalo = 0
   # preracunaj to vreme u sate, minute i sekunde
   preostalo_sati = 0
   preostalo_minuta = 0
   preostalo_sekundi = 0
   
   # -*- acsection: after-main -*-
   print(preostalo_sati, ":", preostalo_minuta, ":", preostalo_sekundi)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for (trajanje_sati, trajanje_minuta, trajanje_sekundi, od_pocetka_sati, od_pocetka_minuta, od_pocetka_sekundi, preostalo_sati, preostalo_minuta, preostalo_sekundi) in [(2, 54, 15, 1, 48, 29, 1, 5, 46), (1, 44, 13, 0, 0, 19, 1, 43, 54)]:
             self.assertEqual(acMainSection(trajanje_sati = trajanje_sati, trajanje_minuta = trajanje_minuta, trajanje_sekundi = trajanje_sekundi, od_pocetka_sati = od_pocetka_sati, od_pocetka_minuta = od_pocetka_minuta, od_pocetka_sekundi = od_pocetka_sekundi)["preostalo_sati"],preostalo_sati,"Ако је трајање (%s, %s, %s), а од почетка је протекло (%s, %s, %s), тада је преостало (%s, %s, %s)." % (trajanje_sati, trajanje_minuta, trajanje_sekundi, od_pocetka_sati, od_pocetka_minuta, od_pocetka_sekundi, preostalo_sati, preostalo_minuta, preostalo_sekundi))
             self.assertEqual(acMainSection(trajanje_sati = trajanje_sati, trajanje_minuta = trajanje_minuta, trajanje_sekundi = trajanje_sekundi, od_pocetka_sati = od_pocetka_sati, od_pocetka_minuta = od_pocetka_minuta, od_pocetka_sekundi = od_pocetka_sekundi)["preostalo_minuta"],preostalo_minuta,"Ако је трајање (%s, %s, %s), а од почетка је протекло (%s, %s, %s), тада је преостало (%s, %s, %s)." % (trajanje_sati, trajanje_minuta, trajanje_sekundi, od_pocetka_sati, od_pocetka_minuta, od_pocetka_sekundi, preostalo_sati, preostalo_minuta, preostalo_sekundi))
             self.assertEqual(acMainSection(trajanje_sati = trajanje_sati, trajanje_minuta = trajanje_minuta, trajanje_sekundi = trajanje_sekundi, od_pocetka_sati = od_pocetka_sati, od_pocetka_minuta = od_pocetka_minuta, od_pocetka_sekundi = od_pocetka_sekundi)["preostalo_sekundi"],preostalo_sekundi,"Ако је трајање (%s, %s, %s), а од почетка је протекло (%s, %s, %s), тада је преостало (%s, %s, %s)." % (trajanje_sati, trajanje_minuta, trajanje_sekundi, od_pocetka_sati, od_pocetka_minuta, od_pocetka_sekundi, preostalo_sati, preostalo_minuta, preostalo_sekundi))
   myTests().main()

Ако урадиш све како треба, добићеш да је преостало ``0 : 35 :
21``. Провери и на другим тест-примерима.

.. reveal:: пресек_решење41
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   .. activecode:: време_до_краја_видеа_решење

      # ukupno vreme trajanja videa
      trajanje_sati = 1
      trajanje_minuta = 23
      trajanje_sekundi = 14
      
      # vreme proteklo od pocetka videa
      od_pocetka_sati = 0
      od_pocetka_minuta = 47
      od_pocetka_sekundi = 53

      # izracunaj trajanje u sekundama
      trajanje = (trajanje_sati*60 + trajanje_minuta)*60 + trajanje_sekundi
      
      # izracunaj vreme od_pocetka od pocetka videa u sekundama
      od_pocetka = (od_pocetka_sati*60 + od_pocetka_minuta)*60 + od_pocetka_sekundi
    
      # izracunaj preostalo vreme do kraja videa u sekundama
      preostalo = trajanje - od_pocetka
      # preracunaj to vreme u sate, minute i sekunde
      preostalo_sati = preostalo // (60 * 60)
      preostalo_minuta = (preostalo // 60) % 60
      preostalo_sekundi = preostalo % 60
      
      print(preostalo_sati, ":", preostalo_minuta, ":", preostalo_sekundi)

