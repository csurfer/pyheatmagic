"""
heat
~~~~
Module implementing IPython cell magic to use pyheat.

Usage of heat:

To have heatmap displayed within ipython notebook.
>>> %%heat

To have heatmap exported as a image file.
>>> %%heat -o heat.png
>>> %%heat --out heat.png

:copyright: (c) 2017 by Vishwas B Sharma.
:license: MIT, see LICENSE for more details.
"""

__title__ = 'heat'
__version__ = '0.0.2'
__author__ = 'Vishwas B Sharma'
__author_email__ = 'sharma.vishwas88@gmail.com'
__license__ = 'MIT'
__copyright__ = 'Copyright 2017 Vishwas B Sharma'

import os
from tempfile import mkstemp

from IPython.core import magic_arguments
from IPython.core.magic import Magics, cell_magic, magics_class
from pyheat import PyHeat


@magics_class
class PyHeatMagic(Magics):
    """Class with IPython magic commands to effectively use py-heat profiling
    within IPython."""

    @magic_arguments.magic_arguments()
    @magic_arguments.argument('-o', '--out', default=None, help='Save the heatmap to given file')
    @cell_magic
    def heat(self, line, cell):
        """Method to profile the python code in the ipython cell and display it
        as a heatmap using py-heat package.

        :param line: Line value for the ipython line this magic is called from.
        :param cell: Cell value for the ipython cell this magic is called from.
        """
        args = magic_arguments.parse_argstring(self.heat, line)
        filename = args.out
        if filename is not None:
            filename = os.path.expanduser(args.out)

        _, tmp_file = mkstemp()
        with open(tmp_file, 'wb') as f:
            f.write(cell.encode())

        pyheat = PyHeat(tmp_file)
        pyheat.create_heatmap()
        pyheat.show_heatmap(output_file=filename)
        pyheat.close_heatmap()

        os.remove(tmp_file)


def load_ipython_extension(ipython):
    ipython.register_magics(PyHeatMagic)
