import storage
import board, digitalio
import supervisor

# If not pressed, the key will be at +V (due to the pull-up).
# https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/circuitpy-midi-serial#circuitpy-mass-storage-device-3096583-4
button = digitalio.DigitalInOut(board.GP18)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

supervisor.disable_autoreload()

# Disable devices only if button is not pressed.
if button.value:
    print(f"boot: button not pressed, disabling drive")
    storage.disable_usb_drive()
else:
    print(f"boot: button pressed, enabling drive")
    new_name = "µKeyer"
    storage.remount("/", readonly=False)
    m = storage.getmount("/")
    m.label = new_name
    storage.remount("/", readonly=True)

