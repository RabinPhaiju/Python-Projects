import asyncio

async def fetch_data(id,sleep_time):
    print('fetching data id:',id)
    await asyncio.sleep(sleep_time)
    print('fetch data id:',id)
    return {'key': 'value','id':id}

async def main():

    # run coroutines concurrently and gather their return values
    results = await asyncio.gather(fetch_data(1,2),fetch_data(2,1),fetch_data(3,3))

    for result in results:
        print('Result',result)

asyncio.run(main())