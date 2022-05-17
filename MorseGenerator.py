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
speaker = pwmio.PWMOut(board.GP25, frequency=config.CW_TONE)
output = pwmio.PWMOut(board.GP24, frequency=config.CW_TONE)


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
    MicroKeyer.cwLed.value = False
    MicroKeyer.cwKey.value = True
    play_tone()
    time.sleep(config.ONE_UNIT)
    be_quiet()
    MicroKeyer.cwKey.value = False
    MicroKeyer.audioLed.value = True
    MicroKeyer.cwLed.value = True
    time.sleep(config.TWO_UNITS)


# -
def dah():
    MicroKeyer.audioLed.value = False
    MicroKeyer.cwLed.value = False
    MicroKeyer.cwKey.value = True
    play_tone()
    time.sleep(config.THREE_UNITS)
    be_quiet()
    MicroKeyer.cwKey.value = False
    MicroKeyer.audioLed.value = True
    MicroKeyer.cwLed.value = True
    time.sleep(config.ONE_UNIT)


# TODO ! needs rework with new board "PTT_KEYER" depricated dedicated CW OUT !
def generate(msg):
    MicroKeyer.pttKey.value = True
    MicroKeyer.pttLed.value = False
    time.sleep(config.PTT_DELAY)
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
                    MicroKeyer.cwLed.value = False
                    MicroKeyer.cwKey.value = True
                    play_tone()
                    time.sleep(config.ONE_UNIT)
                    be_quiet()
                    MicroKeyer.audioLed.value = True
                    MicroKeyer.cwLed.value = True
                    MicroKeyer.cwKey.value = False
                    time.sleep(config.ONE_UNIT)
                if cw == '-':
                    # print(cw)
                    MicroKeyer.audioLed.value = False
                    MicroKeyer.cwLed.value = False
                    MicroKeyer.cwKey.value = True
                    play_tone()
                    time.sleep(config.THREE_UNITS)
                    be_quiet()
                    MicroKeyer.cwLed.value = True
                    MicroKeyer.cwKey.value = False
                    MicroKeyer.audioLed.value = True
                    time.sleep(config.ONE_UNIT)
            time.sleep(config.SEVEN_UNITS)
    MicroKeyer.pttKey.value = False
    MicroKeyer.pttLed.value = True
