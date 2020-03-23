x = 11
n = 281

answer = set()

for i in range(n):
    if (i**2)%n == x:
        print(i)
    answer.add((i**2)%n)
    
print(answer)

if x in answer:
    print('yes')
else:
    print('no')
    
print((+4*14-4*78) % 91)