import asyncio

async def fetch_data(id,sleep_time):
    print('fetching data id:',id)
    await asyncio.sleep(sleep_time)
    print('fetch data id:',id)
    return {'key': 'value','id':id}

async def main():
    task1 = asyncio.create_task(fetch_data(1,4))
    task2 = asyncio.create_task(fetch_data(2,6))
    task3 = asyncio.create_task(fetch_data(3,2))

    result1 = await task1
    print('result1:',result1)

    result2 = await task2
    print('result2:',result2)

    result3 = await task3
    print('result3:',result3)

asyncio.run(main())

# allow us to run multiple task at the same time.