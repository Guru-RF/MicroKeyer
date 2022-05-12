import MicroKeyer
import config
import time
import board
import pwmio

# The secret CW morse code (not so secret after all ;))
CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
        }

# set the output pins, and frequency
speaker = pwmio.PWMOut(board.GP23, frequency=config.CW_TONE_SPEAKER)
output = pwmio.PWMOut(board.GP20, frequency=config.CW_TONE_OUTPUT)


# play tone
def play_tone():
    # Set maximum volume
    speaker.duty_cycle = config.SPEAKER_VOLUME
    output.duty_cycle = config.OUTPUT_VOLUME


# be silent
def be_quiet():
    # Set minimum volume
    speaker.duty_cycle = 0
    output.duty_cycle = 0


# .
def dit():
    MicroKeyer.audioLed.value = False
    play_tone()
    time.sleep(config.ONE_UNIT)
    be_quiet()
    time.sleep(config.TWO_UNITS)
    MicroKeyer.audioLed.value = True


# -
def dah():
    MicroKeyer.audioLed.value = False
    play_tone()
    time.sleep(config.THREE_UNITS)
    be_quiet()
    time.sleep(config.ONE_UNIT)
    MicroKeyer.audioLed.value = True


# TODO ! needs rework with new board "PTT_KEYER" depricated dedicated CW OUT !
def generate(msg):
    if config.PTT_KEYER is False:
        MicroKeyer.pttKey.value = True
        time.sleep(config.ONE_UNIT)
    for char in msg:
        if char == ' ':
            # print(' ' * 7)
            time.sleep(config.SEVEN_UNITS)
        else:
            # print(char)
            for cw in CODE[char.upper()]:
                if cw == '.':
                    # print(cw)
                    MicroKeyer.audioLed.value = False
                    if config.PTT_KEYER is True:
                        MicroKeyer.pttKey.value = True
                    play_tone()
                    time.sleep(config.ONE_UNIT)
                    be_quiet()
                    MicroKeyer.audioLed.value = True
                    if config.PTT_KEYER is True:
                        MicroKeyer.pttKey.value = False
                    time.sleep(config.ONE_UNIT)
                if cw == '-':
                    # print(cw)
                    MicroKeyer.audioLed.value = False
                    if config.PTT_KEYER is True:
                        MicroKeyer.pttKey.value = True
                    play_tone()
                    time.sleep(config.THREE_UNITS)
                    be_quiet()
                    MicroKeyer.audioLed.value = True
                    if config.PTT_KEYER is True:
                        MicroKeyer.pttKey.value = False
                    time.sleep(config.ONE_UNIT)
            time.sleep(config.SEVEN_UNITS)
    if config.PTT_KEYER is False:
        MicroKeyer.pttKey.value = False
