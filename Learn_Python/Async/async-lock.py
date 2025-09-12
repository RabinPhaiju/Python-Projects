import asyncio

shared_resource = 0 # db

lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_resource
    async with lock:
        # critical section starts
        print('resource before modification',shared_resource)
        shared_resource += 1
        await asyncio.sleep(2)
        print('resource after modification',shared_resource)
        # critical section ends

async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))

asyncio.run(main())