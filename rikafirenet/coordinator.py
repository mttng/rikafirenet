"""Xoordinator"""
from .client import FirenetClient

class StoveCoordinator():
    """Class representing a stove coordination"""
    def __init__(self, session, username, password, stove_id):
        self._session = session
        self._username = username
        self._password = password
        self._stove_id = stove_id
        self._client = FirenetClient(session, username, password)
        self._status = None
        self._controls = None

    def connect(self):
        """Connect to stove"""
        if self._client.connect() is True:
            print('Connected to Rika Firenet')
        else:
            raise Exception('Failed to connect with Rika Firenet')
        stoves = self._client.get_stoves_list()
        if stoves:
            for stove in stoves:
                if stove == self._stove_id:
                    print("Stove id found Stove !")
                    return True
            print("Stove id not found !")
            return False
        print("No stove found !")
        return False

    def sync_state(self):
        """Set thermostat"""
        print("Updating stove id: ", self._stove_id)
        self._status = self._client.get_stove_status(self._stove_id)
        return self._status

    def send_controls(self):
        """Operating Mode"""
        if self._client.set_stove_controls(self._stove_id, self._status['controls']) is True:
            return True
        return False
