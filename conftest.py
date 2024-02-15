import pytest
import uiautomator2 as u2
from config import *


@pytest.fixture
def device():
    device_id = 'emulator-5554'
    # device_id = 'TSBM9L55QWWG4LIR'
    d = u2.connect(device_id)
    d.app_clear(package)
    d.app_start(package,stop=True)
    return d



