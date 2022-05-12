import MicroKeyer
import MorseGenerator

MicroKeyer.pcLed.value = False

while True:
    msg = ""
    try:
        msg = input('Enter Message: ')
    except KeyboardInterrupt:
        print("Ignore for now")
    print("Generating Morse")
    MorseGenerator.generate(msg)
