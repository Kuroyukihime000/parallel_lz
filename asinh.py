import asyncio
import random

number = 1

async def fun1():
    global number
    while True:
        jump = random.randint(1, 1000)
        number = min(number + jump, 1_000_000)
        await asyncio.sleep(0.1)
        print(f"fun1: {number}")

async def fun2():
    global number
    while True:
        jump = random.randint(1, 1000)
        number = min(number + jump, 1_000_000)
        await asyncio.sleep(0.1)
        print(f"fun2: {number}")

async def fun3():
    global number
    while True:
        jump = random.randint(1, 1000)
        number = min(number + jump, 1_000_000)
        await asyncio.sleep(0.1)
        print(f"fun3: {number}")

async def main():
    start_time = asyncio.get_event_loop().time()
    tasks = [asyncio.create_task(fun1()), asyncio.create_task(fun2()), asyncio.create_task(fun3())]

    while asyncio.get_event_loop().time() - start_time < 15:
        await asyncio.sleep(0.1)

    for task in tasks:
        task.cancel()

asyncio.run(main())