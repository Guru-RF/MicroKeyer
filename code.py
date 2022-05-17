# Need to implement threading on one button to select (load/unload different modules)
import asyncio
import supervisor
import MicroKeyer
import config
import PC
import Manual
import Voice

apps = ["Manual", "Beacon", "PC", "Voice"]
defaultApp = "Manual"

if supervisor.runtime.usb_connected:
  defaultApp = "PC"


async def menu(apps, app, event_loop):
  currentIndex = apps.index(app)
  if app == "PC":
    MicroKeyer.pcLed.value = False
    app_task = asyncio.create_task(PC.run())
  if app == "Voice":
    MicroKeyer.voiceLed.value = False
    app_task = asyncio.create_task(Voice.run())
  if app == "Beacon":
    MicroKeyer.beaconLed.value = False
  if app == "Manual":
    MicroKeyer.manualLed.value = False
    app_task = asyncio.create_task(Manual.run())

  while(True):
    if MicroKeyer.keyMode.value is False:
      MicroKeyer.pcLed.value = True
      MicroKeyer.voiceLed.value = True
      MicroKeyer.beaconLed.value = True
      MicroKeyer.manLed.value = True
      app_task.cancel()
      print("Push")
      if (currentIndex+1 is len(apps)):
        currentIndex=0
      else:
        currentIndex+=1
      print(apps[currentIndex])
      if apps[currentIndex] == "PC":
        MicroKeyer.pcLed.value = False
        app_task = asyncio.create_task(PC.run())
      if apps[currentIndex] == "Voice":
        MicroKeyer.voiceLed.value = False
        app_task = asyncio.create_task(Voice.run())
      if apps[currentIndex] == "Beacon":
        MicroKeyer.beaconLed.value = False
      if apps[currentIndex] == "Manual":
        MicroKeyer.manLed.value = False
        app_task = asyncio.create_task(Manual.run())
      await asyncio.sleep(0.2)

    await asyncio.sleep(0.1)

async def main():
  loop = asyncio.get_event_loop()
  menu_task = asyncio.create_task(menu(apps, defaultApp, loop))

  loop.run_until_complete(menu_task)
  loop.close()

asyncio.run(main())


