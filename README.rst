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

+---------------+-----------------------------+-------------------+
| Parser        | Runtime (ms)                | Max Memory Usage  |
|               +------------+----------------+                   |
|               | Build Tree | Parse Messages |                   |
+===============+============+================+===================+
| BeautifulSoup | 90750      | 9300           | 3450 MB (3.45 GB) |
+---------------+------------+----------------+-------------------+
| lxml          | 1945       | 935            | 910 MB (0.91 GB)  |
+---------------+------------+----------------+-------------------+

.. image:: http://i.imgur.com/Si3LZG8.png
