def prime(start, end):
    result = []
    for i in range(start, end):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
            if flag:
                result.append(i)
        return result
prime(1, 50)