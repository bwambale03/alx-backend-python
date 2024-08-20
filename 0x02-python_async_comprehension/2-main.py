#!/usr/bin/env python3

import asyncio

measure_runtime = __import__('2-measure_runtime').measure_runtime

async def main():
    '''measures the runtime of measure_runtime'''
    print(f"Runtime: {await measure_runtime()}")
    
asyncio.run(main())