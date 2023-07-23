def fibonacci(n):
    if (n <= 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacciDynamic(n):
    fib = [0] * (n + 2)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

print(fibonacci(10))
print(fibonacciDynamic(10))