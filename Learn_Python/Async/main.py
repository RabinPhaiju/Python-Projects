import asyncio

# Define a coroutine that simluates a time-consuming task
async def fetch_data(delay):
    print('start of fetch_data co-routine')
    await asyncio.sleep(delay)
    print('end of fetch_data co-routine')
    return {'key': 'value'}

# coroutine function
async def main():
    print('start of main co-routine')

    # await asyncio.sleep(1)
    task = fetch_data(3) # just created but not executed
    print(f'task: {task}')

    # Awaits the fetch_data coroutine, pausing execution of main until it completes
    result = await task
    print(rf'received result: {result}')

    print('end of main co-routine')

asyncio.run(main()) # main() -> coroutine object