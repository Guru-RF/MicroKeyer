# Need to implement threading on one button to select (load/unload different modules)
import asyncio
import supervisor
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

apps = ["Manual", "Beacon", "PC", "Voice"]
defaultApp = "Manual"



async def menu(apps, app, event_loop):
    paddleA = asyncio.create_task(Paddle.keyA())
    paddleB = asyncio.create_task(Paddle.keyB())
    keyer = asyncio.create_task(Paddle.keyer())
    ptttoggle = asyncio.create_task(PTTToggle.run())
    hangtime = asyncio.create_task(HangTime.run())

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
    print("Intializing MicroKeyer")
    time.sleep(1)

    if supervisor.runtime.usb_connected:
        supervisor.disable_autoreload()
        defaultApp = "PC"

    print("Lets go async !")
    loop = asyncio.get_event_loop()
    menu_task = asyncio.create_task(menu(apps, defaultApp, loop))

    loop.run_until_complete(menu_task)
    loop.close()


asyncio.run(main())
