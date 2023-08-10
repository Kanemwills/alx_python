#!/usr/bin/python3
def fibonacci_sequence(n):
    if n <= 0:
        return []

    fib_sequence = []
    a, b = 0, 1

    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b

    return fib_sequence

