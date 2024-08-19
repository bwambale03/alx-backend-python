#!/usr/bin/env python3
'''
    a module for measuring the time it 
    takes to run a given number of 
    asycnronous tasksconcurrently
'''
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int = 0, max_delay: int = 10) -> float:
    '''
        measure the runtime of wait_n
    '''
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n