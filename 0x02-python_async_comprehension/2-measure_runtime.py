#!/usr/bin/env python3

'''Import async_comprehension from the previous file
    and write a measure_runtime coroutine that will execute async_
    comprehension four times in parallel using asyncio.gather.

    measure_runtime should measure the total runtime and return it.

    Notice that the total runtime is roughly 10 seconds,
    explain it to yourself.'''

import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measures the runtime of async_comprehension executed
    4 times in parallel'''
    start = perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = perf_counter()
    return end - start

# measuring the runtime of measure_runtime(coroutine)
if __name__ == "__main__":
    runtime = asyncio.run(measure_runtime())
    print(f"Runtime: {runtime:.2f} seconds")
