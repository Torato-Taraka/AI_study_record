template = open("data.txt").read()
template = int(template, 16)

#print(template)

data1 = open("1.txt").read()
data1 = int(data1, 16)

data2 = open("2.txt").read()
data2 = int(data2, 16)

print(format(template ^ data1, 'b'))
print()
print(format(template ^ data2, 'b'))
print()
print(format(data1 ^ data2, 'b'))

x1 = bin(template ^ data1)
print(len(x1))
count = 0
for i in x1:
    if i == '1' :
        count+=1
print(count)

x2 = bin(template ^ data2)
count = 0
for i in x2:
    if i == '1' :
        count+=1
print(count)

x3 = bin(data1 ^ data2)
count = 0
for i in x3:
    if i == '1' :
        count+=1
print(count)