반복문으로 구현한 factorial
def factorial(n):
    c = 1
    for i in range(1, n+1):
        c *= i
    return c

print(factorial(6))

재귀로 구현한 factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(6))