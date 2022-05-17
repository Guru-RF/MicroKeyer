# Need to implement threading on one button to select (load/unload different modules)
import asyncio
import supervisor



if supervisor.runtime.usb_connected:
  import PC
else:
  import Manual