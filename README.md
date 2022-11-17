# Rika Firenet
## Description
This library dialogs with rika pellet stove.

You need a valid firenet acount and a stove id associated.

Under developpement

## Usage

```python
from rikafirenet import Stove
stove = Stove(username="username", password="password", stove_id="stove_id")
stove.connect()
stove.get_room_temperature()
stove.is_stove_burning()
```

You can check this [example](test.py)