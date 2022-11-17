"""Main module."""
from .client import FirenetClient


class Stove():
    """Class representing a stove"""
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


    def set_stove_thermostat(self, temperature) :
        """Set thermostat"""
        self.sync_state()
        data = self._status['controls']
        data['targetTemperature'] = str(temperature)

        if self._client.set_stove_controls(self._stove_id, data) is True:
            print(f"Temperature target is now {temperature} °C")
            return True
        return False
                


    def get_stove_consumption(self) :
        """Set thermostat"""
        return self._status['sensors']['parameterFeedRateTotal']

    def get_stove_temperature(self) :
        """Set thermostat"""
        return self._status['sensors']['inputFlameTemperature']

    def get_stove_thermostat(self) :
        """Set thermostat"""
        return self._status['controls']['targetTemperature']

    def get_room_temperature(self) :
        """Set thermostat"""
        return self._status['sensors']['inputRoomTemperature']

    def is_stove_burning(self) :
        """Set thermostat"""
        main_state = self._status['sensors']['statusMainState']
        if main_state == 4 or main_state == 5 :
            return True
        return False
    def sync_state(self):
        """Set thermostat"""
        print("Updating stove id: ", self._stove_id)
        self._status = self._client.get_stove_status(self._stove_id)
        return self._status
