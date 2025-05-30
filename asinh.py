import asyncio
import random

async def lol():
    start = asyncio.get_event_loop().time()
    a = random.randint(1, 1000000)  
    while asyncio.get_event_loop().time() - start < 1:
        yield a
        a = random.randint(1, 1000000)
        await asyncio.sleep(0.1)

async def lolo():
    async for numb in lol():
        print(numb)