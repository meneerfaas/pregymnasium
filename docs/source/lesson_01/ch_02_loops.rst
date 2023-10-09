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

.. image:: images/hello_variables.png

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