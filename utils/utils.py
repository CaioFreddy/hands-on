"""Some utils functions that can be used in some scripts"""
import time


def time_decorator(func):
    """Calculate the execution time of a method and return it back"""

    def calc_time(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"Time of {func.__name__} was: {duration}.")
        return result

    return calc_time
