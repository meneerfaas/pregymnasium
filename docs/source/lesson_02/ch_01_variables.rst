.. role:: python(code)
   :language: python

Variabelen
==========

.. grid:: 2
    :padding: 0

    .. grid-item::
        :columns: 6

        Voordat je je in loops gaat verdiepen, is het nodig dat je iets weet van *variabelen*. Een variabele is een plaats in het geheugen van de computer waar je een waarde kunt opslaan. Je kunt een variabele vergelijken met een lade in een ladenkast. De lade heeft een label dat aangeeft wat er in zit en in de lade zit inhoud. Een variabele heeft een naam die (meestal) aangeeft wat er in zit en in de variabele zit een waarde.

    .. grid-item::
        :columns: 6

        .. image:: images/variables.png

          
Maak in Mu editor een nieuw bestand door op de knop :guilabel:`New` te klikken. Typ de onderstaande code in het bestand (dus niet kopiëren en plakken) en let daarbij op hoofd- en kleine letters en ook op spaties. Sla het bestand op als :file:`turtle_variables.py`.

.. code-block:: python
    :class: no-copybutton
    :linenos:
    :caption: turtle_variables.py
    :name: turtle_variables_v01

    import turtle

    tony = turtle.Turtle()

    lengte = 100
    tony.fd(lengte)
          
In deze code wordt op regel 5 een variabele :python:`lengte` gemaakt, waarin de waarde :python:`100` wordt opgeslagen. In regel 6 gebruiken we de variabele bij het aanroepen van :python:`tony.fd(lengte)`. 

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
  
    Variabelenamen zijn hoofdlettergevoelig. Dus :python:`lengte` en :python:`Lengte` zijn twee verschillende variabelen.

Het nut van de variabele :python:`lengte` is nu nog niet zo duidelijk. Maar breid je code eens uit als volgt:

.. code-block:: python
    :linenos:
    :emphasize-lines: 7-12
    :caption: turtle_variables.py
    :name: turtle_variables_v02

    import turtle

    tony = turtle.Turtle()

    lengte = 100
    tony.fd(lengte)
    tony.lt(90)
    tony.fd(lengte)
    tony.lt(90)
    tony.fd(lengte)
    tony.lt(90)
    tony.fd(lengte)

Deze code tekent een vierkant met zijden van 100 pixels. Hoe zou je de code moeten aanpassen om zijden van 200 pixels te laten tekenen? Juist, je hoeft slechts regel 5 aan te passen naar :python:`lengte = 200`. Zouden we geen variabele hebben gebruikt, dan had je vier regels code moeten aanpassen (regels 6, 8, 10 en 12 wijzigen naar :python:`tony.fd(200)` ) en nu maar één!

Het aardige van variabelen is dat je ermee kunt rekenen. Wijzig bijvoorbeeld je code als volgt:

.. code-block:: python
    :linenos:
    :emphasize-lines: 6,10,14
    :caption: turtle_variables.py
    :name: turtle_variables_v03

    import turtle

    tony = turtle.Turtle()

    lengte = 100
    breedte = lengte / 2

    tony.fd(lengte)
    tony.lt(90)
    tony.fd(breedte)
    tony.lt(90)
    tony.fd(lengte)
    tony.lt(90)
    tony.fd(breedte)

Begrijp je wat hier gebeurt? De variabele :python:`breedte` krijgt in regel 6 de waarde :python:`lengte / 2`. oftewel de helft van de lengte. De code tekent een rechthoek waarvan de breedte de helft is van de lengte.

.. dropdown:: Opdracht 01
    :color: secondary
    :icon: pencil

    Pas de code in :file:`turtle_variables.py` zodanig aan dat een rechthoek wordt getekend waarvan de breedte 20 pixels minder is dan de lengte en waarvan de lengte 180 pixels is.

    .. dropdown:: Oplossing
        :color: secondary
        :icon: check-circle

        .. code-block:: python
            :linenos:
            :emphasize-lines: 5,6
            :caption: turtle_variables.py
            :name: turtle_variables_opdr01

            import turtle

            tony = turtle.Turtle()

            lengte = 180
            breedte = lengte - 20

            tony.fd(lengte)
            tony.lt(90)
            tony.fd(breedte)
            tony.lt(90)
            tony.fd(lengte)
            tony.lt(90)
            tony.fd(breedte)

.. dropdown:: Opdracht 02
    :color: secondary
    :icon: pencil

    Vervang de code in :file:`turtle_variables.py` door onderstaande code.

    .. code-block:: python
        :linenos:
        :caption: turtle_variables.py
        :name: turtle_variables_opdr02

        import turtle

        tony = turtle.Turtle()
        tony.pensize(3)

        r = 40

        tony.circle(r)

    Vul de code aan zodat :python:`tony` om de cirkel een vierkant tekent, zoals hieronder getoond. Je moet daarbij de variabele :python:`r` gebruiken.

    Als je de code hebt gemaakt, geef dan in regel 6 de variabele :python:`r` een andere waarde, bijvoorbeeld :python:`r = 60` en controleer dat nog steeds het juiste vierkant wordt getekend. 

    .. image:: images/circle_in_square.png

.. dropdown:: Opdracht 03
    :color: secondary
    :icon: pencil

    Dit is een opdracht zonder turtle. Bekijk de onderstaande code en probeer eerst uit je hoofd te beredeneren wat de waarden van de variabelen :python:`getal1`, :python:`getal2`, :python:`getal3`  en :python:`getal4` zijn nadat deze code is uitgevoerd. Controleer daarna je voorspelling door in Mu editor een nieuw bestand te maken, de code daarin te kopiëren en te runnen (sla het bestand op als :file:`hello_variables.py`). Klopte je voorspelling?
    
    .. code-block:: python
        :linenos:
        :name: hello_variables_opdr02

        getal1 = 3
        getal2 = getal1 + 2
        getal3 = getal2 * (getal1 + getal2)
        getal4 = getal3 - getal2

        print("getal1 =", getal1)
        print("getal2 =", getal2)
        print("getal3 =", getal3)
        print("getal4 =", getal4)

    .. dropdown:: Oplossing
        :color: secondary
        :icon: check-circle

        .. code-block:: text
            :name: hello_variables_opdr02_opl

            getal1 = 3
            getal2 = 5
            getal3 = 40
            getal4 = 35  