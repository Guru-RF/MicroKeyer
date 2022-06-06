import config
import MicroKeyer
import asyncio

async def run():

    while True:
        await asyncio.sleep(0.05)

        # PTT Hang time ... but the clever way
        if (MicroKeyer.pttKey.value is True and MicroKeyer.PTTstate.value is True) and MicroKeyer.PTT.value is False:
            await asyncio.sleep(config.PTT_HANGTIME)
            MicroKeyer.pttLed.value = True
            MicroKeyer.pttKey.value = False
            MicroKeyer.PTTstate.value = False
