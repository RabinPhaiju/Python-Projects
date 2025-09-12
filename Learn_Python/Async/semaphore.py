import asyncio

async def access_resource(semaphore,id):
    async with semaphore:
        # simulate accessing a limited resource
        print(rf'Accessing resource {id}')
        await asyncio.sleep(1)
        print(rf'Finished accessing resource {id}')

async def main():
    semaphore = asyncio.Semaphore(2) # limit to 2 concurrent access

    await asyncio.gather(*(access_resource(semaphore,id) for id in range(5)))

asyncio.run(main())