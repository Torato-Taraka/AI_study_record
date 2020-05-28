import counting
import random

iters = 10
prime = []

def Miller_Rabin(n):
    t = n - 1
    s = 0
    while t % 2 == 0:
        t = t // 2
        s += 1
        
    for i in range(iters):
        b = prime[random.randint(0, len(prime))]
        r = counting.Fast(b, t, n)
        if r == n - 1 or r == 1:
            continue
        
        flag = 0
        for j in range(1, s):
            r = r ** 2 % n
            if r == n - 1:
                flag = 1
                break
        if flag:
            continue
        else:
            return False
    
    return True

def is_prime(x):
    for i in prime:
        if x % i == 0:
            return False
    
    return Miller_Rabin(x)

def get_big_prime(key_size = 512):
    while 1:
        n = random.randint(1 << (key_size - 1), 1 << key_size)
        if is_prime(n):
            return n

def get_prime_list(prime_list_len):
    prime_list = []
    for i in range(prime_list_len):
        prime_list.append(1)
        
    prime_list[0] = 0
    prime_list[1] = 0
    for i in range(2, prime_list_len):
        if prime_list[i] == 1:
            prime.append(i)
            x = i
            while x + i < prime_list_len:
                x += i
                prime_list[x] = 0
    #print(prime_list)

if __name__ == '__main__' :
    get_prime_list(1000)
    print(get_big_prime())