import board
import digitalio

audioLed = digitalio.DigitalInOut(board.GP11)
audioLed.direction = digitalio.Direction.OUTPUT

pttLed = digitalio.DigitalInOut(board.GP12)
pttLed.direction = digitalio.Direction.OUTPUT

keyLed = digitalio.DigitalInOut(board.GP10)
keyLed.direction = digitalio.Direction.OUTPUT

kbdLed = digitalio.DigitalInOut(board.GP13)
kbdLed.direction = digitalio.Direction.OUTPUT

manLed = digitalio.DigitalInOut(board.GP7)
manLed.direction = digitalio.Direction.OUTPUT

beaconLed = digitalio.DigitalInOut(board.GP8)
beaconLed.direction = digitalio.Direction.OUTPUT

pcLed = digitalio.DigitalInOut(board.GP6)
pcLed.direction = digitalio.Direction.OUTPUT

voiceLed = digitalio.DigitalInOut(board.GP14)
voiceLed.direction = digitalio.Direction.OUTPUT

pttKey = digitalio.DigitalInOut(board.GP19)
pttKey.direction = digitalio.Direction.OUTPUT

audioLed.value = True
pttLed.value = True
keyLed.value = True
kbdLed.value = True
manLed.value = True
beaconLed.value = True
pcLed.value = True
voiceLed.value = True

pttKey.value = False

keyA = digitalio.DigitalInOut(board.GP16)
keyA.direction = digitalio.Direction.INPUT
