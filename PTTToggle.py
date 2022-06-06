import supervisor
import config
import MicroKeyer
import asyncio



async def run():
    pttState = False

    if supervisor.runtime.usb_connected is True:
        import usb_hid
        from adafruit_hid.keyboard import Keyboard
        from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

        keyboard = Keyboard(usb_hid.devices)
        keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)
        usbConnected = True

    keyPad0 = MicroKeyer.keyPad0
    keyPad1 = MicroKeyer.keyPad1

    while True:
        await asyncio.sleep(0.05)

        pad0 = keyPad0.value
        pad1 = keyPad1.value

        if 48000 < pad0 < 65550 and 48000 < pad1 < 65550:
            if MicroKeyer.pcLed.value is False and config.KEYBOARD is True and config.PTT_KBD_ENTER is True and usbConnected is True:
                print("Press Enter", pad0, pad1)
                keyboard_layout.write("\n")
                await asyncio.sleep(0.5)
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
                    await asyncio.sleep(0.5)

