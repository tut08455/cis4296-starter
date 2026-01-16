

def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

num = int(input("n-th fibonacci number: "))
print(fib(num))
