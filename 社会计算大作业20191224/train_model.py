from sklearn import metrics
import numpy as np

def predict(vector, cols, counts, type_table):
    prob = []
    for i in range(len(vector)):
        #记录这句话是某个话题的可能性，生成词向量
        current_prob = []
        for j in range(cols):
            #取出该词对于该话题的向量
            line = vector[i][j]
            #计算可能性
            sum = 0
            for k in range(len(line)):
                #可能性为这个词在这句话中出现的次数乘以这个词的权重，所有的和
                sum = sum + line[k] * counts[j][k]
            current_prob.append(sum)
        prob.append(current_prob)

        
    #domain用于记录最后的判断
    domain = []
    #softmax标准化
    for i in range(len(vector)):
        #先计算e阶乘和
        e_sum = 0
        for j in range(cols):
            e_sum = e_sum + np.exp(prob[i][j])
        #然后算softmax值
        for j in range(cols):
            prob[i][j] = np.exp(prob[i][j]) / e_sum
        #最后找出最大的概率
        max_prob = 0
        max_domain = 0
        for j in range(cols):
            if prob[i][j] > max_prob:
                max_prob = prob[i][j]
                max_domain = j
        choice = type_table[max_domain]
        domain.append(choice)
        
    return domain            

def start(train_vec, train_labels, develop_vec, develop_labels, columns, counts, type_table):
    prediction = predict(develop_vec, columns, counts, type_table)

    score_accuracy = metrics.accuracy_score(develop_labels, prediction)
    
    #打印预测的结果和得分
    print("accuracy score: {:.4f}".format(score_accuracy))
