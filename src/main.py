import asyncio

from app import App

async def start_project() -> None:
    app = App()
    
    await app.configure()
    await app.start()
    
if __name__ == "__main__":
    asyncio.run(start_project())
