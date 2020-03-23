from time import time, sleep, strftime, gmtime
from pprint import pprint
import pygatt

SERIAL_PORT = '/dev/ttyACM0'
MUSE_MAC = '00:55:DA:B0:B5:B1'

adapter = pygatt.BGAPIBackend(SERIAL_PORT)
adapter.start()
print adapter

devs = adapter.scan()
pprint(devs)

device = adapter.connect(MUSE_MAC)
print device

foo = device.discover_characteristics()
pprint(foo)

# eeg_samples = []
# timestamps = []

# def save_eeg(new_samples, new_timestamps):
#     eeg_samples.append(new_samples)
#     timestamps.append(new_timestamps)

# device.subscribe('273e0001-4c4d-454d-96be-f03bac821358', save_eeg)
# device.char_write_handle(0x000e, [0x02, 0x64, 0x0a], False)
# print 'reading data'
# sleep(3)
# print 'data_ read'
# device.char_write_handle(0x000e, [0x02, 0x68, 0x0a], False)
# device.disconnect()
# adapter.stop()
