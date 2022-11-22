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

        import requests
        from rikafirenet import Stove
        session = requests.session()
        stove = Stove(session, "username", "password", "stove_id")
        if not stove.connect():
            sys.exit(1)
        else :
            print('Target temperatrue: ', stove.get_stove_thermostat())
            print('Room temperature: ', stove.get_room_temperature())
            print('Burning: ',stove.is_stove_burning())

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
