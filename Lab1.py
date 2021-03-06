import logging


def fib(n):
    phi = (1 + 5**0.5)/2.0
    return int(round((phi**n - (1-phi)**n) / 5**0.5))


logging.basicConfig(level=logging.INFO, format='%(message)s')
logging.info(f'Fibonacci number(10):{fib(10)}')
