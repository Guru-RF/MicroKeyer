import time
import config
import MicroKeyer
import MorseGenerator

MicroKeyer.beaconLed.value = False

while True:
    print("Beacon: Generating Morse: ", config.BEACON)
    MorseGenerator.generate(config.BEACON)
    print("Sleeping for ", config.BEACON_SLEEP, " seconds")
    time.sleep(config.BEACON_SLEEP)
