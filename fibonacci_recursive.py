"""
Function to create a Fibonacci series.

"""

'''
def fibonacci(n):
    """ Recursive Fibonacci sequence """
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
'''


def fibonacci_iteratively(n):
    series = [0, 1]
    i = 2
    while i <= n:
        series.append(series[i - 1] + series[i - 2])
        print(series)
        i += 1
    return series[n]

print(fibonacci_iteratively(10))


"""
def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        print(a)
        a, b = b, a + b
    return b
"""

