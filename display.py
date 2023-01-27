import websockets
import asyncio

address = "ws://atom-radpi-01.local"
PORT = 7890

async def listen():
    url = address+":"+str(PORT)

    print(url)

    async with websockets.connect(url) as ws:
        while True:
            await ws.send(input("Send message to server "))
            msg = await ws.recv()
            print("Recieved from client: "+ msg)

asyncio.get_event_loop().run_until_complete(listen())