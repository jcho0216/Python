n = int(input())
def fac(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

print(fac(n))
    