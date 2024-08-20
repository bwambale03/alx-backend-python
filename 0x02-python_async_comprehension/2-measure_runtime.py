#!/usr/bin/env python3

'''Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.'''

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

def measure_runtime() -> float:
    '''measures the runtime of async_comprehension'''
    start = asyncio.get_event_loop().time()
    asyncio.run(asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension()))
    end = asyncio.get_event_loop().time()
    return end - start

asyncio.run(measure_runtime())