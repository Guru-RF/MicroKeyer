import board
import digitalio
import analogio


audioLed = digitalio.DigitalInOut(board.GP6)
audioLed.direction = digitalio.Direction.OUTPUT

pttLed = digitalio.DigitalInOut(board.GP12)
pttLed.direction = digitalio.Direction.OUTPUT

keyLed = digitalio.DigitalInOut(board.GP10)
keyLed.direction = digitalio.Direction.OUTPUT

cwLed = digitalio.DigitalInOut(board.GP5)
cwLed.direction = digitalio.Direction.OUTPUT

kbdLed = digitalio.DigitalInOut(board.GP13)
kbdLed.direction = digitalio.Direction.OUTPUT

manLed = digitalio.DigitalInOut(board.GP7)
manLed.direction = digitalio.Direction.OUTPUT

beaconLed = digitalio.DigitalInOut(board.GP8)
beaconLed.direction = digitalio.Direction.OUTPUT

pcLed = digitalio.DigitalInOut(board.GP23)
pcLed.direction = digitalio.Direction.OUTPUT

voiceLed = digitalio.DigitalInOut(board.GP14)
voiceLed.direction = digitalio.Direction.OUTPUT

# OUTPUTS

pttKey = digitalio.DigitalInOut(board.GP19)
pttKey.direction = digitalio.Direction.OUTPUT

cwKey = digitalio.DigitalInOut(board.GP11)
cwKey.direction = digitalio.Direction.OUTPUT

PTTstate = digitalio.DigitalInOut(board.GP15)
PTTstate.direction = digitalio.Direction.OUTPUT

PTT = digitalio.DigitalInOut(board.GP1)
PTT.direction = digitalio.Direction.OUTPUT

iambicAstate = digitalio.DigitalInOut(board.GP2)
iambicAstate.direction = digitalio.Direction.OUTPUT

iambicBstate = digitalio.DigitalInOut(board.GP3)
iambicBstate.direction = digitalio.Direction.OUTPUT

audioLed.value = True
pttLed.value = True
keyLed.value = True
kbdLed.value = True
cwLed.value = True

manLed.value = True
beaconLed.value = True
pcLed.value = True
voiceLed.value = True

pttKey.value = False
cwKey.value = False

# INPUTS

keyMode = digitalio.DigitalInOut(board.GP18)
keyMode.direction = digitalio.Direction.INPUT
keyMode.pull = digitalio.Pull.UP

keyDIT = digitalio.DigitalInOut(board.GP16)
keyDIT.direction = digitalio.Direction.INPUT
keyDIT.pull = digitalio.Pull.UP

keyDAH = digitalio.DigitalInOut(board.GP17)
keyDAH.direction = digitalio.Direction.INPUT
keyDAH.pull = digitalio.Pull.UP

keyPad0 = analogio.AnalogIn(board.GP26)
keyPad1 = analogio.AnalogIn(board.GP27)

