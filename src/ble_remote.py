from bleak import BleakClient

async def notification_handler(sender, data):
    print("Gomb megnyomás:", data)
    # IDE: te definálod, mi legyen a gombnyomás hatása

async def main():
    async with BleakClient("58:2B:3E:B6:4D:FA") as client:
        await client.start_notify("YOUR-CHAR-UUID", notification_handler)
        await asyncio.Event().wait()  # fut örökké

import asyncio
asyncio.run(main())
