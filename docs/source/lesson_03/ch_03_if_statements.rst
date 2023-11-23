.. role:: python(code)
   :language: python

Als... dan...
=============

Je hebt inmiddels kennisgemaakt met :python:`while` en :python:`for` loops, die je in staat stellen een blok code te herhalen. In dit hoofdstuk behandelen we het :python:`if` statement, waarmee Python kan kiezen om een blok code wel of niet uit te voeren.

Kopieer onderstaande code naar een nieuw bestand in Mu editor en sla het op als hello_if.py. 

.. code-block:: python
    :linenos:
    :caption: hello_if.py
    :name: hello_if_v01

    # Functie say_hello() toont een begroeting
    def say_hello(name):
        print("Hallo", name)
        
    # Hoofdprogramma
    say_hello("Tony")
    say_hello("Tina")

In :file:`hello_if.py` wordt de functie :python:`say_hello()` gedefinieerd, die een begroeting op het scherm toont. In regels 6 en 7 wordt deze functie aangeroepen met twee verschillende namen. De output van het programma is:

.. code-block:: text
    :caption: hello_if.py output
    :name: hello_if_v01_output

    Hallo Tony
    Hallo Tina

Nu gaan we de functie :python:`say_hello()` uitbreiden met een :python:`if` statement:

.. code-block:: python
    :linenos:
    :emphasize-lines: 3,4
    :caption: hello_if.py
    :name: hello_if_v02

    # Functie say_hello() toont een begroeting
    def say_hello(name):
        if name == "Tony":
            print("Hallo", name)
        
    # Hoofdprogramma
    say_hello("Tony")
    say_hello("Tina")

Met het dubbele is-gelijk-aan-teken :python:`==` kun je Python laten checken of twee waarden aan elkaar gelijk zijn. Regel 3 van :file:`hello_if.py` kun je dus lezen als: 'Als de waarde van de variabele :python:`name` gelijk is aan :python:`"Tony"`, doe dan het volgende.' Merk op dat de inspringing van regel 4 aangeeft dat die regel binnen het :python:`if` statement valt.

Wanneer je deze code runt, is de output:

.. code-block:: text
    :caption: hello_if.py output
    :name: hello_if_v02_output

    Hallo Tony

Het programma toont nu alleen een begroeting als de naam Tony wordt gebruikt en anders niet.

If en else
----------

Een :python:`if` statement gebruik je om Python te vertellen: *'Als er dit aan de hand is, doe dan het volgende.'* Met het keyword :python:`else`  kun je dat uitbreiden naar *'Als er dit aan de hand is, doe dan het volgende, en zo niet, doe dan iets anders.'*

Wijzig de functie :python:`say_hello()` als volgt:

.. code-block:: python
    :linenos:
    :emphasize-lines: 5-8
    :caption: hello_if.py
    :name: hello_if_v03

    # Functie say_hello() toont een begroeting
    def say_hello(name):
        if name == "Tony":
            print("Hallo", name)
            print("Leuk je weer te zien.")
        else:
            print("Hallo", name)
            print("Aangenaam kennis te maken.")
        
    # Hoofdprogramma
    say_hello("Tony")
    say_hello("Tina")

Begrijp je wat hier gebeurt? De regels 4 en 5 worden uitgevoerd als aan de functie :python:`say_hello()` het argument :python:`"Tony"` wordt meegegeven. In alle andere gevallen worden de regels 7 en 8 uitgevoerd. Je kunt aan het hoofdprogramma nog extra regels toevoegen om het effect te zien:

.. code-block:: python
    :linenos:
    :lineno-start: 10
    :emphasize-lines: 2
    :caption: hello_if.py
    :name: hello_if_v04

    # Hoofdprogramma
    say_hello("Tabe")
    say_hello("Tess")
    say_hello("Tony")
    say_hello("Tina")

Run het programma en zie dat alleen bij de naam Tony de reactie 'Leuk je weer te zien.' wordt geprint.

Wanneer je deze code runt, is de output:

.. code-block:: text
    :emphasize-lines: 5,6
    :caption: hello_if.py output
    :name: hello_if_v04_output

    Hallo Tabe
    Aangenaam kennis te maken.
    Hallo Tess
    Aangenaam kennis te maken.
    Hallo Tony
    Leuk je weer te zien.
    Hallo Tina
    Aangenaam kennis te maken.

Elif
----

Je kunt een :python:`if` statement nog verder uitbreiden met het keyword :python:`elif`, dat staat voor 'else if'. In de onderstaande code zie je hoe dat werkt. Hierin is tevens de aanroep :python:`print("Hallo", name)` buiten het :python:`if` statement geplaatst (op regel 3) omdat we die begroeting voor elke naam willen tonen.

.. code-block:: python
    :linenos:
    :emphasize-lines: 3-9
    :caption: hello_if.py
    :name: hello_if_v05

    # Functie say_hello() toont een begroeting
    def say_hello(name):
        print("Hallo", name)
        if name == "Tony":
            print("Leuk je weer te zien.")
        elif name == "Tina":
            print("Hoe gaat het met je?")
        else:
            print("Aangenaam kennis te maken.")
        
    # Hoofdprogramma
    say_hello("Tabe")
    say_hello("Tess")
    say_hello("Tony")
    say_hello("Tina")

Op regel 4 checkt Python of de waarde van :python:`name` gelijk is aan :python:`"Tony"`. Zo ja, dan wordt regel 5 uitgevoerd. Zo nee, dan checkt Python in regel 6 of :python:`name` misschien de waarde :python:`"Tina"` bevat. Zo ja, dan wordt regel 7 uitgevoerd. Zo nee, dan zorgt regel 8 ervoor dat de code in regel 9 wordt uitgevoerd.

.. code-block:: text
    :caption: hello_if.py output
    :name: hello_if_v05_output

    Hallo Tabe
    Aangenaam kennis te maken.
    Hallo Tess
    Aangenaam kennis te maken.
    Hallo Tony
    Leuk je weer te zien.
    Hallo Tina
    Hoe gaat het met je?

And en or
---------

In een :python:`if` statement kun je gebruik maken van :python:`and` en :python:`or` om voorwaarden te combineren. Stel dat we zowel Tony als Tina willen begroeten met de zin 'Leuk je weer te zien.', dan zouden we de functie :python:`say_hello()` als volgt kunnen aanpassen (het hoofdprogramma blijft ongewijzigd):

.. code-block:: python
    :linenos:
    :caption: hello_if.py
    :name: hello_if_v06

    # Functie say_hello() toont een begroeting
    def say_hello(name):
        print("Hallo", name)
        if name == "Tony" or name == "Tina":
            print("Leuk je weer te zien.")
        else:
            print("Aangenaam kennis te maken.")

In regel 4 staat :python:`if name == "Tony" or name == "Tina":`. Het keyword :python:`or` betekent **of**. Hier staat dus: 'Als de waarde van :python:`name` gelijk is aan :python:`"Tony"` **of** als de waarde van :python:`name` gelijk is aan :python:`"Tina"`, doe dan het volgende.'

.. dropdown:: Vraag 01
    :color: secondary
    :icon: question

    Het keyword :python:`and` betekent **en**. Wat zou er gebeuren als je regel 4 wijzigt in :python:`if name == "Tony" and name == "Tina":`? Probeer het maar eens uit. Kun je het resultaat verklaren?

    .. dropdown:: Antwoord
        :color: secondary
        :icon: check-circle

        De waarde van :python:`name` kan niet tegelijkertijd zowel :python:`"Tony"` als :python:`"Tina"` zijn. Dus :python:`name == "Tony" and name == "Tina"` is altijd onwaar. Daardoor springt de code naar regel 6 en wordt elke naam begroet met :python:`"Aangenaam kennis te maken."`.
