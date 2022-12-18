Benchmarking
============

All current and new code contains speed and memory benchmarks written in `Airspeed Velocity <https://asv.readthedocs.io/en/stable/>`_. Currently, there is no site hosting
these benchmarks. However, you can run them locally by using the `docker image <https://hub.docker.com/repository/docker/cabreratoxy/pyopera>`_ the project is built on.
Inside the docker image you can run the following commands to spin up a benchmark server and view the results.

.. code-block:: console

   (.venv) $ poetry asv run
   (.venv) $ poetry run asv publish
   (.venv) $ poetry run asv preview