"""
Description:
- It demos asyncio, decorator with pdb, etc.

Sample output:

start: 123
123: 122
start: 246
246: 245
start: 369
369: 368
123: 121
246: 244
==> highest prime below 369: 367
end: 369
123: 120
246: 243
123: 119
246: 242
123: 118
==> highest prime below 246: 241
end: 246
123: 117
123: 116
123: 115
123: 114
==> highest prime below 123: 113
end: 123
elapsed: 0.003601

"""

from time import perf_counter
import pdb
import asyncio as ai


def debug(func):
    def func_wrapper(*args, **kwargs):
        pdb.set_trace()
        return func(*args, **kwargs)
    return func_wrapper


# @debug
def isprime(x):
    for y in range(2, x//2 + 1):
        if x % y == 0:
            break
    else:
        return True
    return False


async def highest_prime(x):
    print(f'start: {x}')
    for y in range(x-1, 1, -1):
        if isprime(y):
            print(f'==> highest prime below {x}: {y}')
            break
        print(f'{x}: {y}')
        await ai.sleep(0)
    print(f'end: {x}')


async def main():
    x = 123
    # print(f'is {x} prime? {isprime(x)}')
    # print(*(highest_prime(x * i) for i in range(1, 4)))
    await ai.gather(*(highest_prime(x * i) for i in range(1, 4)))


if __name__ == "__main__":
    t0 = perf_counter()
    ai.run(main())
    t1 = perf_counter() - t0
    print(f'elapsed: {t1:.6f}')
