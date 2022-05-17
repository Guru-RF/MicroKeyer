import board
import time
import config
import MicroKeyer
import MorseGenerator
import analogio

# We are doing things manually
MicroKeyer.manLed.value = False

# Keyboard PINS
keyPad0 = analogio.AnalogIn(board.GP26)
keyPad1 = analogio.AnalogIn(board.GP27)

# monotonic all the way
start = time.monotonic()

while True:
    # PTT Hang time ... but the clever way
    if start + config.PTT_HANGTIME < time.monotonic():
        MicroKeyer.pttKey.value = False
        MicroKeyer.pttLed.value = True
        start = time.monotonic()

    pad0 = keyPad0.value
    pad1 = keyPad1.value

    if MicroKeyer.keyA.value is False:
        print(".")
        MicroKeyer.pttKey.value = True
        MicroKeyer.pttLed.value = False
        MicroKeyer.keyLed.value = False
        MorseGenerator.dit()
        MicroKeyer.keyLed.value = True
        start = time.monotonic()
        continue

    if MicroKeyer.keyB.value is False:
        print("-")
        MicroKeyer.pttKey.value = True
        MicroKeyer.pttLed.value = False
        MicroKeyer.keyLed.value = False
        MorseGenerator.dah()
        MicroKeyer.keyLed.value = True
        start = time.monotonic()
        continue

    if MicroKeyer.keyA.value is True and MicroKeyer.keyB.value is True:
        if 65000 < pad0 < 65550:
            MicroKeyer.kbdLed.value = False
            print("SW1:", pad0, config.SW1)
            MorseGenerator.generate(config.SW1)
            MicroKeyer.kbdLed.value = True
            continue
        if 60000 < pad0 < 65000:
            MicroKeyer.kbdLed.value = False
            print("SW2:", config.SW2)
            MorseGenerator.generate(config.SW2)
            MicroKeyer.kbdLed.value = True
            continue
        if 50000 < pad0 < 60000:
            MicroKeyer.kbdLed.value = False
            print("SW3:", config.SW3)
            MorseGenerator.generate(config.SW3)
            MicroKeyer.kbdLed.value = True
            continue
        if 40000 < pad0 < 50000:
            MicroKeyer.kbdLed.value = False
            print("SW4:", config.SW4)
            MorseGenerator.generate(config.SW4)
            MicroKeyer.kbdLed.value = True
            continue
        if 65000 < pad1 < 65550:
            MicroKeyer.kbdLed.value = False
            print("SW5:", config.SW5)
            MorseGenerator.generate(config.SW5)
            MicroKeyer.kbdLed.value = True
            continue
        if 60000 < pad1 < 65000:
            MicroKeyer.kbdLed.value = False
            print("SW6:", config.SW6)
            MorseGenerator.generate(config.SW6)
            MicroKeyer.kbdLed.value = True
            continue
        if 50000 < pad1 < 60000:
            MicroKeyer.kbdLed.value = False
            print("SW7:", config.SW7)
            MorseGenerator.generate(config.SW7)
            MicroKeyer.kbdLed.value = True
            continue
        if 40000 < pad1 < 50000:
            MicroKeyer.kbdLed.value = False
            print("SW8:", config.SW8)
            MorseGenerator.generate(config.SW8)
            MicroKeyer.kbdLed.value = True
            continue
