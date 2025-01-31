import asyncio
import websockets


async def handle_connection(websocket, path):
    print(f"New connection from {path}")
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            await websocket.send(f"Echo: {message}")
    except websockets.exceptions.ConnectionClosedOK:
        print("Connection closed")


async def main():
    server = await websockets.serve(handle_connection, "localhost", 8765)
    print("WebSocket server started on ws://localhost:8765")
    await server.wait_closed()


asyncio.run(main())
