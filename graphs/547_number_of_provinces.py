def fn(n):
     print(fn2(0, n))


def fn2(i, n):
    if i > n:
        return 0
    if i == n:
        return 1

    return fn2(i + 1, n) + fn2(i + 2, n)


fn(4)