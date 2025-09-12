import asyncio

async def fetch_data(delay,id):
    print('fetching data id:',id)
    await asyncio.sleep(delay)
    print('fetch data id:',id)
    return {'key': 'value','id':id}

async def main():
    task1 = fetch_data(3,1)
    task2 = fetch_data(3,2)

    result1 = await task1
    print('result1:',result1)

    result2 = await task2
    print('result2:',result2)


asyncio.run(main())

# The two task are running sequentially even after using await, we didn't get any performance benefit here.
# just await the task to be finished.
