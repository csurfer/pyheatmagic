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
__version__ = '0.0.1'
__author__ = 'Vishwas B Sharma'
__author_email__ = 'sharma.vishwas88@gmail.com'
__license__ = 'MIT'
__copyright__ = 'Copyright 2017 Vishwas B Sharma'

import os

from IPython.core import magic_arguments
from IPython.core.magic import Magics, cell_magic, magics_class
from pyheat import PyHeat


@magics_class
class PyHeatMagic(Magics):
    @magic_arguments.magic_arguments()
    @magic_arguments.argument(
        '-o',
        '--out',
        default=None,
        help='Save the heatmap to given file'
    )
    @cell_magic
    def heat(self, line, cell):
        args = magic_arguments.parse_argstring(self.heat, line)
        filename = args.out
        if filename is not None:
            filename = os.path.expanduser(args.out)

        tmp_file = 'ipython_cell_input.py'
        with open(tmp_file, 'wb') as f:
            f.write(cell)

        pyheat = PyHeat(tmp_file)
        pyheat.create_heatmap()
        pyheat.show_heatmap(output_file=filename)
        pyheat.close_heatmap()


def load_ipython_extension(ipython):
    ipython.register_magics(PyHeatMagic)
