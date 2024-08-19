#!/usr/bin/env python3

'''
    a module for creating asyncio tasks that run asyncronous functions.
'''

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
        create an aysncio task that waits fr a random amount of time 
        up to `max_delay` seconds.whrn run
        Retutrns the created task
    '''
    return asyncio.create_task(wait_random(max_delay))