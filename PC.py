import time
import MicroKeyer
import MorseGenerator
import supervisor
import asyncio
import sys

MicroKeyer.pcLed.value = False

class USBSerialReader:
    """ Read a line from USB Serial (up to end_char), non-blocking, with optional echo """
    def __init__(self):
        self.s = ''
    def read(self,end_char='\n', echo=True):
        n = supervisor.runtime.serial_bytes_available
        if n > 0:                    # we got bytes!
            s = sys.stdin.read(n)    # actually read it in
            if echo: sys.stdout.write(s)  # echo back to human
            self.s = self.s + s      # keep building the string up
            if s.endswith(end_char): # got our end_char!
                rstr = self.s        # save for return
                self.s = ''          # reset str to beginning
                rstr = rstr.rstrip('\r\n')
                rstr = rstr.rstrip('\n')
                return rstr
        return None                  # no end_char yet


async def run():
    usb_reader = USBSerialReader()
    print("type text to send:")
    while True:
        msg = usb_reader.read(end_char='\n', echo=True)
        await asyncio.sleep(0.01)
        if msg:
            print("Generating Morse", msg)
            MorseGenerator.generate(msg)
            msg = ""
            n = supervisor.runtime.serial_bytes_available
            sys.stdin.read(n)
            print("type text to send:")

