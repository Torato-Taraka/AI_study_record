import read_data
import establish
import numpy as np
min_freq = 1

def make_list(list1, list2):
    word_count = []
    word_to_id = []
    #weight用来记录分词权重
    topic_word_weight = []
    #实际上，list1也就是分类后的分词表的行数即为分类数
    for i in range(len(list1)):
        #同一话题域合成一个列表
        all_list = list1[i] + list2[i]
        #计算该分类共有多少个分词
        total_numbers = len(all_list)
        #print(all_list)
        
        #统计每一个词出现的频率
        current_count = dict()
        for j in range(len(all_list)):
            word = all_list[j]
            if word in current_count:
                current_count[word] += 1
            else:
                current_count[word] = 1
        word_count.append(current_count)
        #print(word_count)
                
        #这样所有词语都在这个列表all_list里面，然后进行编号，利用一个类似hash的方法进行映射
        #遍历每个词语，如果他在前面出现了，就跳过，否则，就给他一个递增的编号
        current_word_to_id = dict()
        current_weight = []
        for i in range(len(all_list)):
            # 得到一个词语
            word = all_list[i]
            # 查看word是否在word_to_id这个字典中出现
            if word in current_word_to_id:
                continue
            #这一行的作用是过滤低频单词，
            #如果word的频率小于最低频率，就忽略掉这个单词
            if current_count[word] < min_freq:
                continue
            #没有出现，那么给他一个id,假设前面已经有若干个词语["我"，"不能"，"是"]
            # 被编码为[0, 1, 2],即：{'我':0, '不能':1,'是':2}
            # 那么就给word编码为3，正好等于word_to_id的长度e
            word_index = len(current_word_to_id)
            current_word_to_id[word] = word_index
            #对onehot进行隐含层处理
            weight = current_count[word] / np.sqrt(total_numbers)
            #weight = current_count[word] / total_numbers
            #weight = current_count[word] ** 2 / total_numbers
            current_weight.append(weight)
        word_to_id.append(current_word_to_id)
        topic_word_weight.append(current_weight)
        #print(word_to_id)
        #print(weight)
        
    return word_count, word_to_id, topic_word_weight

def vectorizer(listx, word_count, word_to_id):
    #最终期望形成的vector的规模应该是 分句数 * 分类数 * 分词数
    onehot_result = []
    #最外面一层循环是遍历每一个分句，计算对每一个分句的vector值
    for i in range(len(listx)):
        #current_result用来记录当前分类情况下的vector
        current_result = []
        #sentence读取当前的分句
        sentence = listx[i]
        #print(sentence)
        #实际上，word_count或者是word_to_id的行数，也是分类数
        for k in range(len(word_count)):
            #初始化向量
            vector = [0 for i in range(len(word_to_id[k]))]
            #最里面遍历分词
            for j in range(len(sentence)):
                word = sentence[j]
                #只有这个分词在分类表里有，才统计他
                if word in word_count[k]:
                    if word_count[k][word] < min_freq:
                        continue
                    idx = word_to_id[k][word]
                    vector[idx] += 1
            current_result.append(vector)
        onehot_result.append(current_result)

    return onehot_result

#_origin表示的是分类前的分词表
def word_to_vec(list1, list2, list3, list1_origin, list2_origin):
    #实现在同一话题域内建立词典
    #topic_word_weight表示一个分词在这个话题域中的重要程度
    word_count, word_to_id, topic_word_weight = make_list(list1, list2)
    #print(word_count, word_to_id)
    
    vec1 = vectorizer(list1_origin, word_count, word_to_id)
    vec2 = vectorizer(list2_origin, word_count, word_to_id)
    vec3 = vectorizer(list3, word_count, word_to_id)
    
    #print(vec1)
    #print(len(vec2))
    #print(vec3)
    #print(topic_word_weight)
    
    return vec1, vec2, vec3, topic_word_weight

if __name__ == '__main__':
    train_words, train_labels = read_data.read_data_from_dir(filename = 'data/train')
    develop_words, develop_labels = read_data.read_data_from_dir(filename = 'data/develop')
    test_words, test_words_origin = read_data.read_test(filename = 'data/test')
    
    #建立话题域
    topic_types, topic_types_number, train_topic_list, develop_topic_list = establish.establish_topic(train_words, train_labels, develop_words, develop_labels)
   
    
    #向量化
    train_vec, develop_vec, test_vec, topic_word_weight = word_to_vec(train_topic_list, develop_topic_list, test_words, train_words, develop_words)

    