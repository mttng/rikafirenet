"""Just an example for testing purpose"""
import sys
import time
from pathlib import Path
import os
import yaml

import requests


from rikafirenet import Stove, OperatingMode

session = requests.session()

def get_yaml_info(file):
    """Get file and load it"""
    with open(file, encoding="utf-8") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            return exc

secret_file = Path(os.path.dirname(__file__) + "/secret.yaml")
secret = get_yaml_info(secret_file)
USERNAME = secret['username']
PASSWORD = secret['password']
STOVE_ID = secret['stove_id']
stove = Stove(session, USERNAME, PASSWORD, STOVE_ID)

if not stove.connect():
    sys.exit(1)
else :
    # while True:
        print("")
        print('Synching state', stove.sync_state())
        print('Target temperatrue', stove.get_stove_thermostat(), '°C')
        print('Consumption', stove.get_stove_consumption(), 'Kg')
        print('Runtime', stove.get_stove_runtime(), 'hours')
        print('Room temperature', stove.get_room_temperature(), '°C')
        print('Burning',stove.is_stove_burning())
        print('Flame temperature', stove.get_stove_flame_temperature(), '°C')
        print('Get Operating mode', stove.get_stove_operating_mode())
        print('Is on?', stove.is_stove_on())
        print('is heating times active for comfort', stove.is_heating_times_active_for_comfort())
        print('State', stove.get_state())
        print('')
        # print("Turning on", stove.turn_on())
        # print("Turning off", stove.turn_off())
        print('Set Operating mode', OperatingMode.MANUAL.value, stove.set_stove_operating_mode(OperatingMode.MANUAL.value))
        print('Set temperatrue', stove.set_stove_thermostat(20))
        stove.send_controls()