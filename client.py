# Importing the relevant libraries
import websockets
import asyncio
import results_display
import json
from gpiozero import Button

# Set up the GPIO button
button = Button(23)


# The main function that will handle connection and communication
# with the server
async def listen():
    url = "ws://atom-radpi-01.local:7890"
    # Connect to the server
    async with websockets.connect(url) as ws:
        # Send request for data
        button.wait_for_press()
        await ws.send('{"request": "distance"}')
        # Stay alive forever, listening to incoming msgs
        # while True:
        msg = await ws.recv()
        print(msg)
        data = json.loads(msg)
        data["label"] = "Distance"
        results_display.draw_display(json.dumps(data))

        # await ws.send(input("Send to server: "))


# Start the connection
asyncio.get_event_loop().run_until_complete(listen())
