heat
====

|pypiv| |pyv| |Licence| |Thanks|

IPython magic command to profile and view your python code as a heat map
using `py-heat`_.

Demo
----

|Demo|

In case the demo was too fast, here is a `snapshot`_ of the last step of the
demo for deeper contemplation :)

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

Contributing
------------

Bug Reports and Feature Requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please use `issue tracker`_ for reporting bugs or feature requests.

Development
~~~~~~~~~~~

Pull requests are most welcome.

Buy the developer a cup of coffee!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you found the utility helpful you can buy me a cup of coffee using

|Donate|



.. _py-heat: https://github.com/csurfer/pyheat

.. _snapshot: http://i.imgur.com/isxRNV0.png

.. _issue tracker: https://github.com/csurfer/pyheatmagic/issues

.. |Donate| image:: https://www.paypalobjects.com/webstatic/en_US/i/btn/png/silver-pill-paypal-34px.png
   :target: https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=3BSBW7D45C4YN&lc=US&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHosted

.. |Thanks| image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
   :target: https://saythanks.io/to/csurfer

.. |Demo| image:: http://i.imgur.com/IUtasPH.gif

.. |Licence| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/csurfer/pyheatmagic/master/LICENSE

.. |pypiv| image:: https://img.shields.io/pypi/v/py-heat-magic.svg
   :target: https://pypi.python.org/pypi/py-heat-magic

.. |pyv| image:: https://img.shields.io/pypi/pyversions/py-heat-magic.svg
   :target: https://pypi.python.org/pypi/py-heat-magic