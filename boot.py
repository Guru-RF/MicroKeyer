import storage
import board, digitalio
import supervisor
import MicroKeyer
import time

supervisor.disable_autoreload()

# Disable devices only if button is not pressed.
if MicroKeyer.keyMode.value:
    print(f"boot: button not pressed, disabling drive")
    storage.disable_usb_drive()
    storage.remount("/", readonly=False)
else:
    print(f"boot: button pressed, enabling drive")

    MicroKeyer.audioLed.value = False
    MicroKeyer.pttLed.value = False
    MicroKeyer.keyLed.value = False
    MicroKeyer.kbdLed.value = False
    MicroKeyer.cwLed.value = False

    MicroKeyer.manLed.value = False
    MicroKeyer.beaconLed.value = False
    MicroKeyer.pcLed.value = False
    MicroKeyer.voiceLed.value = False

    new_name = "µKeyer"
    storage.remount("/", readonly=False)
    m = storage.getmount("/")
    m.label = new_name
    storage.remount("/", readonly=True)

    time.sleep(2)



