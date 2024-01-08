import asyncio
import websockets


async def connect_to_server():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            message = input("Enter message: ")
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Received: {response}")

if __name__ == "__main__":
    asyncio.run(connect_to_server())
