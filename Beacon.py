import time
import config
import MicroKeyer
import MorseGenerator
import asyncio



async def run():
    while True:
        print("Beacon: Generating Morse:", config.BEACON)
        await asyncio.sleep(1)
        MorseGenerator.generate(config.BEACON)
        print("Sleeping for", config.BEACON_SLEEP, "seconds")
        await asyncio.sleep(config.BEACON_SLEEP)
