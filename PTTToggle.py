import board
import time
import config
import MicroKeyer
import MorseGenerator
import analogio
import asyncio
import board
import pwmio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

pttState = False

async def run():
    global pttState

    keyPad0 = MicroKeyer.keyPad0
    keyPad1 = MicroKeyer.keyPad1

    while True:
        await asyncio.sleep(0.01)

        pad0 = keyPad0.value
        pad1 = keyPad1.value

        if 50000 < pad0 < 65550 and 50000 < pad1 < 65550:
            if MicroKeyer.pcLed.value is False and config.KEYBOARD is True and config.PTT_KBD_ENTER is True:
                print("Press Enter", pad0, pad1)
                keyboard_layout.write("\n")
                await asyncio.sleep(1.5)
            else:
                print("PTT Toggle", pad0, pad1)
                if pttState is True:
                    pttState = False
                    ptt = False
                    print("PTT Off")
                    MicroKeyer.pttKey.value = False
                    MicroKeyer.pttLed.value = True
                    MicroKeyer.PTT.value = False
                    await asyncio.sleep(0.5)
                elif pttState is False:
                    pttState = True
                    ptt = True
                    print("PTT On")
                    MicroKeyer.PTT.value = True
                    MicroKeyer.pttKey.value = True
                    MicroKeyer.pttLed.value = False
                    await asyncio.sleep(1.5)

