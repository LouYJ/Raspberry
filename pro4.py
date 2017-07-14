from espeak import espeak

espeak.synth("Hello")

import evdev

ds = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
    
dev = evdev.InputDevice('/dev/input/event2')
for event in dev.read_loop():
    if (event.value == 1) :
        if (event.code == 71 or event.code == 72 or event.code == 73):
            espeak.synth(str(event.code - 64))
        elif (event.code == 75 or event.code == 76 or event.code == 77):
            espeak.synth(str(event.code - 71))
        elif (event.code == 79 or event.code == 80 or event.code == 81):
            espeak.synth(str(event.code - 78))
        elif (event.code == 82):
            espeak.synth(str(event.code - 82))
        elif (event.code == 96):
            espeak.synth("Goodbye")
            break
            