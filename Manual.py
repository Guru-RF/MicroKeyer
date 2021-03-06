import config
import MicroKeyer
import MorseGenerator
import asyncio


async def run():
    # Keyboard PINS
    keyPad0 = MicroKeyer.keyPad0
    keyPad1 = MicroKeyer.keyPad1

    while True:
        await asyncio.sleep(0.05)

        pad0 = keyPad0.value
        pad1 = keyPad1.value

        if MicroKeyer.keyDAH.value is True and MicroKeyer.keyDIT.value is True:
            if 48000 < pad0 < 65555 and 48000 < pad1 < 65555:
                await asyncio.sleep(0.05)
                continue
            if 65000 < pad0 < 65555:
                MicroKeyer.kbdLed.value = False
                print("SW1:", config.SW1, pad0)
                MorseGenerator.generate(config.SW1)
                MicroKeyer.kbdLed.value = True
                continue
            if 55000 < pad0 < 65000:
                MicroKeyer.kbdLed.value = False
                print("SW2:", config.SW2, pad0)
                MorseGenerator.generate(config.SW2)
                MicroKeyer.kbdLed.value = True
                continue
            if 45000 < pad0 < 55000:
                MicroKeyer.kbdLed.value = False
                print("SW3:", config.SW3, pad0)
                MorseGenerator.generate(config.SW3)
                MicroKeyer.kbdLed.value = True
                continue
            if 30000 < pad0 < 40000:
                MicroKeyer.kbdLed.value = False
                print("SW4:", config.SW4, pad0)
                MorseGenerator.generate(config.SW4)
                MicroKeyer.kbdLed.value = True
                continue
            if 65000 < pad1 < 65555:
                MicroKeyer.kbdLed.value = False
                print("SW5:", config.SW5, pad1)
                MorseGenerator.generate(config.SW5)
                MicroKeyer.kbdLed.value = True
                continue
            if 55000 < pad1 < 65000:
                MicroKeyer.kbdLed.value = False
                print("SW6:", config.SW6, pad1)
                MorseGenerator.generate(config.SW6)
                MicroKeyer.kbdLed.value = True
                continue
            if 45000 < pad1 < 55000:
                MicroKeyer.kbdLed.value = False
                print("SW7:", config.SW7, pad1)
                MorseGenerator.generate(config.SW7)
                MicroKeyer.kbdLed.value = True
                continue
            if 30000 < pad1 < 40000:
                MicroKeyer.kbdLed.value = False
                print("SW8:", config.SW8, pad1)
                MorseGenerator.generate(config.SW8)
                MicroKeyer.kbdLed.value = True
                continue
