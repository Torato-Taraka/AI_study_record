import numpy as np
import pandas as pd

#引入sklearn里的数据集，iris 鸢尾花
from sklearn.datasets import load_iris

#切分数据集为训练集和测试集的方法
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

#数据加载预处理
iris = load_iris()
#print(iris)

df = pd.DataFrame(data = iris.data, columns = iris.feature_names)
#print(df)
df['class'] = iris.target
#print(df)
df['class'] = df['class'].map({i: iris.target_names[i] for i in range(3)})
#print(df)

x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 30, stratify = y)

def l1_distance(x, y):
    return np.sum( np.abs(x - y) , axis = 1)

def l2_distance(x, y):
    return np.sqrt( np.sum( (x - y) ** 2 , axis = 1) )

class kNN:
    def __init__(self, neighbors = 1, dist_func = l1_distance):
        self.neighbors = neighbors
        self.dist_func = dist_func
        
    def fit(self, x, y):
        self.x_train = x
        self.y_train = y
        
    def predict(self, x):
        prediction = np.zeros( (x.shape[0], 1), dtype = self.y_train.dtype )
        
        for i, x_test in enumerate(x):
            distance = self.dist_func(self.x_train, x_test)
            index = np.argsort(distance)
            classification = self.y_train[index[:self.neighbors]].ravel()
            prediction[i] = np.argmax( np.bincount( classification ) ) 
    
        return prediction
    
knn = kNN()

knn.fit(x_train, y_train)

knn.neighbors = 3

prediction = knn.predict(x_test)

score = accuracy_score(prediction, y_test)

print(score)