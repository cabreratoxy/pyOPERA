Setup & Installation
====================

Installation
------------

To use PyOPERA, first install it using pip:

.. code-block:: console

   (.venv) $ pip install pyopera

PyOPERA is written on top of a Python package generated from a MATLAB project. It requires a MATLAB Runtime installation to work properly. MATLAB Runtime can be installed
in Windows, Linux, MacOS (however Windows is not currently supported in this version). It can also be installed from the command line using silent mode. For more information head over to the `MATLAB Runtime docs <https://www.mathworks.com/help/compiler/install-the-matlab-runtime.html>`_.
Download files can be found `here <https://www.mathworks.com/products/compiler/matlab-runtime.html>`_. This package was tested on MATLAB Runtime 9.12.

.. note::

   PyOPERA is not currently directly supported on Windows due to the base package not running on Windows. You can run it on Windows with WSL 2 or Docker but not directly on Windows.


Usage
------------

you can use the ``easy_opera()`` function:

.. autofunction:: pyopera.opera.opera.easy_opera