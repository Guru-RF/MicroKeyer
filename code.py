# Need to implement threading on one button to select (load/unload different modules)
import asyncio
import MicroKeyer
import config
import time
import PC
import Paddle
import Manual
import Voice
import Beacon
import PTTToggle
import HangTime
import Decoder

apps = ["Manual", "Beacon", "PC", "Voice"]



async def menu(apps, app, event_loop):
    print("Init Hangtime")
    hangtime = asyncio.create_task(HangTime.run())
    print("Init Iambic B")
    paddleDah = asyncio.create_task(Paddle.PaddleKeyDah())
    paddleDit = asyncio.create_task(Paddle.PaddleKeyDit())
    print("Init Keyer")
    keyer = asyncio.create_task(Paddle.keyer())
    print("Init PTT Toggle")
    ptttoggle = asyncio.create_task(PTTToggle.run())
    print("Iambic decoder")
    decoder = asyncio.create_task(Decoder.run())

    currentIndex = apps.index(app)
    if app == "PC":
        MicroKeyer.pcLed.value = False
        app_task = asyncio.create_task(PC.run())
    if app == "Voice":
        MicroKeyer.voiceLed.value = False
        app_task = asyncio.create_task(Voice.run())
    if app == "Beacon":
        app_task = asyncio.create_task(Beacon.run())
        MicroKeyer.beaconLed.value = False
    if app == "Manual":
        MicroKeyer.manLed.value = False
        app_task = asyncio.create_task(Manual.run())

    while (True):
        if MicroKeyer.keyMode.value is False:
            MicroKeyer.pcLed.value = True
            MicroKeyer.voiceLed.value = True
            MicroKeyer.beaconLed.value = True
            MicroKeyer.manLed.value = True
            app_task.cancel()
            if (currentIndex + 1 is len(apps)):
                currentIndex = 0
            else:
                currentIndex += 1
            print("->", apps[currentIndex])
            if apps[currentIndex] == "PC":
                MicroKeyer.pcLed.value = False
                app_task = asyncio.create_task(PC.run())
            if apps[currentIndex] == "Voice":
                MicroKeyer.voiceLed.value = False
                app_task = asyncio.create_task(Voice.run())
            if apps[currentIndex] == "Beacon":
                app_task = asyncio.create_task(Beacon.run())
                MicroKeyer.beaconLed.value = False
            if apps[currentIndex] == "Manual":
                app_task = asyncio.create_task(Manual.run())
                MicroKeyer.manLed.value = False
            await asyncio.sleep(0.2)

        await asyncio.sleep(0.1)


async def main():
    loop = asyncio.get_event_loop()
    menu_task = asyncio.create_task(menu(apps, config.DEFAULT, loop))

    loop.run_until_complete(menu_task)
    loop.close()


print("Intializing MicroKeyer")
time.sleep(1)

print("Lets go async !")
asyncio.run(main())
