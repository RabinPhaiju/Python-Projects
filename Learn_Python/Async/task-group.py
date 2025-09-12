import asyncio

async def fetch_data(id,delay):
    print('start of fetch_data co-routine')
    # if id ==3:
        # raise ValueError('cannot be 3')
    await asyncio.sleep(delay)
    return {'key': 'value','id':id}

async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2,1,3],start=1):
            task = tg.create_task(fetch_data(i,sleep_time))
            tasks.append(task)
        
    
    # After the Task Group block, all tasks have completed
    results = [task.result() for task in tasks]

    for result in results:
        print('Result',result)


asyncio.run(main())