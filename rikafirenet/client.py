"""Api with rika pellet stove"""
import asyncio
from datetime import datetime
import time
from bs4 import BeautifulSoup  # Parse page

urls = {
    "BASE": "https://www.rika-firenet.com",
    "LOGIN": "/web/login",
    "STOVE": "/web/stove/",
    "API": "/api/client/",
}


class FirenetClient:
    """Class representing a stove"""

    def __init__(self, session, username, password):
        self._username = username
        self._password = password
        self._session = session
        self._url_base = urls["BASE"]
        self._url_login = urls["LOGIN"]
        self._url_stove = urls["STOVE"]
        self._url_api = urls["API"]

    async def connect(self):
        """Connect to Rika Firenet"""
        if await self.is_authenticated():
            return True

        data = {'email': self._username, 'password': self._password}

        async with self._session.post(f"{self._url_base}{self._url_login}", data=data) as response:
            response_text = await response.text()
            if '/logout' not in response_text:
                raise ConnectionError("Failed to connect with Rika Firenet")
        return True

    async def is_authenticated(self):
        """Check if already authenticated to Rika Firenet"""
        cookies = self._session.cookie_jar.filter_cookies(self._url_base)

        if 'connect.sid' not in cookies:
            return False

        # Ensure expires_in is an integer (if it's a string, convert it)
        expires_in = cookies.get('connect.sid', {}).get('expires', 0)
        try:
            expires_in = int(expires_in)  # Convert to int if it's a string
        except ValueError:
            expires_in = 0  # If conversion fails, treat it as expired
        # Get the current time in seconds since epoch
        epoch_now = int(datetime.now().timestamp())

        if expires_in <= epoch_now:
            return False
        return True

    async def get_stoves_list(self):
        """Get list of stoves"""
        await self.connect()

        async with self._session.get(f"{self._url_base}/web/summary") as response:
            soup = BeautifulSoup(await response.text(), "html.parser")
            stove_list = soup.find("ul", {"id": "stoveList"})

            if stove_list is None:
                print("No stove found")
                return []

            stoves = [
                stove.find("a", href=True).attrs["href"].rsplit("/", 1)[-1]
                for stove in stove_list.findAll("li")
            ]

        return stoves

    async def get_stove_status(self, stove_id):
        """Get stove status from API"""
        await self.connect()

        url = self._url_base + self._url_api + stove_id + '/status?nocache=' + str(int(time.time()))
        async with self._session.get(url) as response:
            return await response.json()

    async def set_stove_controls(self, stove_id, data):
        """Set stove controls using the API"""
        await self.connect()

        url = f"{self._url_base}{self._url_api}{stove_id}/controls"
        for attempt in range(10):
            async with self._session.post(url, json=data) as response:
                response_text = await response.text()
                if "OK" in response_text:
                    print("Controls updated")
                    return True
                print(f"In progress... ({attempt + 1}/10)")
                await asyncio.sleep(2)
        return False

    async def close(self):
        """Close the session"""
        if self._session:
            await self._session.close()
            self._session = None
