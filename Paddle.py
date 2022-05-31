import board
import time
import config
import MicroKeyer
import MorseGenerator
import analogio
import asyncio
import board
import pwmio

keyDIT = False
keyDAH = False
firstDIT = False
firstDAH = False
toneDIT = False
toneDAH = False


async def PaddleKeyDah():
    global keyDIT
    global keyDAH
    global firstDIT
    global firstDAH
    global toneDIT
    global toneDAH
    global ditdah
    global dahdit
    while True:
        await asyncio.sleep(0.0001)

        if MicroKeyer.keyDIT.value is False:
            keyDIT = True
            if not (dahdit is True or ditdah is True):
                if keyDAH is True:
                    firstDAH = True
                    firstDIT = False
            if toneDAH is True:
                await asyncio.sleep(config.THREE_UNITS)
        else:
            keyDIT = False


async def PaddleKeyDit():
    global keyDIT
    global keyDAH
    global firstDIT
    global firstDAH
    global toneDIT
    global toneDAH
    global ditdah
    global dahdit
    while True:
        await asyncio.sleep(0.001)

        if MicroKeyer.keyDAH.value is False:
            keyDAH = True
            if not (dahdit is True or ditdah is True):
                if keyDIT is True:
                    firstDIT = True
                    firstDAH = False
            if toneDIT is True:
                await asyncio.sleep(config.THREE_UNITS)
        else:
            keyDAH = False



async def keyer():
    global keyDIT
    global keyDAH
    global firstDIT
    global firstDAH
    global toneDIT
    global toneDAH
    global ditdah
    global dahdit

    ditdah = False
    dahdit = False

    # monotonic all the way
    start = time.monotonic()

    while True:
        await asyncio.sleep(0.0001)

        #print("ditdah", ditdah, "dahdit", dahdit, "keyDIT", keyDIT, "keyDAH", keyDAH, "firstDIT", firstDIT, "firstDAH", firstDAH )

        if start + config.PTT_HANGTIME < time.monotonic():
            MicroKeyer.PTTstate.value = True
            start = time.monotonic()

#        # reset ditdah or dahdit
#        if keyDIT is False or keyDAH is False:
#            if keyDAH is True:
#                firstDIT = False
#                firstDAH = True
#            if keyDIT is True:
#                firstDIT = True
#                firstDAH = False
#            ditdah = False
#            dahdit = False

        # reset all
        if keyDIT is False and keyDAH is False:
            ditdah = False
            dahdit = False
            firstDIT = False
            firstDAH = False

#        # ditdah
#        if (keyDIT is True and keyDAH is True and firstDAH is True) or ditdah is True:
#            toneDIT = False
#            toneDAH = False
#            firstDIT = False
#            firstDAH = False
#            ditdah = True
#            dahdit = False
#
#            print("-B.A")
#            if MicroKeyer.pttKey.value is False:
#                MicroKeyer.pttKey.value = True
#                MicroKeyer.pttLed.value = False
#            #                await asyncio.sleep(config.PTT_DELAY)
#            MicroKeyer.keyLed.value = False
#            MicroKeyer.cwLed.value = False
#            MicroKeyer.cwKey.value = True
#            speaker = pwmio.PWMOut(board.GP25, frequency=config.CW_TONE)
#            output = pwmio.PWMOut(board.GP24, frequency=config.CW_TONE)
#            MicroKeyer.iambicAstate.value = True
#            MorseGenerator.play_tone(speaker, output)
#            await asyncio.sleep(config.THREE_UNITS)
#            MorseGenerator.be_quiet(speaker, output)
#            output.deinit()
#            speaker.deinit()
#            # await asyncio.sleep(config.TWO_UNITS)
#            MicroKeyer.keyLed.value = True
#            MicroKeyer.cwLed.value = True
#            MicroKeyer.cwKey.value = False
#
#            if MicroKeyer.keyDIT.value is False:
#                print("-B.A L")
#                await asyncio.sleep(config.ONE_UNIT)
#                MicroKeyer.keyLed.value = False
#                MicroKeyer.cwLed.value = False
#                MicroKeyer.cwKey.value = True
#                speaker = pwmio.PWMOut(board.GP25, frequency=config.CW_TONE)
#                output = pwmio.PWMOut(board.GP24, frequency=config.CW_TONE)
#                MicroKeyer.iambicBstate.value = True
#                MorseGenerator.play_tone(speaker, output)
#                await asyncio.sleep(config.ONE_UNIT)
#                MorseGenerator.be_quiet(speaker, output)
#                output.deinit()
#                speaker.deinit()
#                await asyncio.sleep(config.ONE_UNIT)
#                MicroKeyer.keyLed.value = True
#                MicroKeyer.cwLed.value = True
#                MicroKeyer.cwKey.value = False
#
#            start = time.monotonic()
#            continue
#
#        # dahdit
#        if (keyDIT is True and keyDAH is True and firstDIT is True) or dahdit is True:
#            toneDIT = False
#            toneDAH = False
#            firstDIT = False
#            firstDAH = False
#            ditdah = False
#            dahdit = True
#
#            print(".A-B")
#
#            if MicroKeyer.pttKey.value is False:
#                MicroKeyer.pttKey.value = True
#                MicroKeyer.pttLed.value = False
#            #                await asyncio.sleep(config.PTT_DELAY)
#            MicroKeyer.keyLed.value = False
#            MicroKeyer.cwLed.value = False
#            MicroKeyer.audioLed.value = False
#            MicroKeyer.cwKey.value = True
#            speaker = pwmio.PWMOut(board.GP25, frequency=config.CW_TONE)
#            output = pwmio.PWMOut(board.GP24, frequency=config.CW_TONE)
#            MicroKeyer.iambicBstate.value = True
#            MorseGenerator.play_tone(speaker, output)
#            await asyncio.sleep(config.ONE_UNIT)
#            MorseGenerator.be_quiet(speaker, output)
#            output.deinit()
#            speaker.deinit()
#            MicroKeyer.keyLed.value = True
#            MicroKeyer.cwLed.value = True
#            MicroKeyer.audioLed.value = True
#            MicroKeyer.cwKey.value = False
#            await asyncio.sleep(config.ONE_UNIT)
#
#            if MicroKeyer.keyDAH.value is False:
#                print(".A-B L")
#                MicroKeyer.keyLed.value = False
#                MicroKeyer.cwLed.value = False
#                MicroKeyer.audioLed.value = False
#                MicroKeyer.cwKey.value = True
#                speaker = pwmio.PWMOut(board.GP25, frequency=config.CW_TONE)
#                output = pwmio.PWMOut(board.GP24, frequency=config.CW_TONE)
#                MicroKeyer.iambicAstate.value = True
#                MorseGenerator.play_tone(speaker, output)
#                await asyncio.sleep(config.THREE_UNITS)
#                MorseGenerator.be_quiet(speaker, output)
#                output.deinit()
#                speaker.deinit()
#                await asyncio.sleep(config.ONE_UNIT)
#                MicroKeyer.keyLed.value = True
#                MicroKeyer.cwLed.value = True
#                MicroKeyer.audioLed.value = True
#                MicroKeyer.cwKey.value = False
#
#            start = time.monotonic()
#            continue

        # dit
        if keyDIT is True or firstDIT is True:
            if firstDIT is True:
                keyDIT = False
                firstDIT = False
            print(".A")
            toneDIT = True
            if MicroKeyer.pttKey.value is False:
                MicroKeyer.pttKey.value = True
                MicroKeyer.pttLed.value = False
            #                await asyncio.sleep(config.PTT_DELAY)
            MicroKeyer.keyLed.value = False
            MicroKeyer.cwLed.value = False
            MicroKeyer.audioLed.value = False
            MicroKeyer.cwKey.value = True
            speaker = pwmio.PWMOut(board.GP25, frequency=config.CW_TONE)
            output = pwmio.PWMOut(board.GP24, frequency=config.CW_TONE)
            MicroKeyer.iambicBstate.value = True
            MorseGenerator.play_tone(speaker, output)
            await asyncio.sleep(config.ONE_UNIT)
            MorseGenerator.be_quiet(speaker, output)
            output.deinit()
            speaker.deinit()
            await asyncio.sleep(config.ONE_UNIT)
            MicroKeyer.keyLed.value = True
            MicroKeyer.cwLed.value = True
            MicroKeyer.audioLed.value = True
            MicroKeyer.cwKey.value = False
            toneDIT = False

            start = time.monotonic()
            #continue

        # dah
        if keyDAH is True or firstDAH is True:
            if firstDAH is True:
                keyDAH = False
                firstDAH = False
            print("-B")
            toneDAH = True
            if MicroKeyer.pttKey.value is False:
                MicroKeyer.pttKey.value = True
                MicroKeyer.pttLed.value = False
            #                await asyncio.sleep(config.PTT_DELAY)
            MicroKeyer.keyLed.value = False
            MicroKeyer.cwLed.value = False
            MicroKeyer.audioLed.value = False
            MicroKeyer.cwKey.value = True
            speaker = pwmio.PWMOut(board.GP25, frequency=config.CW_TONE)
            output = pwmio.PWMOut(board.GP24, frequency=config.CW_TONE)
            MicroKeyer.iambicAstate.value = True
            MorseGenerator.play_tone(speaker, output)
            await asyncio.sleep(config.THREE_UNITS)
            MorseGenerator.be_quiet(speaker, output)
            output.deinit()
            speaker.deinit()
            await asyncio.sleep(config.ONE_UNIT)
            MicroKeyer.keyLed.value = True
            MicroKeyer.cwLed.value = True
            MicroKeyer.audioLed.value = True
            MicroKeyer.cwKey.value = False
            toneDAH = False

            start = time.monotonic()
            #continue
