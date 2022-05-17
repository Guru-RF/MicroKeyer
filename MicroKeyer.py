import board
import digitalio

audioLed = digitalio.DigitalInOut(board.GP6)
audioLed.direction = digitalio.Direction.OUTPUT

pttLed = digitalio.DigitalInOut(board.GP12)
pttLed.direction = digitalio.Direction.OUTPUT

keyLed = digitalio.DigitalInOut(board.GP10)
keyLed.direction = digitalio.Direction.OUTPUT

cwLed = digitalio.DigitalInOut(board.GP21)
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

audioLed.value = True
pttLed.value = True
keyLed.value = True
kbdLed.value = True
manLed.value = True
beaconLed.value = True
pcLed.value = True
cwLed.value = True
voiceLed.value = True

pttKey.value = False
cwKey.value = False

# INPUTS

keyMode = digitalio.DigitalInOut(board.GP18)
keyMode.direction = digitalio.Direction.INPUT
keyMode.pull = digitalio.Pull.UP

keyA = digitalio.DigitalInOut(board.GP16)
keyA.direction = digitalio.Direction.INPUT
keyA.pull = digitalio.Pull.UP

keyB = digitalio.DigitalInOut(board.GP17)
keyB.direction = digitalio.Direction.INPUT
keyB.pull = digitalio.Pull.UP
