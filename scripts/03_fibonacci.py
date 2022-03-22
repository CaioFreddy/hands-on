"""Some functions that generate the fibonacci sequence"""
from functools import lru_cache
import time
from utils.utils import time_decorator

memory = {0: 0, 1: 1}


def fib_rec_mem_dict(n):
    """The Fibonacci sequence with recursion using memoization with dict"""
    if n not in memory:
        memory[n] = fib_rec_mem_dict(n - 1) + fib_rec_mem_dict(n - 2)
    return memory[n]


@lru_cache(maxsize=None)
def fib_memo_lrucache(n):
    """The Fibonacci sequence with recursion using automatic memoization with lru_cache"""
    if n < 2:
        return n
    return fib_memo_lrucache(n - 1) + fib_memo_lrucache(n - 2)


@time_decorator
def fib_iter(n):
    """The Fibonacci sequence with iteration"""
    if n == 0:
        return n
    last = 0
    nextn = 1
    for _ in range(1, n):
        last, nextn = nextn, last + nextn
    return nextn


def fib_generator(n):
    """The Fibonacci sequence with a generator"""
    yield 0
    if n > 0:
        yield 1
    last = 0
    nextn = 1
    for _ in range(1, n):
        last, nextn = nextn, last + nextn
        yield nextn


if __name__ == "__main__":
    num = 400

    start = time.time()
    fib_rec_mem_dict(num)
    print(f"Time of fib_rec_mem_dict was: {time.time() - start}.")
    # Time of fib_rec_mem_dict was: 0.0006008148193359375.

    start = time.time()
    fib_memo_lrucache(num)
    print(f"Time of fib_memo_lrucache was: {time.time() - start}.")
    # Time of fib_memo_lrucache was: 0.0003521442413330078.

    fib_iter(num)
    # Time of fib_iter was: 4.887580871582031e-05.

    start = time.time()
    for i in fib_generator(num):
        pass
    print(f"Time of fib_generator was: {time.time() - start}.")
    # Time of fib_generator was: 7.748603820800781e-05.
