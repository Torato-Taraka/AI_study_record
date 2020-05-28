import numpy as np
import pandas as pd

#评分矩阵R
R = np.array([[7, 6, 7, 4, 5, 4], 
             [ 6, 7, 0, 4, 3, 4],
             [ 0, 3, 3, 1, 1, 0],
             [ 1, 2, 2, 3, 3, 4],
             [ 1, 0, 1, 2, 3, 3]])
#参考人数 K
K = len(R)
#相关度阈值
min_sim = 0.5

def AVR(x):
    """
        计算非0项均值
    """
    #s是非0项的和，n是非0项个数
    s, n = 0, 0
    for i in range(len(x)):
        if x[i] != 0:
            s += x[i]
            n += 1
            
    return s / n

def Pearson(u, v):
    """
        pearson相似度
    """
    #uv为分子项，w_u、w_v为分母项
    uv, w_u, w_v = 0, 0, 0
    #计算u、v各自的评分均值
    avr_u, avr_v = AVR(u), AVR(v)
    #分别计算分子分母
    for i in range(len(u)):
        if u[i] != 0 and v[i] != 0:
            uv += (u[i] - avr_u) * (v[i] - avr_v)
            w_u += (u[i] - avr_u) ** 2
            w_v += (v[i] - avr_v) ** 2
    
    return uv / ( np.sqrt(w_u) * np.sqrt(w_v) )

def Cosine(u, v):
    """
        余弦相似度
    """       
    #uv为分子项，w_u、w_v为分母项
    uv, w_u, w_v = 0, 0, 0
    #分别计算分子分母
    for i in range(len(u)):
        if u[i] != 0 and v[i] != 0:
            uv += u[i]* v[i]
            w_u += u[i] ** 2
            w_v += v[i] ** 2
    
    return uv / ( np.sqrt(w_u) * np.sqrt(w_v) )

class UBCF:
    def __init__(self, sim_func = Pearson):
        self.sim_func = sim_func
        
    def fit(self, R):
        self.R = R
        #预处理每一行的平均值
        avr = np.zeros(len(R))
        for i in range(len(R)):
            avr[i] = AVR(R[i])
        self.avr = avr
        
    def predict(self, user, item, k = K - 1):
        #sim是相似度列表
        sim = np.zeros(len(self.R))
        #计算user和其他用户的相似度
        for i in range(len(self.R)):
            sim[i] = self.sim_func(self.R[user], self.R[i])
            
        #相似度排序，只取序号
        sim_sort = np.argsort(-sim)
        
        #取k个最相似的用户，如果有相似度小于阈值的用户则不予考虑
        #w_sim是有效评分用户相似度和，w_score是带权评分和，avr_u是user的平均评分
        w_sim, w_score = 0, 0
        #第一个必定是用户自己，所以不必考虑
        for i in range(1, k + 1):
            if sim[sim_sort[i]] > min_sim:
                w_sim += sim[sim_sort[i]]
                w_score += sim[sim_sort[i]] * (self.R[sim_sort[i], item] - self.avr[sim_sort[i]])
                
        return self.avr[user] + w_score / w_sim

if __name__ == '__main__' :
    model = UBCF()
    model.fit(R)
    prediction = model.predict(2, 0)
    print(prediction)