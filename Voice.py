import board
import config
import MicroKeyer
import analogio
import audiocore
import audiopwmio
import asyncio
import time


def generate_audio(wavfile):
    if MicroKeyer.pttKey.value is False:
        MicroKeyer.pttKey.value = True
        MicroKeyer.pttLed.value = False
        time.sleep(config.PTT_DELAY)

    radioAudio = audiopwmio.PWMAudioOut(board.GP24)
    MicroKeyer.kbdLed.value = False
    MicroKeyer.audioLed.value = False
    print("Playing ", wavfile)
    data = open(wavfile, "rb")
    wav = audiocore.WaveFile(data)
    radioAudio.play(wav)
    while radioAudio.playing:
        pass
    radioAudio.deinit()
    MicroKeyer.kbdLed.value = True
    MicroKeyer.audioLed.value = True
    MicroKeyer.PTTstate.value = True


async def run():
    keyPad0 = MicroKeyer.keyPad0
    keyPad1 = MicroKeyer.keyPad1

    while True:
        await asyncio.sleep(0.01)

        pad0 = keyPad0.value
        pad1 = keyPad1.value

        if pad0 > 65000:
            generate_audio(config.VSW1)
            continue
        if 60000 < pad0 < 65000:
            generate_audio(config.VSW2)
            continue
        if 50000 < pad0 < 60000:
            generate_audio(config.VSW3)
            continue
        if 40000 < pad0 < 50000:
            generate_audio(config.VSW4)
            continue
        if pad1 > 65000:
            generate_audio(config.VSW5)
            continue
        if 60000 < pad1 < 65000:
            generate_audio(config.VSW6)
            continue
        if 50000 < pad1 < 60000:
            generate_audio(config.VSW7)
            continue
        if 40000 < pad1 < 50000:
            generate_audio(config.VSW8)
            continue
