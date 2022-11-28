"""sensors"""
from .coordinator import StoveCoordinator

class StoveSensors(StoveCoordinator):
    """Class getting sensors of stove"""

    def get_state(self):
        """get state"""
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
        elif main_state == 5:
            if sub_state in (3,4):
                result = ["/images/status/Visu_Clean.svg", "big_clean"]
            else:
                result = ["/images/status/Visu_Clean.svg", "clean"]
        return result
    def get_stove_consumption(self) :
        """Get stove consumption in kg"""
        return self._status['sensors']['parameterFeedRateTotal']

    def get_stove_runtime(self):
        """Runtime"""
        return self._status['sensors']['parameterRuntimePellets']

    def get_stove_thermostat(self) :
        """Get thermostat"""
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

    def get_consumption_before_service(self):
        """Pellet consumption before sevice in kg"""
        return float(self._status['sensors']['parameterFeedRateService'])

    def get_wifi_signal(self):
        """Wifi signal"""
        return float(self._status['sensors']['statusWifiStrength'])

    def is_heating_times_active_for_comfort(self):
        """Heating time for confort"""
        return self._status['controls']['heatingTimesActiveForComfort']

    def is_stove_on(self):
        """Is stove on"""
        return bool(self._status['controls']['onOff'])

    def get_stove_set_back_temperature(self):
        """Back temperature"""
        return float(self._status['controls']['setBackTemperature'])

    def is_stove_convection_fan1_on(self):
        """Convection fan1 state"""
        return bool(self._status['controls']['convectionFan1Active'])

    def is_stove_convection_fan2_on(self):
        """Convection fan2 state"""
        return bool(self._status['controls']['convectionFan2Active'])

    def get_convection_fan1_level(self):
        """Convection fan1 level"""
        return int(self._status['controls']['convectionFan1Level'])

    def get_convection_fan1_area(self):
        """Convection fan1 area"""
        return int(self._status['controls']['convectionFan1Area'])

    def get_convection_fan2_level(self):
        """Convection fan2 level"""
        return int(self._status['controls']['convectionFan2Level'])

    def get_convection_fan2_area(self):
        """Convection fan2 area"""
        return int(self._status['controls']['convectionFan2Area'])

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
