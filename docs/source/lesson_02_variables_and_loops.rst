.. role:: python(code)
   :language: python

Les 2: variabelen en loops
==========================

In de vorige les heb je kennisgemaakt met de turtle module in Python. Je schreef algoritmen om de schildpad te besturen en zodoende een tekening te laten maken. Die algoritmen bevatten best veel herhaling. Om bijvoorbeeld een vierkant te maken met zijden van 100 pixels, zou je de volgende code gebruiken:

.. code-block:: python
    :linenos:
    :emphasize-lines: 5-11
    :caption: turtle_square.py
    :name: turtle_square

    import turtle

    tony = turtle.Turtle()

    tony.fd(100)
    tony.lt(90)
    tony.fd(100)
    tony.lt(90)
    tony.fd(100)
    tony.lt(90)
    tony.fd(100)

De regels 5 tot en met 11 van :file:`turtle_square.py` bevatten slechts twee instructies: :python:`tony.fd(100)` en :python:`tony.lt(90)`. Kunnen we Python niet gewoon vertellen dat het die instructies vier keer moet uitvoeren, in plaats van zoveel regels code te gebruiken? Ja dat kan! En in deze les leer je hoe. Maar eerste moet je iets weten over variabelen.

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Onderdelen

   lesson_02/ch_01_variables
   lesson_02/ch_02_loops