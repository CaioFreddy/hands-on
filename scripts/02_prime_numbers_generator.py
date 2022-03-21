"""Module that contains a function to generate prime numbers"""
from collections import defaultdict
from itertools import islice


def png():
    """Function that generate prime numbers"""
    memory = defaultdict(list)
    prime_number = 2

    while True:
        if prime_number not in memory:
            yield prime_number
            memory[2 * prime_number].append(prime_number)
        else:
            for item in memory[prime_number]:
                memory[prime_number + item].append(item)
        prime_number += 1


for n in islice(png(), 10):
    print(n)
