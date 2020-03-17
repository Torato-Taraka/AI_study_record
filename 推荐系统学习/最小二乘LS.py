import numpy as np
import matplotlib.pyplot as plt

points = np.genfromtxt('E:\\python AI\\test.txt', delimiter = ',')

#print(points)

x = points[:, 0]
y = points[:, 1]

plt.scatter(x, y)
plt.show()

#损失函数计算
def compute_cost(w, b, points):
    total_cost = 0
    M = len(points)
    
    for i in range(M):
        x = points[i, 0]
        y = points[i, 1]
        total_cost += (y - w * x - b) ** 2;
        
    return total_cost/M

#求平均值
def average(data):
    sum = 0
    num = len(data)
    for i in range(num):
        sum += data[i]
    return sum/num

#拟合函数
def fit(points):
    M = len(points)
    x_bar = average(points[:, 0])
    
    sum_yx = 0
    sum_x2 = 0
    sum_delta = 0
    
    for i in range(M):
        x = points[i, 0]
        y = points[i, 1]
        sum_yx += y * (x - x_bar)
        sum_x2 = x ** 2
    
    w = sum_yx / (sum_x2 - M * (x_bar ** 2) )
    
    for i in range(M):
        x = points[i, 0]
        y = points[i, 1]
        sum_delta += y - w * x
        
    b = sum_delta / M
    
    return w, b

w, b = fit(points)

print("w is ", w)
print("b is ", b)

cost = compute_cost (w, b, points)    
print("cost is ", cost)

plt.scatter(x, y)
pred_y = w * x + b

plt.plot(x, pred_y, c = "r")
plt.show()