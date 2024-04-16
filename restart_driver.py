import time

import uiautomator2 as u2

d = u2.connect('emulator-5554')

d.service('uiautomator').stop()
time.sleep(5)
d.service('uiautomator').start()
time.sleep(10)
