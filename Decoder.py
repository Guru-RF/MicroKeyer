import board
import time
import config
import MicroKeyer
import MorseGenerator
import analogio
import asyncio
import board
import pwmio
import Morse
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

async def run():

    word = False
    decodeLetter = False
    checkSpace = False
    toDecode = ""
    start = time.monotonic()

    while True:
        await asyncio.sleep(0.005)

        if decodeLetter is True:
            print("\t\t\t", Morse.decode(toDecode))
            if MicroKeyer.pcLed.value is False and config.KEYBOARD is True:
                keyboard_layout.write(Morse.decode(toDecode))
            toDecode = ""
            decodeLetter = False
            checkSpace = True

        if MicroKeyer.iambicAstate.value is True:
            if word is False:
                print("")
                word = True
            start = time.monotonic()
            toDecode += "-"
            print("-", end="")
            MicroKeyer.iambicAstate.value = False

        if MicroKeyer.iambicBstate.value is True:
            if word is False:
                #print("")
                word = True
            start = time.monotonic()
            toDecode += "."
            print(".", end="")
            MicroKeyer.iambicBstate.value = False

        if checkSpace is True and ((start + config.SEVEN_UNITS + config.ONE_UNIT) < time.monotonic()):
            if MicroKeyer.pcLed.value is False and config.KEYBOARD is True:
                keyboard_layout.write(" ")
            print("␍")
            checkSpace = False

        if word is True and ((start + config.THREE_UNITS + config.TWO_UNITS) < time.monotonic()):
            print("")
            word = False
            decodeLetter = True

