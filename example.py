import sys
from pathlib import Path
import os
import yaml
import aiohttp
import asyncio
from rikafirenet import Stove, OperatingMode

async def get_yaml_info(file):
    """Asynchronously load YAML file"""
    try:
        with open(file, encoding="utf-8") as stream:
            return yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        return exc

async def main():
    # Set up the session
    async with aiohttp.ClientSession() as session:
        # Load secrets
        secret_file = Path(os.path.dirname(__file__) + "/secret-example.yaml")
        secret = await get_yaml_info(secret_file)
        USERNAME = secret['username']
        PASSWORD = secret['password']
        STOVE_ID = secret['stove_id']
        
        # Create Stove instance
        stove = Stove(session, USERNAME, PASSWORD, STOVE_ID)

        # Connect to stove
        if not await stove.connect():
            sys.exit(1)

        print("")
        print('Synching state', await stove.sync_state())  # Awaiting async sync_state method
        print('Target temperature', await stove.get_stove_thermostat(), '°C')  # Awaiting async method
        print('Consumption', await stove.get_stove_consumption(), 'Kg')  # Awaiting async method
        print('Consumption before service', await stove.get_consumption_before_service(), 'Kg')  # Awaiting async method
        print('Runtime', await stove.get_stove_runtime(), 'hours')  # Awaiting async method
        print('Room temperature', await stove.get_room_temperature(), '°C')  # Awaiting async method
        print('Burning', await stove.is_stove_burning())  # Awaiting async method
        print('Flame temperature', await stove.get_stove_flame_temperature(), '°C')  # Awaiting async method
        print('Get Operating mode', await stove.get_stove_operating_mode())  # Awaiting async method
        print('Is on?', await stove.is_stove_on())  # Awaiting async method
        print('Is heating times active for comfort', await stove.is_heating_times_active_for_comfort())  # Awaiting async method
        print('State', await stove.get_state())  # Awaiting async method
        print('WiFi signal', await stove.get_wifi_signal())  # Awaiting async method
        print('')
        
        # Uncomment the following to control the stove
        print("Turning on", await stove.turn_on())  # Awaiting async method
        print("Turning off", await stove.turn_off())  # Awaiting async method
        # print(await stove.set_stove_operating_mode(OperatingMode.MANUAL.value))  # Awaiting async method
        print('Operating mode', OperatingMode.MANUAL.value)
        # print('Set temperature', 20, await stove.set_stove_thermostat(20))  # Awaiting async method
        print('Set manual power', 30, await stove.set_manual_power(30))  # Awaiting async method
        print('Set comfort power', 3, await stove.set_confort_power(3))  # Awaiting async method
        await stove.send_controls()  # Awaiting async method

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())
