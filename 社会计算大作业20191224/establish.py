import read_data

#实现对话题的统计
def topic_sift(labels):
    #话题域以及话题域的个数
    topic_types = []
    topic_types_number = 0
    #遍历标签
    for i in range(len(labels)):
        #第一个话题或者相邻两个分句话题不同时建立新话题
        if (i == 0) or (i > 0 and labels[i] != labels[i - 1]) :
            #新话题的建立
            topic_types.append(labels[i])
            topic_types_number += 1
    
    return topic_types, topic_types_number

#实现分词表重分类
def list_re_classification(lists, labels):
    #最终建立的与话题域对应的分词表
    final_lists = []
    #类指针
    topic_point = 0
    
    for i in range(len(labels)):
        if (i == 0) or (i > 0 and labels[i] != labels[i - 1]) :
            #如果两个相邻分词行属于同一个话题域，那么就延展该话题域
            #此处用+=是在同一行后面延伸
            final_lists.append(lists[i])
            topic_point += 1
        else:
            #如果两个相邻分词行不属于同一个话题域，那么就新建话题域
            #此处用append，是在list中新加一行列表元素
            final_lists[topic_point - 1] = final_lists[topic_point - 1] + lists[i]
    
    return final_lists

def establish_topic(list1, labels1, list2, labels2):
    topic_types, topic_types_number = topic_sift(labels1)
    final_list1 = list_re_classification(list1, labels1)
    final_list2 = list_re_classification(list2, labels2)
    return topic_types, topic_types_number, final_list1, final_list2

if __name__ == '__main__':
    train_words, train_labels = read_data.read_data_from_dir(filename = 'data/train')
    develop_words, develop_labels = read_data.read_data_from_dir(filename = 'data/develop')
    
    #建立话题域
    topic_types, topic_types_number, train_topic_list, develop_topic_list = establish_topic(train_words, train_labels, develop_words, develop_labels)