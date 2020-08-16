"""
multiprocessing is good for CPU bound tasks
as demoed in this sample code.

"""

from time import perf_counter
from multiprocessing import Process, Queue
import random
from functools import reduce
from os import getpid

DONE = 'DONE'

def calc(q: Queue, n: int):
    pid = getpid()
    print(f'process id: {pid}')
    random_list = random.sample(range(1_000_000), n)
    # print(random_list)
    result = reduce(lambda x, y: x * y, random_list)
    # print(result)
    q.put(f'{pid}: {DONE}')

if __name__ == "__main__":
    t0 = perf_counter()

    nTasks = 4
    number = 50_000
    workers = []
    q = Queue()
    for i in range(nTasks):
        workers.append(Process(target=calc, args=(q, number)))

    for w in workers:
        w.start()

    nLeft = nTasks
    while nLeft > 0:
        ret = str(q.get()).split(':')
        print(ret)
        if ret[1].strip() == DONE:
            nLeft -= 1
            print(f'left: {nLeft}')

    for w in workers:
        w.join()

    t1 = perf_counter() - t0
    print(f'elapsed: {t1:.6f}')
