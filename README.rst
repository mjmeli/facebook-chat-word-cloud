facebook-chat-word-cloud
========================
.. image:: https://travis-ci.org/mjmeli/facebook-chat-word-cloud.svg?branch=master
    :target: https://travis-ci.org/mjmeli/facebook-chat-word-cloud
A Python tool for generating a word cloud for a Facebook chat conversation.

Requirements
------------
This uses `lxml` to parse the messages file provided by Facebook. This requires `libxml2` and `libxslt` to be installed.

For Debian/Ubuntu:

    sudo apt-get install libxml2-dev libxslt-dev python-dev

This also uses `Pillow` to handle image manipulation. This requires `libjpeg`, `zlib`, and `libfreetype`:

    sudo apt-get install libjpeg-dev zlib1g-dev libfreetype6-dev

Installation
------------
    pip install .

Development
-----------
    pip install -e .

Testing
-------
    python setup.py test

Releasing
---------
https://python-packaging.readthedocs.io/en/latest/minimal.html

Parser Choice
-------------
Benchmarks from attempting to analyze a 60 MB file:

+---------------+-------------------------+-------------------+
| Parser        | Build Tree Runtime (ms) | Max Memory Usage  |
+===============+=========================+===================+
| BeautifulSoup | 90750                   | 3450 MB (3.45 GB) |
+---------------+-------------------------+-------------------+
| lxml          | 1945                    | 910 MB (0.91 GB)  |
+---------------+-------------------------+-------------------+

Issues
------
**ImportError: The _imagingft C module is not installed**
This means you don't have `libfreetype` installed. See the Requirements section. If installing it does not work, you may have to uninstall and reinstall `Pillow` via `pip`.
