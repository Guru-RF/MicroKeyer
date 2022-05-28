import board
import time
import config
import MicroKeyer
import MorseGenerator
import analogio
import asyncio
import board
import pwmio
import Morse


async def run():

    word = False
    decodeLetter = False
    checkSpace = False
    toDecode = ""
    start = time.monotonic()

    while True:
        await asyncio.sleep(0.005)

        if decodeLetter is True:
            print(Morse.decode(toDecode))
            toDecode = ""
            decodeLetter = False
            checkSpace = True

        if MicroKeyer.iambicAstate.value is True:
            if word is False:
                print("")
                word = True
            start = time.monotonic()
            toDecode += "-"
            print("-", end="")
            MicroKeyer.iambicAstate.value = False

        if MicroKeyer.iambicBstate.value is True:
            if word is False:
                print("")
                word = True
            start = time.monotonic()
            toDecode += "."
            print(".", end="")
            MicroKeyer.iambicBstate.value = False

        if checkSpace is True and ((start + config.SEVEN_UNITS + config.ONE_UNIT) < time.monotonic()):
            print(" SPACE ")
            checkSpace = False

        if word is True and ((start + config.THREE_UNITS + config.TWO_UNITS) < time.monotonic()):
            print("")
            word = False
            decodeLetter = True

