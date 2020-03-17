import numpy as np
import pandas as pd

#评分矩阵R
R = np.array([[4, 0, 2, 0, 1], 
             [ 0, 2, 3, 0, 0],
             [ 1, 0, 2, 4, 0],
             [ 5, 0, 0, 3, 1],
             [ 0, 0, 1, 5, 1],
             [ 0, 3, 2, 4, 1],])

"""
输入参数：
R：M*N 的评分矩阵
K：隐特征向量维度
max_iter：最大迭代次数
alpha：步长
lamda：正则化系数

输出：
分解后的P、Q
P：初始化用户特征矩阵M*K
Q：初始化物品特征矩阵N*K
"""

#给定超参数

K = 2
max_iter = 5000
alpha = 0.0005
lamda = 0.004

#核心算法
def LFM_grad_desc( R, K, max_iter = 1000, alpha = 0.0001, lamda = 0.004 ):
    #基本维度参数定义
    M = len(R)
    N = len(R[0])
    
    #P，Q初始值,随机生成
    P = np.random.rand(M, K)
    Q = np.random.rand(N, K)
    Q = Q.T
    
    #开始迭代
    for step in range(max_iter):
        #遍历用户u，物品i，对应的特征向量Pu、Qi梯度下降
        for u in range(M):
            for i in range(N):
                #有评分才计算误差
                if R[u, i] > 0:
                    ui = np.dot( P[u , : ], Q[ : , i] ) - R[u, i]
                    
                    #梯度下降，更新Pu，Qi
                    for k in range(K):
                        P[u, k] = P[u, k] - alpha * ( 2 * ui * Q[k, i] + 2 * lamda * P[u, k] )
                        Q[k, i] = Q[k, i] - alpha * ( 2 * ui * P[u, k] + 2 * lamda * Q[k, i] )
        
        #u、i遍历完成，所有特征向量更新完成，可以得到P、Q，可以计算预测评分矩阵
        pred_R = np.dot( P , Q )
        
        #计算当前损失函数
        cost = 0
        for  u in range(M):
            for i in range(N):
                if R[u, i] > 0:
                    cost += (pred_R[u, i] - R[u, i]) ** 2
                    #加上正则化项
                    for k in range(K):
                        cost += lamda * ( P[u, k] ** 2 + Q[k, i] ** 2 )
                        
        if cost < 0.0001:
            break
        
    return P, Q.T, cost

P, Q, cost = LFM_grad_desc(R, K, max_iter, alpha, lamda)

print(P)
print(Q)
print(cost)
print(R)

pred_R = np.dot( P, Q.T )
print(pred_R)