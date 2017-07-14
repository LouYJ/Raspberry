import evdev

ds = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
for device in ds:
    print(device.fn, device.name)
    
dev = evdev.InputDevice('/dev/input/event2')
for event in dev.read_loop():
    if (event.value == 1) :
        if (event.code == 71 or event.code == 72 or event.code == 73):
            print(event.code - 64)
        elif (event.code == 75 or event.code == 76 or event.code == 77):
            print(event.code - 71)
        elif (event.code == 79 or event.code == 80 or event.code == 81):
            print(event.code - 78)
        elif (event.code == 82):
            print(event.code - 82)
        elif (event.code == 96):
            print("Bye")
            break
            