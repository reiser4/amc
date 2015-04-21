from evdev import InputDevice, list_devices, categorize, ecodes
from select import select

'''
devices = [InputDevice(fn) for fn in list_devices()]

for dev in devices:
    print(dev.fn, dev.name, dev.phys)
'''

devices = map(InputDevice, ('/dev/input/event2', '/dev/input/event14'))
devices = {dev.fd : dev for dev in devices}

for dev in devices.values():
    print(dev)

while True:
    r,w,x = select(devices, [], [])
    for fd in r:
        for event in devices[fd].read():
            if event.type == ecodes.EV_KEY and event.value == 0:
                print(str(devices[fd].phys) + "\t->\t" + str(categorize(event)))
