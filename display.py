
# Importing the relevant libraries
import websockets
import asyncio

# The main function that will handle connection and communication 
# with the server
async def listen():
    url = "ws://atom-radpi-01.local:7890"
    # Connect to the server
    async with websockets.connect(url) as ws:
        # Send a greeting message
        await ws.send("{'request': 'distance'}")
        # Stay alive forever, listening to incoming msgs
        #while True:
        msg = await ws.recv()
        print(msg)
        #await ws.send(input("Send to server: ")) 

# Start the connection
asyncio.get_event_loop().run_until_complete(listen())