"""Just an example for testing purpose"""
import sys
import time
from pathlib import Path
import os
import yaml

import requests


from rikafirenet import Stove

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
    stove.sync_state()
    while True:
        print("")
        # print('Set temperatrue', stove.set_stove_thermostat(18))
        print('Target temperatrue', stove.get_stove_thermostat())
        print('Room temperature', stove.get_room_temperature())
        print('Burning',stove.is_stove_burning())
        print("")
        print("Retry in 1/5 ...")
        time.sleep(1)
        print("Retry in 2/5 ...")
        time.sleep(1)
        print("Retry in 3/5 ...")
        time.sleep(1)
        print("Retry in 4/5 ...")
        time.sleep(1)
        print("Retry in 5/5 ...")
        time.sleep(1)
