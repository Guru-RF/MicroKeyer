import board
import time
import config
import MicroKeyer
import MorseGenerator
import analogio
import asyncio
import board
import pwmio

pttState = False

async def run():
    global pttState

    keyPad0 = MicroKeyer.keyPad0
    keyPad1 = MicroKeyer.keyPad1

    while True:
        await asyncio.sleep(0.01)

        pad0 = keyPad0.value
        pad1 = keyPad1.value

        if 65000 < pad0 < 65550 and 65000 < pad1 < 65550:
            print("Toggle", pad0, pad1)
            if pttState is True:
                pttState = False
                print("PTT Off")
            elif pttState is False:
                pttState = True
                print("PTT On")
            await asyncio.sleep(1.5)
