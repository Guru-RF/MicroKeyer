import board
import config
import MicroKeyer
import analogio
import audiocore
import audiopwmio

MicroKeyer.voiceLed.value = False

speakerAudio = audiopwmio.PWMAudioOut(board.GP23)
radioAudio = audiopwmio.PWMAudioOut(board.GP20)

keyPad0 = analogio.AnalogIn(board.GP26)
keyPad1 = analogio.AnalogIn(board.GP27)


def generate_audio(wavfile):
    if config.PTT_KEYER is False:
        MicroKeyer.pttKey.value = True
    print("Playing ", wavfile)
    data = open(wavfile, "rb")
    wav = audiocore.WaveFile(data)
    radioAudio.play(wav)
    while radioAudio.playing:
        pass
    if config.PTT_KEYER is False:
        MicroKeyer.pttKey.value = False


while True:
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
