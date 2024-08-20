#!/usr/bin/env python3

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def main():
    result = await async_comprehension()
    print(result)
asyncio.run(main())