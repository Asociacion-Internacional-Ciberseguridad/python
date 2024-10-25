import asyncio
import random

async def productor(queue):
    for _ in range(10):
        item = random.randint(1, 100)
        await queue.put(item)
        print(f"Producido {item}")
        await asyncio.sleep(1)

async def consumidor(queue):
    for _ in range(10):
        item = await queue.get()
        print(f"Consumido {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    productor_task = asyncio.create_task(productor(queue))
    consumidor_task = asyncio.create_task(consumidor(queue))
    await asyncio.gather(productor_task, consumidor_task)

asyncio.run(main())
