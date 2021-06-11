def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input('구하고 싶은 피보나치 수를 입력해주세요: '))
print(fibo(n))