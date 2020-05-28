def primitive_root(n, m = 100):
    for i in range(2, m):
        x = i
        for j in range(2, n):
            x = x * i % n
            if x == 1 :
                if j == n-1:
                    print(i)
                break

n = 257
m = 208
primitive_root(n, m)

print()
for x in range(1, n):
    if x ** 2 % n != 1 and x ** ((n-1) / 2) % n != 1:
        print(x)
  

x = 3
t = 1
for i in range(n):
    print("{0} : {1}".format(i, t))
    t = t * x % n
print()

for i in range(2,n):
    if m**i % n == 1:
        print(i)
        break