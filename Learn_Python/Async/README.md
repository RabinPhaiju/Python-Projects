# When to choose what
1. Asyncio
    - task that wait a lot. (network request, reading files, db query)
    - best for handling task concurrently without using much cpu power. (more efficient & responsive)
    
2. Threads
    - task that wait too but also shares data.
    - runs in parallel. ( io bound but less cpu intensive)
    
# event,condition