def bezout(a, b):
    """
        欧几里得带余除法求bezout等式
        input: a, b
        output: s, t, gcd
        其中，s*a + t*b = gcd(a, b)
    """
    if a == 1:
        return 1, 0, 1
    
    div_list = []
    
    r = 1
    while (r > 0):
        r = a % b
        div_list.append(a // b)
        a = b
        b = r
    #print(div_list)
    
    gcd = a
    n = len(div_list)
    s = 1
    t = - div_list[n-2]
    for i in range(1, n-1):
        x = div_list[n - 2 - i]
        if i % 2:
            s = s - t * x
        else:
            t = t - s * x
            
    if div_list[0] == 0:
        return t, s, gcd
    else:
        return s, t, gcd


def primary_congruence(a, b, m):
    """
        一次同余式 ax = b (mod m) 的一般解
        input: a, b, m
        output: x_list
    """
    _, _, gcd_a_m = bezout(a, m)
    
    t = gcd_a_m
    
    temp_inverse, _, _ = bezout(a // gcd_a_m, m // gcd_a_m)
    
    answer = []
    for i in range(t):
        answer.append(b // gcd_a_m * temp_inverse + i * m // gcd_a_m)
    
    return answer
    
def CRT(b_list, m_list):
    """
        中国剩余定理
        input: b1, b2, b3, ..., m1, m2, m3, ...
        output: x
    """
    m = 1
    for i in range(len(m_list)):
        m = m * m_list[i]
    print(m)
        
    M_list = []
    for i in range(len(m_list)):
        M_list.append(m // m_list[i])
    print(M_list)
    
    M_inverse_list = []
    for i in range(len(m_list)):
        M_inverse, _, _ = bezout( M_list[i] % m_list[i] , m_list[i] )
        M_inverse_list.append((M_inverse + m_list[i]) % m_list[i])
    print(M_inverse_list)
        
    x = 0
    for i in range(len(m_list)):
        x = x + b_list[i] * M_inverse_list[i] * M_list[i]
    
    return x % m

if __name__ == '__main__' :
    #print(bezout(1, 5))
    #print(primary_congruence(3, 3, 12))
    print(CRT([2, 3, 2], [3, 5, 7]))