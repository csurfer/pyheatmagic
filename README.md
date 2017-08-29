# heat

[![pypiv](https://img.shields.io/pypi/v/py-heat-magic.svg)](https://pypi.python.org/pypi/py-heat-magic)
[![pyv](https://img.shields.io/pypi/pyversions/py-heat-magic.svg)](https://pypi.python.org/pypi/py-heat-magic)
[![Licence](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/csurfer/pyheatmagic/master/LICENSE)
[![Thanks](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/csurfer)

IPython magic command to profile and view your python code as a heat map using [py-heat](https://github.com/csurfer/pyheat).

## Demo

![Demo](http://i.imgur.com/IUtasPH.gif)

In case the demo was too fast, here is a [snapshot](http://i.imgur.com/isxRNV0.png) of the last step of the demo for deeper contemplation :)

## What is the magic command?

```python
%%heat
```

## Setup

### Using pip

```bash
pip install py-heat-magic
```

### Directly from the repository

```bash
git clone https://github.com/csurfer/pyheatmagic.git
python pyheatmagic/setup.py install
```

### Load Extension in IPython

```python
%load_ext heat
```

## Usage

```python
# To view the heatmap
%%heat

# To save the heatmap as a file
%%heat -o file.png
```

## Contributing

### Bug Reports and Feature Requests

Please use [issue tracker](https://github.com/csurfer/pyheatmagic/issues) for reporting bugs or feature requests.

### Development

Pull requests are most welcome.

### Buy the developer a cup of coffee!

If you found the utility helpful you can buy me a cup of coffee using

[![Donate](https://www.paypalobjects.com/webstatic/en_US/i/btn/png/silver-pill-paypal-44px.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=3BSBW7D45C4YN&lc=US&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHosted)
