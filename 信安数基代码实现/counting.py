def Fast(a, n, m):
    """
        计算 a^n(mod m)
        input: a, n, m
        output: a^n % m
    """
    result = 1
    t = a
    while n > 0:
        if n % 2:
            result = result * t % m
        t = t ** 2 % m
        n = n // 2
    
    return result

if __name__ == '__main__':
    m = 199063407469228486126213758181565333299
    a = 5
    n = 99531703734614243063106879090782666649
    print(Fast(a, n, m))