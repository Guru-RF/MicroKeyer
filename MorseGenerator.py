import MicroKeyer
import config
import time
import board
import pwmio
import Morse
import OLED


# play tone
def play_tone(output):
    output.duty_cycle = config.OUTPUT_VOLUME


# be silent
def be_quiet(output):
    # Set minimum volume
    output.duty_cycle = 0


def generate(msg):
    output = pwmio.PWMOut(board.GP24, frequency=config.CW_TONE)

    if MicroKeyer.pttKey.value is False:
        MicroKeyer.pttKey.value = True
        MicroKeyer.pttLed.value = False
        time.sleep(config.PTT_DELAY)
    try:
        for char in msg:
            if char == ' ':
                print("␍", end="")
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
                            play_tone(output)
                            time.sleep(config.ONE_UNIT)
                            be_quiet(output)
                            MicroKeyer.audioLed.value = True
                            MicroKeyer.cwLed.value = True
                            MicroKeyer.cwKey.value = False
                            time.sleep(config.ONE_UNIT)
                        if cw == '-':
                            print(cw, end="")
                            MicroKeyer.audioLed.value = False
                            MicroKeyer.cwLed.value = False
                            MicroKeyer.cwKey.value = True
                            play_tone(output)
                            time.sleep(config.THREE_UNITS)
                            be_quiet(output)
                            MicroKeyer.cwLed.value = True
                            MicroKeyer.cwKey.value = False
                            MicroKeyer.audioLed.value = True
                            time.sleep(config.ONE_UNIT)
            print("\t\t\t", char.lower())
	    OLED.printDb(char.lower())
            time.sleep(config.SEVEN_UNITS)
    except KeyError:
        return

    output.deinit()
    MicroKeyer.PTTstate.value = True
