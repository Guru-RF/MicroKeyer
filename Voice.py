import board
import config
import MicroKeyer
import analogio
import audiocore
import audiopwmio
import asyncio
import time


def generate_audio(wavfile):
    radioAudio = audiopwmio.PWMAudioOut(board.GP24)
    MicroKeyer.pttKey.value = True
    print("Playing ", wavfile)
    data = open(wavfile, "rb")
    wav = audiocore.WaveFile(data)
    radioAudio.play(wav)
    while radioAudio.playing:
        pass
    radioAudio.deinit()
    MicroKeyer.pttKey.value = False


async def run():
    keyPad0 = MicroKeyer.keyPad0
    keyPad1 = MicroKeyer.keyPad1

    while True:
        await asyncio.sleep(0.01)
        pad0 = keyPad0.value
        pad1 = keyPad1.value
        if pad0 > 65000:
            generate_audio(config.VSW1)
        if 60000 < pad0 < 65000:
            generate_audio(config.VSW2)
        if 50000 < pad0 < 60000:
            generate_audio(config.VSW3)
        if 40000 < pad0 < 50000:
            generate_audio(config.VSW4)
        if pad1 > 65000:
            generate_audio(config.VSW5)
        if 60000 < pad1 < 65000:
            generate_audio(config.VSW6)
        if 50000 < pad1 < 60000:
            generate_audio(config.VSW7)
        if 40000 < pad1 < 50000:
            generate_audio(config.VSW8)
