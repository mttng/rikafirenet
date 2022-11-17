============
Rika Firenet
============


.. image:: https://img.shields.io/pypi/v/rikafirenet.svg
        :target: https://pypi.python.org/pypi/rikafirenet


Python package that dialogs with Rika pellet stove


* Free software: MIT license

Usage
--------

.. code-block:: python

   stove = Stove(username="username", password="password", stove_id="stove_id")
   stove.connect()
   stove.get_room_temperature()
   stove.is_stove_burning()

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
