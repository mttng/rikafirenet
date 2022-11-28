"""controls"""
from .coordinator import StoveCoordinator

class StoveControls(StoveCoordinator):
    """Class setting stove control"""

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

    def set_stove_thermostat(self, temperature) :
        """Set thermostat"""
        self._status['controls']['targetTemperature'] = str(temperature)
        return True

    def set_confort_power(self, power):
        """Power when using confort mode """
        self._status['controls']['RoomPowerRequest'] = power
        return True

    def set_manual_power(self, percent):
        """Percent power when using manual mode """
        self._status['controls']['heatingPower'] = percent
        return True

    def set_stove_operating_mode(self, mode):
        """Operating Mode"""
        self._status['controls']['operatingMode'] = mode
        return True

    def turn_convection_fan1_on(self):
        """Turn fan1 on"""
        self._status['controls']['convectionFan1Active'] = True

    def turn_convection_fan1_off(self):
        """Turn fan1 off"""
        self._status['controls']['convectionFan1Active'] = False

    def turn_convection_fan2_on(self):
        """Turn fan2 on"""
        self._status['controls']['convectionFan1Active'] = True

    def turn_convection_fan2_off(self):
        """Turn fan2 off"""
        self._status['controls']['convectionFan1Active'] = False
