"""Coordinator"""
from .client import FirenetClient

class StoveCoordinator:
    """Class representing a stove coordination"""

    def __init__(self, session, username, password, stove_id):
        self._session = session
        self._username = username
        self._password = password
        self._stove_id = stove_id
        self._client = FirenetClient(session, username, password)
        self._status = None
        self._controls = None

    async def connect(self):
        """Connect to stove"""
        if await self._client.connect():
            print('Connected to Rika Firenet')
        else:
            raise ConnectionError('Failed to connect with Rika Firenet')
        stoves = await self._client.get_stoves_list()  # Await the asynchronous call
        if stoves:
            for stove in stoves:
                if stove == self._stove_id:
                    print("Stove id found Stove !")
                    return True
            print("Stove id not found !")
            return False
        print("No stove found !")
        return False

    async def sync_state(self):
        """Sync stove state"""
        print("Updating stove id: ", self._stove_id)
        self._status = await self._client.get_stove_status(self._stove_id)
        return self._status

    async def send_controls(self):
        """Send controls to the stove"""
        if await self._client.set_stove_controls(self._stove_id, self._status['controls']):
            return True
        return False
