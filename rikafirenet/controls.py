"""controls"""
from .coordinator import StoveCoordinator

class StoveControls(StoveCoordinator):
    """Class setting stove control"""

    async def turn_on(self):
        """Turn on"""
        await self.sync_state()  # Await the sync_state coroutine
        self._status['controls']['onOff'] = True

        if await self._client.set_stove_controls(self._stove_id, self._status['controls']) is True:
            print("Stove has been turned on")
            await self.sync_state()  # Await the sync_state coroutine after turning on
            return True
        return False

    async def turn_off(self):
        """Turn off"""
        await self.sync_state()  # Await the sync_state coroutine
        self._status['controls']['onOff'] = False

        if await self._client.set_stove_controls(self._stove_id, self._status['controls']) is True:
            print("Stove has been turned off")
            await self.sync_state()  # Await the sync_state coroutine after turning off
            return True
        return False

    async def set_stove_thermostat(self, temperature):
        """Set thermostat"""
        self._status['controls']['targetTemperature'] = str(temperature)
        return True

    async def set_confort_power(self, power):
        """Power when using confort mode"""
        self._status['controls']['RoomPowerRequest'] = power
        return True

    async def set_manual_power(self, percent):
        """Percent power when using manual mode"""
        self._status['controls']['heatingPower'] = percent
        return True

    async def set_stove_operating_mode(self, mode):
        """Operating Mode"""
        self._status['controls']['operatingMode'] = mode
        return True

    async def turn_convection_fan1_on(self):
        """Turn fan1 on"""
        self._status['controls']['convectionFan1Active'] = True

    async def turn_convection_fan1_off(self):
        """Turn fan1 off"""
        self._status['controls']['convectionFan1Active'] = False

    async def turn_convection_fan2_on(self):
        """Turn fan2 on"""
        self._status['controls']['convectionFan2Active'] = True

    async def turn_convection_fan2_off(self):
        """Turn fan2 off"""
        self._status['controls']['convectionFan2Active'] = False
