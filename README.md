# Rika Firenet
## Description
This library dialogs with rika pellet stove.

You need a valid firenet acount and a stove id associated.

Under developpement

## Usage

```python
import requests
from rikafirenet import Stove
session = requests.session()
stove = Stove(session, "username", "password", "stove_id")
if not stove.connect():
    sys.exit(1)
else :
    print('Target temperatrue: ', stove.get_stove_thermostat())
    print('Room temperature: ', stove.get_room_temperature())
    print('Burning: ',stove.is_stove_burning())
```

You can check this [example](example.py)