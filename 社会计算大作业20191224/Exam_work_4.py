import read_data
import establish
import word2vec
import train_model

def run_step():
    #读取文件数据
    train_words, train_labels = read_data.read_data_from_dir(filename = 'data/train')
    develop_words, develop_labels = read_data.read_data_from_dir(filename = 'data/develop')
    test_words, test_words_origin = read_data.read_test(filename = 'data/test')
    
    #建立话题域
    topic_types, topic_types_number, train_topic_list, develop_topic_list = establish.establish_topic(train_words, train_labels, develop_words, develop_labels)
    
    #向量化
    train_vec, develop_vec, test_vec, topic_word_weight = word2vec.word_to_vec(train_topic_list, develop_topic_list, test_words, train_words, develop_words)
    
    #开始训练模型
    train_model.start(train_vec, train_labels, develop_vec, develop_labels, topic_types_number, topic_word_weight, topic_types)

    #使用模型，进行预测
    predict_domain = train_model.predict(test_vec, topic_types_number, topic_word_weight, topic_types)
    
    with open('data/submit.txt', 'w', encoding = 'utf-8-sig') as file:
        for i in range(len(predict_domain)):
            file.write(predict_domain[i] + '\t' + test_words_origin[i] + '\n')
    
if __name__ == '__main__':
    run_step()
