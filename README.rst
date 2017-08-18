heat
====

|pypiv| |pyv| |Licence|

IPython magic command to profile and view your python code as a heat map
using `py-heat`_.

|Demo|

What is the magic command?
--------------------------

.. code:: python

    %%heat

Setup
-----

Using pip
~~~~~~~~~

.. code:: bash

    pip install py-heat-magic

Directly from the repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    git clone https://github.com/csurfer/pyheatmagic.git
    python pyheatmagic/setup.py install

Load Extension in IPython
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    %load_ext heat

Usage
-----

.. code:: python

    # To view the heatmap
    %%heat

    # To save the heatmap as a file
    %%heat -o file.png

.. _py-heat: https://github.com/csurfer/pyheat

.. |Demo| image:: http://i.imgur.com/IUtasPH.gif

.. |Licence| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/csurfer/pyheatmagic/master/LICENSE

.. |pypiv| image:: https://img.shields.io/pypi/v/py-heat-magic.svg
   :target: https://pypi.python.org/pypi/py-heat-magic

.. |pyv| image:: https://img.shields.io/pypi/pyversions/py-heat-magic.svg
   :target: https://pypi.python.org/pypi/py-heat-magic