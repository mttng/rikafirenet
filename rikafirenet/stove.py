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
        self._status['controls']['targetTemperature'] = str(temperature)

        # if self._client.set_stove_controls(self._stove_id, self._status['controls']) is True:
        #     print(f"Temperature target is now {temperature} °C")
        #     return True
        return True

    def get_stove_consumption(self) :
        """Set thermostat"""
        return self._status['sensors']['parameterFeedRateTotal']

    def get_stove_runtime(self):
        """Runtime"""
        return self._status['sensors']['parameterRuntimePellets']

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
        if main_state in (4, 5):
            return True
        return False

    def get_stove_flame_temperature(self):
        """Input flame"""
        return float(self._status['sensors']['inputFlameTemperature'])

    def get_stove_operating_mode(self):
        """Operating Mode"""
        return float(self._status['controls']['operatingMode'])

    def set_stove_operating_mode(self, mode):
        """Operating Mode"""
        # self.sync_state()
        self._status['controls']['operatingMode'] = mode

        # if self._client.set_stove_controls(self._stove_id, self._status['controls']) is True:
        #     print(f"New operating mode {mode} selected")
        #     # self.sync_state()
        #     return True
        return True

    def send_controls(self):
        """Operating Mode"""
        # self.sync_state() # Synchronize data first

        if self._client.set_stove_controls(self._stove_id, self._status['controls']) is True:
            return True
        return False

    def is_heating_times_active_for_comfort(self):
        """Heating time for confort"""
        return self._status['controls']['heatingTimesActiveForComfort']

    def is_stove_on(self):
        """Is stove on"""
        return bool(self._status['controls']['onOff'])

    def sync_state(self):
        """Set thermostat"""
        print("Updating stove id: ", self._stove_id)
        self._status = self._client.get_stove_status(self._stove_id)
        return self._status

    def turn_on(self):
        """turn on"""
        self.sync_state()
        self._status['controls']['onOff'] = True

        if self._client.set_stove_controls(self._stove_id, self._status['controls']) is True:
            print("Stove has been turned on")
            self.sync_state()
            return True
        return False

    def turn_off(self):
        """turn off"""
        self.sync_state()
        self._status['controls']['onOff'] = False

        if self._client.set_stove_controls(self._stove_id, self._status['controls']) is True:
            print("Stove has been turned off")
            self.sync_state()
            return True
        return False

    def get_state(self):
        """get statee"""
        main_state = self._status['sensors']['statusMainState']
        sub_state = self._status['sensors']['statusSubState']
        frost_started = self._status['sensors']['statusFrostStarted']
        result = ["/images/status/Visu_Off.svg", "unknown"]

        if frost_started:
            result = ["/images/status/Visu_Freeze.svg", "frost_protection"]
        result = _MAIN_STATE.get(main_state)
        if main_state == 1:
            if sub_state == 0:
                result = ["/images/status/Visu_Off.svg", "stove_off"]
            elif sub_state in (1, 3):
                result = ["/images/status/Visu_Standby.svg", "standby"]
            elif sub_state == 2:
                result = ["/images/status/Visu_Standby.svg", "external_request"]
        # elif main_state == 2:
        #     result = ["/images/status/Visu_Ignition.svg", "ignition_on"]
        # elif main_state == 3:
        #     result = ["/images/status/Visu_Ignition.svg", "starting_up"]
        # elif main_state == 4:
        #     result = ["/images/status/Visu_Control.svg", "running"]
        elif main_state == 5:
            if sub_state in (3,4):
                result = ["/images/status/Visu_Clean.svg", "big_clean"]
            else:
                result = ["/images/status/Visu_Clean.svg", "clean"]
        return result

_MAIN_STATE = {
    1: [],
    2: ["/images/status/Visu_Ignition.svg", "ignition_on"],
    3: ["/images/status/Visu_Ignition.svg", "starting_up"],
    4: ["/images/status/Visu_Control.svg", "running"],
    5: [],
    6: ["/images/status/Visu_BurnOff.svg", "burn_off"],
    11: ["/images/status/Visu_SpliLog.svg", "split_log_check"],
    13: ["/images/status/Visu_SpliLog.svg", "split_log_check"],
    14: ["/images/status/Visu_SpliLog.svg", "split_log_check"],
    16: ["/images/status/Visu_SpliLog.svg", "split_log_check"],
    17: ["/images/status/Visu_SpliLog.svg", "split_log_check"],
    20: ["/images/status/Visu_SpliLog.svg", "split_log_mode"],
    21: ["/images/status/Visu_SpliLog.svg", "split_log_mode"],
    50: ["/images/status/Visu_SpliLog.svg", "split_log_check"]
}
