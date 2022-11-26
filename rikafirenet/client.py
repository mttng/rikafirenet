"""Api with rika pellet stove"""
import time
from datetime import datetime

from bs4 import BeautifulSoup  # parse page
# from .const import Url

urls = {
    "BASE": "https://www.rika-firenet.com",
    "LOGIN": "/web/login",
    "STOVE": "/web/stove/",
    "API": "/api/client/"
}

class FirenetClient():
    """Class representing a stove"""

    def __init__(
        self,
        session,
        username,
        password,
    ):
        self._session = session
        self._username = username
        self._password = password
        self._url_base = urls["BASE"]
        self._url_login = urls["LOGIN"]
        self._url_stove = urls["STOVE"]
        self._url_api = urls["API"]

    def connect(self) :
        """Connect to rika firenet"""
        if self.is_authenticated():
            return True

        data = {
            'email': self._username,
            'password': self._password
        }

        response = self._session.post('https://www.rika-firenet.com/web/login', data)

        if not '/logout' in response.text:
            raise Exception('Failed to connect with Rika Firenet')
        return True

    def is_authenticated(self):
        """Check if already authenticated to rika firenet"""
        if 'connect.sid' not in self._session.cookies:
            return False

        expires_in = list(self._session.cookies)[0].expires
        epoch_now = int(datetime.now().strftime('%S'))

        if expires_in <= epoch_now:
            return False
        return True

    def get_stoves_list(self):
        """Get list of stoves"""
        self.connect()
        stoves = []
        response = self._session.get('https://www.rika-firenet.com/web/summary')

        soup = BeautifulSoup(response.content, "html.parser")
        stove_list = soup.find("ul", {"id": "stoveList"})

        if stove_list is None:
            print("No stove found")
            return stoves

        for stove in stove_list.findAll('li'):
            stove_link = stove.find('a', href=True)
            stove_name = stove_link.attrs['href'].rsplit('/', 1)[-1]
            stoves.append(stove_name)

        return stoves

    def get_stove_status(self, stove_id):
        """Get stove status from api"""
        self.connect()
        print('Getting status')
        url = self._url_base + self._url_api + stove_id + '/status?nocache=' + str(int(time.time()))
        data = self._session.get(url).json()

        return data

    def set_stove_controls(self, stove_id, data):
        """Set stove status from api"""
        response = self._session.post(self._url_base+self._url_api+stove_id+'/controls', data)

        for counter in range (0,10) :
            if 'OK' in response.text :
                print('Controls updated')
                return True
            print(f"In progress..({counter})/10")
            time.sleep(2)
        return False
