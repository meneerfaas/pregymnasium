.. role:: python(code)
   :language: python

Les 1: algoritmen
=================

Een *algoritme* is een reeks instructies die leidt tot een einddoel. Eenvoudiger gezegd is een algoritme een stappenplan. Wellicht denk je bij algoritmen meteen aan computers, maar dat hoeft niet. In het dagelijks leven gebruik je onbewust allerlei algoritmen. Bijvoorbeeld om je tanden te poetsen:

.. grid:: 2

    .. grid-item::
        :columns: auto

        1. Draai de kraan open.
        2. Spoel je mond.
        3. Pak je tandenborstel.
        4. Spoel je tandenborstel af.
        5. Pak de tandpasta.
        6. Draai het dopje van de tandpasta los.
        7. ... enzovoort

    .. grid-item::
        :columns: auto

        .. image:: ../images/teethbrushing.png

In deze les ga je aan de slag met algoritmen om in Python een schildpad (Engels: turtle) te besturen.

Python Turtle
-------------

Start in Mu editor met een nieuw bestand door op de knop :guilabel:`New` te klikken. Typ onderstaande code in het bestand en let daarbij goed op het verschil tussen hoofdletters en kleine letters! Sla het bestand op als :file:`hello_turtle.py` in de Documenten map.

.. code-block:: python
    :class: no-copybutton
    :linenos:
    :caption: hello_turtle.py
    :name: hello_turtle_v01

    import turtle

    tony = turtle.Turtle()

    tony.forward(100)

Run deze code om het resultaat te bekijken.

Sommige functies zoals :python:`print()` zitten standaard in Python, maar om met de schildpad te kunnen werken is het nodig de module :python:`turtle` te importeren. Dat gebeurt op regel 1. Op regel 3 maken we met de functie :python:`Turtle()` uit de :python:`turtle` module een schildpad aan met de naam :python:`tony`. Op regel 5 sturen we :python:`tony` 100 pixels naar voren.

.. image:: ../images/turtle_01.png
    :scale: 50%

Maar wat is dat nu? Onze Tony lijkt helemaal niet op een schildpad! Hij lijkt meer op een pijlpunt! Daar gaan we verandering in brengen. En we gaan hem ook van richting laten veranderen. Pas je code als volgt aan (de nieuwe regels zijn gemarkeerd):

.. code-block:: python
    :class: no-copybutton
    :linenos:
    :caption: hello_turtle.py
    :name: hello_turtle_v02
    :emphasize-lines: 4,7-12

    import turtle

    tony = turtle.Turtle()
    tony.shape('turtle')

    tony.forward(100)
    tony.left(90)
    tony.forward(50)
    tony.left(90)
    tony.forward(100)
    tony.left(90)
    tony.forward(50)

Op regel 4 zorgt :python:`tony.shape('turtle')` ervoor dat onze schildpad er ook uitziet als een schildpad. De regels 7 t/m 12 laten :python:`tony` af en toe linksaf slaan alvorens verder te lopen.

.. dropdown:: Meer weten over turtle shapes?
    :color: info
    :icon: info

    Om de vorm van :python:`tony` in een schildpad te veranderen, gaven we de functie :python:`tony.shape()` de waarde :python:`'turtle'` mee. Er zijn echter nog andere vormen mogelijk. Dit is de volledige lijst:

    * :python:`'arrow'`
    * :python:`'turtle'`
    * :python:`'circle'`
    * :python:`'square'`
    * :python:`'triangle'`
    * :python:`'classic'`
 
De waarde die je tussen de haakjes aan de functie :python:`tony.forward()` meegeeft, is het aantal pixels dat de schildpad vooruit moet bewegen. Maar wat doet het getal :python:`90` tussen de haakjes van :python:`tony.left()`?

.. dropdown:: Vraag 01
    :color: secondary
    :icon: question

    Wat betekent het getal :python:`90` tussen de haakjes van :python:`turtle.left()`?

    .. dropdown:: Antwoord
        :color: secondary
        :icon: check-circle

        Dat getal geeft aan hoeveel **graden** de turtle moet draaien. Een hoek van 90° is een rechte hoek. De aanroep :python:`turtle.left(90)` zorgt er dus voor dat de turtle 90° naar links draait, oftewel linksaf slaat.

        In onderstaande figuur zie je hoe een cirkel in graden is verdeeld. Hoeveel graden zitten er in een volledige cirkel denk je?

        .. image:: ../images/turtle_angles.png

De basisbewegingen
------------------
        
Tot nu toe hebben we in onze code voor de beweging van de schilpad de functies :python:`forward()` en :python:`left()` gebruikt. Kun je voorspellen welke bewegingsfuncties er nog meer zijn? Juist, :python:`backward()` en :python:`right()`. Omdat je deze vier functies heel vaak gebruikt, zijn er afkortingen voor, zodat je minder hoeft te typen.

.. list-table:: Afkortingen van de turtle functies
    :header-rows: 1

    * - Functie
      - Afkorting
    * - :python:`turtle.forward()`
      - :python:`turtle.fd()`
    * - :python:`turtle.backward()`
      - :python:`turtle.bk()`
    * - :python:`turtle.left()`
      - :python:`turtle.lt()`
    * - :python:`turtle.right()`
      - :python:`turtle.rt()`


.. dropdown:: Opdracht 01
    :color: secondary
    :icon: pencil

    Vervang de code in :file:`hello_turtle.py` door onderstaande code. Je hoeft de code niet over te typen, je kunt kopiëren en plakken.

    .. code-block:: python
        :linenos:
        :caption: hello_turtle.py
        :name: hello_turtle_oef01

        import turtle

        tony = turtle.Turtle()
        tony.shape('turtle')

        tony.lt(90)
        tony.fd(100)
        tony.bk(50)
        tony.rt(90)
        tony.fd(60)

    Run de code om te zien dat de schildpad het begin van een hoofdletter H tekent. Maak de code af zodat een volledige hoofdletter H wordt getekend. 

Pen up, pen down en pen size
----------------------------

Zoals je hebt gemerkt, is :python:`tony` een schildpad die van tekenen houdt, want hij heeft een pen vast waarmee hij zijn afgelegde weg tekent. Soms wil je echter dat :python:`tony` zijn pen even van het 'papier' haalt. Met de volgende twee functies kun je de pen van de schildpad bedienen:

.. list-table::
    :header-rows: 1

    * - Functie
      - Afkorting
    * - :python:`turtle.penup()`
      - :python:`turtle.pu()` of :python:`turtle.up()`
    * - :python:`turtle.pendown()`
      - :python:`turtle.pd()` of :python:`turtle.down()`

Daarnaast kun je de pendikte instellen met de volgende functie:

.. list-table::
    :header-rows: 1

    * - Functie
    * - :python:`turtle.pensize()`

Bij de functies :python:`turtle.penup()` en :python:`turtle.pendown()` zet je niks tussen de haakjes, maar de functie :python:`turtle.pensize()` heeft wél input nodig. Tussen de haakjes zet je een geheel getal dat de pendikte in pixels aangeeft. Dus bijvoorbeeld :python:`turtle.pensize(10)`

.. dropdown:: Opdracht 02
    :color: secondary
    :icon: pencil

    Breid je code in :file:`hello_turtle.py` uit zodat naast de letter H ook een hoofdletter E wordt getekend, met pendikte 5.

    .. image:: ../images/turtle_HE.png

    Kies zelf mooie lengtes voor de drie horizontale lijnen van de letter E, zodat je resultaat lijkt op het bovenstaande plaatje.

Kleuren
-------

Onze schildpad tekent vooralsnog zwarte lijnen; tijd voor wat fleurigheid! Uiteraard is er een functie om de penkleur van :python:`tony` te veranderen.

.. list-table::
    :header-rows: 1

    * - Functie
    * - :python:`turtle.pencolor()`

Tussen de haakjes geef je de gewenste kleur mee met de Engelse naam tussen aanhalingstekens, bijvoorbeeld :python:`turtle.pencolor('yellow')` of :python:`turtle.pencolor('green')`. Andere kleuren zijn :python:`gold`, :python:`orange`, :python:`red`, :python:`maroon`, :python:`violet`, :python:`magenta`, :python:`purple`, :python:`navy`, :python:`blue`, :python:`skyblue`, :python:`cyan`, :python:`turquoise`, :python:`lightgreen`, :python:`darkgreen`, :python:`chocolate`, :python:`brown`, :python:`black` en :python:`gray`. En er zijn er nog veel meer! Op `deze website <https://trinket.io/docs/colors>`_ kun je een kleurenpalet vinden.

.. dropdown:: Opdracht 03
    :color: secondary
    :icon: pencil

    Breid je code in :file:`hello_turtle.py` uit zodat de schildpad het woord HELLO tekent, waarbij elke letter een andere kleur en een andere pendikte heeft. Je mag zelf je favoriete kleuren en pendiktes kiezen. Hieronder staat een voorbeeldje.

    .. image:: ../images/turtle_HELLO.png