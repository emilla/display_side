import websockets
import asyncio

address = "ws://atom-radpi-01.local"
PORT = 7890

async def listen():
    url = "ws://"+"adress"+":"+str(PORT)

    async with websockets.connect(url) as ws:
        await ws.send('Hello Serever')
        while True:
            msg = await ws.recv()
            print(msg)

asyncio.get_event_loop().run_until_complete(listen())