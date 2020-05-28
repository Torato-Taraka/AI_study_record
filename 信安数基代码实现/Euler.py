def Euler(m):
    """
        欧拉函数
        input: m
        output: fai(m)
    """
    prime_list = []
    for i in range(m + 1):
        prime_list.append(1)
    
    for i in range(2, m + 1):
        x = i
        while x + i <= m:
            x = x + i
            prime_list[x] = 0
            
    euler = m
    for i in range(2, m + 1):
        if m % i == 0 and prime_list[i]:
            euler = euler * (1-1/i)
    
    return int(euler)
        
if __name__ == '__main__' :
    print(Euler(11))