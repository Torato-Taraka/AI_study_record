import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import BernoulliNB
import jieba
import math

"""
@author: XXX
2019/10/30
社会计算（跨）第一次作业demo
""" 
min_freq = 1

def read_train_valid(filename):
    """
    读取训练或者验证文件
    :param filname: 训练集/验证集的文件名字
    :return:
    返回训练集的文本和标签
    其中文本是一个list, 标签是一个list(每个元素为int)
    返回示例：['我很开心', '你不是真正的快乐', '一切都是假的], [1, 0, 0]
    """
    
    #读文件， filename是文件名，‘r’表示读，encoding='utf-8'表示以‘utf-8’打开文件
    #返回结果是一个类似字符串，即整篇文章可以当一个str处理
    content = open(filename, 'r', encoding='utf-8').read()
    #content = open(filename, 'r', encoding='gbk').read()
    #切分，按照换行符‘\n’切分成一句一句的
    #结果是一个list， 每一句里面都是一个str对象
    sentences = content.split('\n')
    
    #切分句子

    labels = []
    sentences_splited = []
    for i in range(len(sentences)-1):
        if i == 0:    #第一行是表头，不用管, 从第二行开始读
            continue 
        sentence = sentences[i]
        #对每一个句子按照'\t'切开为标签和文本
        sentence = sentence.split(',')
        
        #print(sentence)

        #第三个元素为标签，转换成int型
        label = int(sentence[2])
        
        disease_category = sentence[3]
        
        sentence = list(jieba.cut(sentence[0])) + list(jieba.cut(sentence[1]))
        sentence.append(disease_category)
        
        sentences_splited.append(sentence)

        #将每一次读到的label添加到最终的labels列表后面
        labels.append(label)

    """
    print(sentences_splited)
    print('\n')
    print(labels)
    print('\n')
    """

    return sentences_splited, labels


def read_test(filename):
    
    """
    读取测试文件
    :param filname: 测试集文件名字
    :return:
    返回测试集文本和对应的id编号
    其中文本是一个list, id就是文件中的id
    返回示例：['我很开心', '你不是真正的快乐', '一切都是假的], [1,2,3]
    """

    #content = open(filename, 'r', encoding='gbk').read()
    content = open(filename, 'r', encoding='utf-8').read()
   
    sentences = content.split('\n')
    
    #切分句子

    labels = []
    sentences_splited = []
    for i in range(len(sentences)-1):
        if i == 0:    #第一行是表头，不用管, 从第二行开始读
            continue 
        sentence = sentences[i]
        #对每一个句子按照'\t'切开为标签和文本
        sentence = sentence.split(',')
        
        #print(sentence)

        #第三个元素为标签，转换成int型
        label = int(sentence[0])
        
        disease_category = sentence[3]
        
        sentence = list(jieba.cut(sentence[1])) + list(jieba.cut(sentence[2]))
        sentence.append(disease_category)
        
        sentences_splited.append(sentence)

        #将每一次读到的label添加到最终的labels列表后面
        labels.append(label)
        
    """
    print(sentences_splited)
    print()
    print(labels)
    print()
    """

    return sentences_splited, labels


"""
分词的部分直接放在读入的时候处理了，那这一段也没啥用了
def split_text(text_data):
 
    将原始文本分词
    例如：输入['今天星期四', '明天有雨'],
             返回[['今天‘，‘星期四’], ['明天','有‘，‘雨']]
            
    或者例如：输入['I don't want to go', ''Who are you?’],
            返回[['I', 'don't', 'want', 'to', 'go',],['Who', ' are', 'you',' ?']]
        中文推荐jieba分词(请pip install jieba)，英文直接用空格切分句子即可
    :param text_data:
    :return:

"""


def make_dict(sentences1,sentences2,sentences3):
    
    #统一语料库

    #合成超长列表
    all_list = []
    for i in range(len(sentences1)):
        all_list += sentences1[i]
    for i in range(len(sentences2)):
        all_list += sentences2[i]
    for i in range(len(sentences3)):
        all_list += sentences3[i]
        
    word_number = len(all_list)
        
    #然后统计每一个词出现的频率
    word_count = dict()

    for i in range(len(all_list)):
        word = all_list[i]
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1
            
    """
    tf_idf专属
    """
    #统计每个分词在多少行中出现过以及一共有多少行
    file_number = len(sentences1) + len(sentences2) + len(sentences3)
    word_contain_file = dict()
    for i in range(len(sentences1)):
        words = set(sentences1[i])
        for j in words:
            if j in word_contain_file:
                word_contain_file[j] += 1
            else:
                word_contain_file[j] = 1
    for i in range(len(sentences2)):
        words = set(sentences2[i])
        for j in words:
            if j in word_contain_file:
                word_contain_file[j] += 1
            else:
                word_contain_file[j] = 1
    for i in range(len(sentences3)):
        words = set(sentences3[i])
        for j in words:
            if j in word_contain_file:
                word_contain_file[j] += 1
            else:
                word_contain_file[j] = 1

    #print(file_number)
    
        
            
    #这样所有词语都在这个列表all_list里面，然后进行编号，利用一个类似hash的方法进行映射
    #遍历每个词语，如果他在前面出现了，就跳过，否则，就给他一个递增的编号
    #这里需要用到python 的dict，每一个key对应一个元素
    #可以以O(1)的方法查找一个元素key对应的value
    #具体dict的用法可以自行学习
    word_to_id = dict()
    for i in range(len(all_list)):
        # 得到一个词语
        word = all_list[i]
        # 查看word是否在word_to_id这个字典中出现
        if word in word_to_id:
            continue
        #这一行的作用是过滤低频单词，
        #如果word的频率小于最低频率，就忽略掉这个单词
        if word_count[word] < min_freq:
            continue
        #没有出现，那么给他一个id,假设前面已经有若干个词语["我"，"不能"，"是"]
        # 被编码为[0, 1, 2],即：{'我':0, '不能':1,'是':2}
        # 那么就给word编码为3，正好等于word_to_id的长度e
        word_index = len(word_to_id)
        word_to_id[word] = word_index
    
    return word_to_id, word_count, word_number , word_contain_file, file_number
        
def vectorizer(sentences, word_to_id, word_count, word_number, word_contain_file, file_number):
    """
    将原始文本转化为向量
    可选方法
    1. one hot 方法, 2. tf-idf方法，3. 词向量或者其他方法
    推荐使用1或者2的方法，两种方法都可以选择调用第三方包或者自己实现
    可用的包：
    CountVectorizer, TfidfVectorizer可以实现one-hot和tfd-idf编码
    使用tf-idf比onehot有加分; 自己实现比调用第三方包有额外加分
    愿意使用词向量也可
    返回示例：[[0,0,1,2], [2,3,3,4]]
                   [[0,0,1,2], [2,3,3,4]]
                    [[0,0,1,2], [2,3,3,4]]
    分别对应train, valid, test的向量化结果，每一个结果都是一个二维的list, 每一个元素都是int or float
    :param text:  一个list, 每个元素是一句话
    :return: 3个二维list
    """

    #得到每一个单词对应的编号，就可以对句子进行编码
    #首先我们知道每一个句子对应的向量长度等于词表的大小
    #所以先初始化一个全0的向量
    """
    onehot_result = []
    for i in range(len(sentences)):
        sentence = sentences[i]
        vector = [0 for i in range(len(word_to_id))]
        for j in range(len(sentence)):
            word = sentence[j]
            if word_count[word] < min_freq:
                continue
            idx = word_to_id[word]
            vector[idx] += 1
        onehot_result.append(vector)

    return onehot_result
    """
    
    """
    tf_idf方法
    """
    tf_idf_result = []
    for i in range(len(sentences)):
        sentence = sentences[i]
        tf = [0 for i in range(len(word_to_id))]
        idf = [0 for i in range(len(word_to_id))]
        tf_idf = [0 for i in range(len(word_to_id))]
        for j in range(len(sentence)):
            word = sentence[j]
            if word_count[word] < min_freq:
                continue
            idx = word_to_id[word]
            tf[idx] = word_count[word] / word_number
            idf[idx] = math.log(file_number/(word_contain_file[word] + 1), 10)
            tf_idf[idx] = tf[idx] * idf[idx]
        tf_idf_result.append(tf_idf)

    return tf_idf_result
    


def train_model(train_data, train_label, valid_data, valid_label):
    """
    开始训练模型并使用验证集验证效果
    推荐方法
    1. 朴素贝叶斯: 可用包 BernoulliNB,
    2. LogisticRegression 可用包 sklearn中的LogisticsRegression
    3. 其他方法不做强制性要求
    以上方法，自己实现比调包加分，手动实现 LR比手动实现朴素贝叶斯加分
    调包示例：
        model = one_model()
        model.some_func(train_data, train_label)
        score = model.score_function(valid_data, valid_label)
        print("valid accuracy score is {:.4f}".format(score}
        
        
        以上只计算了accuracy score，如果能打印验证集precision_score, recall_score, F1_score， 加分
        可以调用 sklearn.metric 中的precision_score, recall_score, F1_score
        请试着调节模型的参数，将你的各项score尽量提高，验证集分数越高，测试集的效果也可能越好
        也推荐同学们尝试交叉验证方法，提升模型的泛化能力
        最终返回训练完成的模型 model
    :param train_data:
    :param train_label:
    :param valid_data:
    :param valid_label:
    :return:
    """
    #定义模型
    model = LogisticRegression(penalty = 'l1', tol = 1e-5, C = 0.9)
    #开始训练,使用训练集的train_x 和train_y
    model.fit(train_data, train_label)
    #训练完毕，预测一下验证集
    prediction = model.predict(valid_data)
    #评估一下真正的结果和预测的结果的差异
    score_accuracy = accuracy_score(valid_label, prediction)
    score_recall = metrics.recall_score(valid_label, prediction)
    score_F1 = metrics.f1_score(valid_label, prediction)
    score_fbeta = metrics.fbeta_score(valid_label,prediction, beta = 0.5)
    #打印预测的结果和得分
    print(prediction)
    print("accuracy score: {:.4f}".format(score_accuracy))
    print("recal score:    {:.4f}".format(score_recall))
    print("F1 score:       {:.4f}".format(score_F1))
    print("fbeta score:    {:.4f}".format(score_fbeta))
    
    return model

def predict(model, test_data,test_id):
    """
    使用训练好的模型预测测试数据
    返回预测的标签，为list
    :param model:
    :param test_data:
    :return:
    """
    
    #使用训练好的模型训练，得到预测结果
    result = model.predict(test_data)
    #打印预测结果
    print("test result", result)
    #将结果和id写入文件夹中
    
    with open("final_test_data/submit.txt", "w", encoding='utf-8') as f:
    #with open("work_data/submit.txt", "w", encoding='gbk') as f:
        f.write("id,labels\n")
        for i in range(len(result)):
            idx = str(test_id[i])
            lable = str(result[i])
            f.write(idx + '\t' + lable + '\n')



def run_step():
    """
        选择相应的任务和文件
        读文件，train_data, train_label = some_function(filename='')
                    valid_data, validlabel = some_function(filename='')
                   test_data, test_ids = some_function(filename='')
        将原始文本分词：
                  train_data = split_function(train_data)
                  valid_data = split_function(valid_data)
                  test_data = split_function(test_data)
        将分词后的文本变成向量：
                  train_vec, valid_vec, test_vec = vectorizer(train_data, valid_data, test_data)
        开始训练模型：
                model = train_function(train_vec, train_label, valid_vec, valid_label)
        开始预测结果：
                 test_result = predict(mode, test_data)
        写入文件：
                将test和对应的test写入test_result, 结果样本如submit所示
        请大家尽量按照步骤来，顺利完成整个流程。有余力的同学可以试试提高预测的精度
    :return:
    """
    """
    train_sentences, train_labels = read_train_valid(filename = 'work_data/training.txt')
    valid_sentences, valid_labels = read_train_valid(filename = 'work_data/validation.txt')
    test_sentences, test_ids = read_test(filename = 'work_data/test.txt')
    
    """
    train_sentences, train_labels = read_train_valid(filename = 'final_test_data/training.txt')
    valid_sentences, valid_labels = read_train_valid(filename = 'final_test_data/validation.txt')
    test_sentences, test_ids = read_test(filename = 'final_test_data/test.txt')
    
    
    
    word_to_id_list, word_count, word_number, word_contain_file, file_number = make_dict(train_sentences, valid_sentences, test_sentences)
   
    train_vec = vectorizer(train_sentences, word_to_id_list, word_count, word_number, word_contain_file, file_number)
    valid_vec = vectorizer(valid_sentences, word_to_id_list, word_count, word_number, word_contain_file, file_number)
    test_vec = vectorizer(test_sentences, word_to_id_list, word_count, word_number, word_contain_file, file_number)
    train_vec = np.array(train_vec)
    valid_vec = np.array(valid_vec)
    test_vec = np.array(test_vec)
   
    """
    print(train_vec)
    print(train_labels)
    print()
    print(valid_vec)
    print(valid_labels)
    print()
    print(test_vec)
    print(test_ids)
    print('\n')
    """
    
    
    # 开始训练模型，使用train_x, train_y训练，valid_x, valid_y验证
    model = train_model(train_vec, train_labels, valid_vec, valid_labels)
    
    predict(model,test_vec,test_ids)
    

    
if __name__ == '__main__':
    run_step()
