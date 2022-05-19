import board
import time
import config
import MicroKeyer
import MorseGenerator
import analogio
import asyncio


async def run():
    # Keyboard PINS
    keyPad0 = MicroKeyer.keyPad0
    keyPad1 = MicroKeyer.keyPad1

    # monotonic all the way
    start = time.monotonic()

    while True:
        await asyncio.sleep(0.01)

        # PTT Hang time ... but the clever way
        if start + config.PTT_HANGTIME < time.monotonic():
            MicroKeyer.pttKey.value = False
            MicroKeyer.pttLed.value = True
            start = time.monotonic()

        pad0 = keyPad0.value
        pad1 = keyPad1.value

        if MicroKeyer.keyA.value is True and MicroKeyer.keyB.value is True:
            if 65000 < pad0 < 65550 and 65000 < pad1 < 65550:
                continue
            if 65000 < pad0 < 65550:
                MicroKeyer.kbdLed.value = False
                print("SW1:", config.SW1)
                MorseGenerator.generate(config.SW1)
                MicroKeyer.kbdLed.value = True
                continue
            if 60000 < pad0 < 65000:
                MicroKeyer.kbdLed.value = False
                print("Morse Keyer:", config.SW2)
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
