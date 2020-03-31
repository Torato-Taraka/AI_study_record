import numpy as np

n = 2003

is_prime = 1
for i in range(2, int(np.sqrt(n))):
    if n % i == 0:
        is_prime = 0
        print(i)
        break

print(is_prime)