import asyncio
import websockets


async def connect_to_server():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        print("Connected to the server")
        await websocket.send("Hello, Server!")
        response = await websocket.recv()
        print(f"Received: {response}")


asyncio.run(connect_to_server())
