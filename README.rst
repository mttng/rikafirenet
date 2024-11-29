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

    """Exemple of how to communicate with stove"""
    import sys
    from pathlib import Path
    import asyncio
    import os
    import yaml
    import aiohttp
    from rikafirenet import Stove, OperatingMode

    async def get_yaml_info(file):
        """Asynchronously load YAML file"""
        try:
            with open(file, encoding="utf-8") as stream:
                return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            return exc

    async def main():
        """main program"""
        # Set up the session
        async with aiohttp.ClientSession() as session:
            # Load secrets
            secret_file = Path(os.path.dirname(__file__) + "/secret.yaml")
            secret = await get_yaml_info(secret_file)
            username = secret['username']
            password = secret['password']
            stove_id = secret['stove_id']
            # Create Stove instance
            stove = Stove(session, username, password, stove_id)

            # Connect to stove
            if not await stove.connect():
                sys.exit(1)

            print("")
            print('Synching state', await stove.sync_state())
            print('Target temperature', await stove.get_stove_thermostat(), '°C')
            print('Consumption', await stove.get_stove_consumption(), 'Kg')
            print('Consumption before service', await stove.get_consumption_before_service(), 'Kg')
            print('Runtime', await stove.get_stove_runtime(), 'hours')
            print('Room temperature', await stove.get_room_temperature(), '°C')
            print('Burning', await stove.is_stove_burning())
            print('Flame temperature', await stove.get_stove_flame_temperature(), '°C')
            print('Get Operating mode', await stove.get_stove_operating_mode())
            print('Is on?', await stove.is_stove_on())
            print(
                'Is heating times active for comfort', 
                await stove.is_heating_times_active_for_comfort()
            )
            print('State', await stove.get_state())
            print('WiFi signal', await stove.get_wifi_signal())
            print('')
            # Uncomment the following to control the stove
            print("Turning on", await stove.turn_on())
            print("Turning off", await stove.turn_off())
            # print(await stove.set_stove_operating_mode(OperatingMode.MANUAL.value))
            print('Operating mode', OperatingMode.MANUAL.value)
            # print('Set temperature', 20, await stove.set_stove_thermostat(20))
            print('Set manual power', 30, await stove.set_manual_power(30))
            print('Set comfort power', 3, await stove.set_confort_power(3))
            await stove.send_controls()

    # Run the async main function
    if __name__ == "__main__":
        asyncio.run(main())

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
