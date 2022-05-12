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
        start = time.monotonic()

    pad0 = keyPad0.value
    pad1 = keyPad1.value

    if MicroKeyer.keyA.value is True:
        print(".")
        MicroKeyer.pttKey.value = True
        MorseGenerator.dit()
        continue

    if config.KBD is False:
        if pad0 > 55000:
            print(".")
            MicroKeyer.pttKey.value = True
            MorseGenerator.dit()
            start = time.monotonic()
            continue
        if pad1 > 55000:
            print("-")
            MicroKeyer.pttKey.value = True
            MorseGenerator.dah()
            start = time.monotonic()
            continue
    else:
        if 65000 < pad0 < 65550:
            print("SW1:", pad0, config.SW1)
            MorseGenerator.generate(config.SW1)
            continue
        if 60000 < pad0 < 65000:
            print("SW2:", config.SW2)
            MorseGenerator.generate(config.SW2)
            continue
        if 50000 < pad0 < 60000:
            print("SW3:", config.SW3)
            MorseGenerator.generate(config.SW3)
            continue
        if 40000 < pad0 < 50000:
            print("SW4:", config.SW4)
            MorseGenerator.generate(config.SW4)
            continue
        if 65000 < pad1 < 65550:
            print("SW5:", config.SW5)
            MorseGenerator.generate(config.SW5)
            continue
        if 60000 < pad1 < 65000:
            print("SW6:", config.SW6)
            MorseGenerator.generate(config.SW6)
            continue
        if 50000 < pad1 < 60000:
            print("SW7:", config.SW7)
            MorseGenerator.generate(config.SW7)
            continue
        if 40000 < pad1 < 50000:
            print("SW8:", config.SW8)
            MorseGenerator.generate(config.SW8)
            continue
