import board
import time
import config
import MicroKeyer
import MorseGenerator
import analogio
import asyncio
import board
import pwmio

async def run():

    while True:
        await asyncio.sleep(0.005)

        # PTT Hang time ... but the clever way
        if MicroKeyer.pttKey.value is True and MicroKeyer.PTTstate.value is True:
            print("Hangtime")
            await asyncio.sleep(config.PTT_HANGTIME)
            MicroKeyer.pttLed.value = True
            MicroKeyer.pttKey.value = False
            MicroKeyer.PTTstate.value = False
