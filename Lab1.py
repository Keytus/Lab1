import logging


def fib(n):
    if n < 2:
        return n
    return fib(n-1)+fib(n-2)


logging.basicConfig(level=logging.INFO, format='%(message)s')
logging.info(f'Fibonacci number(10):{fib(10)}')
