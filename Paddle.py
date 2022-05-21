import board
import time
import config
import MicroKeyer
import MorseGenerator
import analogio
import asyncio
import board
import pwmio

keyA = False
keyB = False
firstA = False
firstB = False
toneA = False
toneB = False

async def keyA():
    global keyA
    global keyB
    global firstA
    global firstB
    global toneA
    global toneB
    global ditdah
    global dahdit
    while True:
        await asyncio.sleep(0.01)
        if MicroKeyer.keyA.value is False:
            keyA = True
            if not (dahdit is True or ditdah is True):
                if keyB is True:
                    firstB = True
                    firstA = False
            if toneB is True:
                await asyncio.sleep(config.THREE_UNITS)
        else:
            keyA = False


async def keyB():
    global keyA
    global keyB
    global firstA
    global firstB
    global toneA
    global toneB
    global ditdah
    global dahdit
    while True:
        await asyncio.sleep(0.01)
        if MicroKeyer.keyB.value is False:
            keyB = True
            if not (dahdit is True or ditdah is True):
                if keyA is True:
                    firstA = True
                    firstB = False
            if toneA is True:
                await asyncio.sleep(config.TWO_UNITS)
        else:
            keyB = False

async def keyer():
    global keyA
    global keyB
    global firstA
    global firstB
    global toneA
    global toneB
    global ditdah
    global dahdit

    ditdah = False
    dahdit = False

    # monotonic all the way
    start = time.monotonic()

    while True:
        await asyncio.sleep(0.005)

        if start + config.PTT_HANGTIME < time.monotonic():
            MicroKeyer.PTTstate.value = True
            start = time.monotonic()

        # reset ditdah or dahdit
        if keyA is False or keyB is False:
            ditdah = False
            dahdit = False
            firstA = False
            firstB = False

        # reset all
        if keyA is False and keyB is False:
            ditdah = False
            dahdit = False
            firstA = False
            firstB = False

        # ditdah
        if (keyA is True and keyB is True and firstB is True) or ditdah is True:
            toneA = False
            toneB = False
            firstA = False
            firstB = False
            ditdah = True
            dahdit = False

            print(".A-B")
            if MicroKeyer.pttKey.value is False:
                MicroKeyer.pttKey.value = True
                MicroKeyer.pttLed.value = False
                await asyncio.sleep(config.PTT_DELAY)
            MicroKeyer.keyLed.value = False
            MicroKeyer.cwLed.value = False
            MicroKeyer.cwKey.value = True
            speaker = pwmio.PWMOut(board.GP25, frequency=config.CW_TONE)
            output = pwmio.PWMOut(board.GP24, frequency=config.CW_TONE)
            MorseGenerator.play_tone(speaker, output)
            await asyncio.sleep(config.ONE_UNIT)
            MorseGenerator.be_quiet(speaker, output)
            output.deinit()
            speaker.deinit()
            await asyncio.sleep(config.TWO_UNITS)
            MicroKeyer.keyLed.value = True
            MicroKeyer.cwLed.value = True
            MicroKeyer.cwKey.value = False

            MicroKeyer.keyLed.value = False
            MicroKeyer.cwLed.value = False
            MicroKeyer.cwKey.value = True
            speaker = pwmio.PWMOut(board.GP25, frequency=config.CW_TONE)
            output = pwmio.PWMOut(board.GP24, frequency=config.CW_TONE)
            MorseGenerator.play_tone(speaker, output)
            await asyncio.sleep(config.THREE_UNITS)
            MorseGenerator.be_quiet(speaker, output)
            output.deinit()
            speaker.deinit()
            await asyncio.sleep(config.ONE_UNIT)
            MicroKeyer.keyLed.value = True
            MicroKeyer.cwLed.value = True
            MicroKeyer.cwKey.value = False

            start = time.monotonic()
            continue

        #dahdit
        if (keyA is True and keyB is True and firstA is True) or dahdit is True:
            toneA = False
            toneB = False
            firstA = False
            firstB = False
            ditdah = False
            dahdit = True

            print("-B.A")

            if MicroKeyer.pttKey.value is False:
                MicroKeyer.pttKey.value = True
                MicroKeyer.pttLed.value = False
                await asyncio.sleep(config.PTT_DELAY)
            MicroKeyer.keyLed.value = False
            MicroKeyer.cwLed.value = False
            MicroKeyer.audioLed.value = False
            MicroKeyer.cwKey.value = True
            speaker = pwmio.PWMOut(board.GP25, frequency=config.CW_TONE)
            output = pwmio.PWMOut(board.GP24, frequency=config.CW_TONE)
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

            MicroKeyer.keyLed.value = False
            MicroKeyer.cwLed.value = False
            MicroKeyer.audioLed.value = False
            MicroKeyer.cwKey.value = True
            speaker = pwmio.PWMOut(board.GP25, frequency=config.CW_TONE)
            output = pwmio.PWMOut(board.GP24, frequency=config.CW_TONE)
            MorseGenerator.play_tone(speaker, output)
            await asyncio.sleep(config.ONE_UNIT)
            MorseGenerator.be_quiet(speaker, output)
            output.deinit()
            speaker.deinit()
            await asyncio.sleep(config.TWO_UNITS)
            MicroKeyer.keyLed.value = True
            MicroKeyer.cwLed.value = True
            MicroKeyer.audioLed.value = True
            MicroKeyer.cwKey.value = False

            start = time.monotonic()
            continue

        # dit
        if keyA is True:
            print(".A")
            toneA = True
            if MicroKeyer.pttKey.value is False:
                MicroKeyer.pttKey.value = True
                MicroKeyer.pttLed.value = False
                await asyncio.sleep(config.PTT_DELAY)
            MicroKeyer.keyLed.value = False
            MicroKeyer.cwLed.value = False
            MicroKeyer.audioLed.value = False
            MicroKeyer.cwKey.value = True
            speaker = pwmio.PWMOut(board.GP25, frequency=config.CW_TONE)
            output = pwmio.PWMOut(board.GP24, frequency=config.CW_TONE)
            MorseGenerator.play_tone(speaker, output)
            await asyncio.sleep(config.ONE_UNIT)
            MorseGenerator.be_quiet(speaker, output)
            output.deinit()
            speaker.deinit()
            await asyncio.sleep(config.TWO_UNITS)
            MicroKeyer.keyLed.value = True
            MicroKeyer.cwLed.value = True
            MicroKeyer.audioLed.value = True
            MicroKeyer.cwKey.value = False
            toneA = False

            start = time.monotonic()
            continue

        # dah
        if keyB is True:
            print("-B")
            toneB = True
            if MicroKeyer.pttKey.value is False:
                MicroKeyer.pttKey.value = True
                MicroKeyer.pttLed.value = False
                await asyncio.sleep(config.PTT_DELAY)
            MicroKeyer.keyLed.value = False
            MicroKeyer.cwLed.value = False
            MicroKeyer.audioLed.value = False
            MicroKeyer.cwKey.value = True
            speaker = pwmio.PWMOut(board.GP25, frequency=config.CW_TONE)
            output = pwmio.PWMOut(board.GP24, frequency=config.CW_TONE)
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
            toneB = False

            start = time.monotonic()
            continue

