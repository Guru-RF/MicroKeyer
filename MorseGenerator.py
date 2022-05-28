import MicroKeyer
import config
import time
import board
import pwmio
import Morse
import asyncio

## The secret CW morse code (not so secret after all ;))
#CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
#        'D': '-..', 'E': '.', 'F': '..-.',
#        'G': '--.', 'H': '....', 'I': '..',
#        'J': '.---', 'K': '-.-', 'L': '.-..',
#        'M': '--', 'N': '-.', 'O': '---',
#        'P': '.--.', 'Q': '--.-', 'R': '.-.',
#        'S': '...', 'T': '-', 'U': '..-',
#        'V': '...-', 'W': '.--', 'X': '-..-',
#        'Y': '-.--', 'Z': '--..',
#
#        '0': '-----', '1': '.----', '2': '..---',
#        '3': '...--', '4': '....-', '5': '.....',
#        '6': '-....', '7': '--...', '8': '---..',
#        '9': '----.'
#        }


# play tone
def play_tone(speaker, output):
    speaker.duty_cycle = config.SPEAKER_VOLUME
    output.duty_cycle = config.OUTPUT_VOLUME


# be silent
def be_quiet(speaker, output):
    # Set minimum volume
    speaker.duty_cycle = 0
    output.duty_cycle = 0



def generate(msg):
    speaker = pwmio.PWMOut(board.GP25, frequency=config.CW_TONE)
    output = pwmio.PWMOut(board.GP24, frequency=config.CW_TONE)

    if MicroKeyer.pttKey.value is False:
        MicroKeyer.pttKey.value = True
        MicroKeyer.pttLed.value = False
        time.sleep(config.PTT_DELAY)
    try:
        for char in msg:
            if char == ' ':
                print("␍")
                time.sleep(config.SEVEN_UNITS)
            else:
                # print(char)
                #   for cw in CODE[char.upper()]:
                    for cw in Morse.encode(char.lower()):
                        if cw == '.':
                            print(cw, end="")
                            MicroKeyer.audioLed.value = False
                            MicroKeyer.cwLed.value = False
                            MicroKeyer.cwKey.value = True
                            play_tone(speaker, output)
                            time.sleep(config.ONE_UNIT)
                            be_quiet(speaker, output)
                            MicroKeyer.audioLed.value = True
                            MicroKeyer.cwLed.value = True
                            MicroKeyer.cwKey.value = False
                            time.sleep(config.ONE_UNIT)
                        if cw == '-':
                            print(cw, end="")
                            MicroKeyer.audioLed.value = False
                            MicroKeyer.cwLed.value = False
                            MicroKeyer.cwKey.value = True
                            play_tone(speaker, output)
                            time.sleep(config.THREE_UNITS)
                            be_quiet(speaker, output)
                            MicroKeyer.cwLed.value = True
                            MicroKeyer.cwKey.value = False
                            MicroKeyer.audioLed.value = True
                            time.sleep(config.ONE_UNIT)
                    print("\t\t\t", char.lower())
                    time.sleep(config.SEVEN_UNITS)
    except KeyError:
        return

    output.deinit()
    speaker.deinit()
    MicroKeyer.PTTstate.value = True
