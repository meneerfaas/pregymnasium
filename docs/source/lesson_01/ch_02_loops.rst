.. role:: python(code)
   :language: python

Code herhalen met loops
=======================

.. ToDo: nog wat inleiding schrijven (in het vorige onderdeel veel herhalende code getypt)

Variabelen
----------

.. grid:: 2
    :padding: 0

    .. grid-item::
        :columns: 6

        Voordat je je in loops gaat verdiepen, is het nodig dat je iets weet van *variabelen*. Een variabele is een plaats in het geheugen van de computer waarin je een waarde kunt opslaan. Je kunt een variabele vergelijken met een lade in een ladenkast. De lade heeft een label dat aangeeft wat er in zit en in de lade zit inhoud. Een variabele heeft een naam die (meestal) aangeeft wat er in zit en in de variabele zit een waarde.

    .. grid-item::
        :columns: 6

        .. image:: images/variables.png
          
Maak in Mu editor weer een nieuw bestand door op de knop :guilabel:`New` te klikken. Typ de onderstaande code in het bestand (dus niet kopiëren en plakken) en let daarbij op hoofd- en kleine letters en ook op spaties. Sla het bestand op als :file:`hello_variables.py`.

.. code-block:: python
    :class: no-copybutton
    :linenos:
    :caption: hello_variables.py
    :name: hello_variables_v01

    naam_tony = 'Tony'
    leeftijd_tony = 95
    print(naam_tony)
    print(leeftijd_tony)
          
In deze code wordt op regel 1 een variabele :python:`naam_tony` gemaakt, waarin de waarde :python:`'Tony'` wordt opgeslagen. Op regel 2 krijgt de variabele :python:`leeftijd_tony` de waarde :python:`95` (schildpadden kunnen heel oud worden). De functie :python:`print()` op regels 3 en 4 toont de waarden van :python:`naam_tony` en :python:`leeftijd_tony` op het scherm.

.. grid:: 1
    :padding: 0

    .. grid-item:: 
        :columns: auto
        
        .. image:: images/hello_variables.png


.. dropdown:: Meer weten over het maken van een variabele?
    :color: info
    :icon: info

    Een variabele maak je door een (zelfbedachte) **variabelenaam** te typen, gevolgd door een **is-gelijk-aan-teken** en de **waarde** die je in de variabele wilt opslaan. Dit bij elkaar heet in het Engels een *assignment statement*.

    .. card:: Assignment statement

        :python:`<variabelenaam> = <waarde>`

    Je mag de variabelenaam zelf bedenken, maar hij moet wel aan enkele voorwaarden voldoen:

        * De naam moet beginnen met een letter of het underscore karakter (:python:`_`).
        * De naam mag niet met een cijfer beginnen.
        * De naam mag alleen letters, cijfers en het underscore karakter bevatten.
  
    Variabelenamen zijn hoofdlettergevoelig. Dus :python:`leeftijd` en :python:`Leeftijd` zijn twee verschillende variabelen.


Het aardige van variabelen is dat je ermee kunt rekenen. Breid je code als volgt uit:

.. code-block:: python
    :class: no-copybutton
    :linenos:
    :emphasize-lines: 2,4,7,8
    :caption: hello_variables.py
    :name: hello_variables_v02

    naam_tony = 'Tony'
    naam_tina = 'Tina'
    leeftijd_tony = 95
    leeftijd_tina = leeftijd_tony - 5
    print(naam_tony)
    print(leeftijd_tony)
    print(naam_tina)
    print(leeftijd_tina)

Begrijp je wat in regel 4 gebeurt? De variabele :python:`leeftijd_tina` krijgt hier de waarde :python:`leeftijd_tony - 5` oftewel de waarde 90.

Met variabelen waarin getallen zijn opgeslagen kun je rekenen zoals je gewend bent. Maar ook met tekstvariabelen kun je een beetje rekenen. Voeg onderstaande regels toe aan je code:

.. code-block:: python
    :class: no-copybutton
    :linenos:
    :lineno-start: 9
    :caption: hello_variables.py
    :name: hello_variables_v02_contd

    print(leeftijd_tony + leeftijd_tina)
    print(naam_tony + naam_tina)
    print(3 * naam_tony)

Run de code en je krijgt de volgende output:

.. code-block:: text
    :class: no-copybutton
    :caption: hello_variables.py output
    :name: hello_variables_v02_contd

    Tony
    95
    Tina
    90
    185
    TonyTina
    TonyTonyTony

Wanneer je twee tekstwaarden 'optelt', plakt Python ze aan elkaar. Dus :python:`'Tony' + 'Tina'` geeft :python:`'TonyTina'`. 

Het sterretje :python:`*` is in Python het symbool voor vermenigvuldiging. Wanneer je een tekstwaarde met een getal 'vermenigvuldigt', herhaalt Python de tekst zo vaak als het getal aangeeft. Dus :python:`3 * 'Tony'` geeft :python:`TonyTonyTony`.

.. dropdown:: Meer weten over soorten variabelen?
    :color: info
    :icon: info

    Hoe weet Python dat het bij het optellen van twee getallen gewoon moet optellen, maar bij het 'optellen' van twee tekstwaarden die waarden aan elkaar moet plakken? Dat weet Python door naar de *datatypes* te kijken. Door de aanhalingstekens om :python:`'Tony'` en :python:`'Tina'`, weet Python dat de variabelen :python:`naam_tony` en :python:`naam_tina` van het datatype :python:`string` zijn. En Python weet dat een :python:`+` tussen twee stringvariabelen betekent 'plak aan elkaar'.
    
    De variabelen :python:`leeftijd_tony` en :python:`leeftijd_tina` zijn van het datatype :python:`integer`. Dat is Engels voor *geheel getal*.

    Je kunt achter het datatype van een variabele komen met de functie :python:`type()`. Probeer de volgende code maar eens uit (je mag de code in :file:`hello_variables.py` vervangen).

    .. code-block:: python
        :linenos:
        :name: hello_variables_datatypes

        naam = 'Alan'
        leeftijd = 11
        lichaamslengte = 1.54

        print(type(naam))
        print(type(leeftijd))
        print(type(lichaamslengte))

    Je ziet dat Python de datatypes van de drie variabelen print:

    .. list-table::
        :header-rows: 1

        * - Variabele
          - Resultaat :python:`type()`
          - Datatype
          - Betekenis
        * - :python:`naam`
          - :python:`<class 'str'>`
          - string
          - tekstwaarde
        * - :python:`leeftijd`
          - :python:`<class 'int'>`
          - integer
          - geheel getal
        * - :python:`lichaamslengte`
          - :python:`<class 'float'>`
          - floating point
          - kommagetal


.. dropdown:: Opdracht 01
    :color: secondary
    :icon: pencil

    Verwijder alle code uit :file:`hello_variables.py`. Schrijf in het lege bestand code die het volgende doet:

    1.  Een variabele :python:`aantal_appels` aanmaken met de waarde :python:`8`.
    2.  Een variabele :python:`prijs_per_appel` aanmaken met de waarde :python:`0.75`.
    3.  Een variabele :python:`totale_prijs` aanmaken waarin je het product (dat is de vermenigvuldiging) van de vorige twee variabelen opslaat.
    4.  De waarde van :python:`totale_prijs` tonen op het scherm.     

    .. dropdown:: Oplossing
        :color: secondary
        :icon: check-circle

        .. code-block:: python
            :linenos:
            :caption: hello_variables.py
            :name: hello_variables_opdr01

            aantal_appels = 8
            prijs_per_appel = 0.75
            totale_prijs = aantal_appels * prijs_per_appel
            print(totale_prijs)

.. dropdown:: Opdracht 02
    :color: secondary
    :icon: pencil

    Bekijk de onderstaande code en probeer eerst uit je hoofd te beredeneren wat de waarden van :python:`a`, :python:`b` en :python:`c` zijn nadat deze code is uitgevoerd. Controleer daarna je antwoord door de code naar Mu editor (vervang de code in het bestand :file:`hello_variables`) te kopiëren en te runnen.   
    
    .. code-block:: python
        :linenos:
        :name: hello_variables_opdr02

        a = 5
        b = a + 2
        c = b * b
        a = c - b
        print(a, b, c)

    .. dropdown:: Oplossing
        :color: secondary
        :icon: check-circle

        :python:`a` heeft de waarde 42, :python:`b` heeft de waarde 7 en :python:`c` heeft de waarde 49.   

While loops
-----------

Maak in Mu editor weer een nieuw bestand door op de knop :guilabel:`New` te klikken. Kopieer en plak de onderstaande code in het bestand en sla het op als :file:`turtle_while.py`.

.. code-block:: python
    :linenos:
    :caption: turtle_while.py
    :name: turtle_while

    import turtle

    tony = turtle.Turtle()

    zijde = 0
    while zijde < 4:
        tony.forward(100)
        tony.lt(90)
        zijde = zijde + 1

Run de code om het resultaat te bekijken.