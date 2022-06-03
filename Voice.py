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

        if 65000 < pad0 < 65555:
            generate_audio(config.VSW1)
            continue
        if 55000 < pad0 < 65000:
            generate_audio(config.VSW2)
            continue
        if 45000 < pad0 < 55000:
            generate_audio(config.VSW3)
            continue
        if 30000 < pad0 < 40000:
            generate_audio(config.VSW4)
            continue
        if 65000 < pad1 < 65555:
            generate_audio(config.VSW5)
            continue
        if 55000 < pad1 < 65000:
            generate_audio(config.VSW6)
            continue
        if 45000 < pad1 < 55000:
            generate_audio(config.VSW7)
            continue
        if 30000 < pad1 < 40000:
            generate_audio(config.VSW8)
            continue
