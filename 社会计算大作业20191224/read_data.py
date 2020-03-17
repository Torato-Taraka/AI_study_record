import os
import words_cut

#该过程实现从train和develop文件夹中读取数据
#包括分类信息以及分词后的分句
def read_data_from_dir(filename):
    #记录分类信息的标签表
    labels = []
    #记录分句
    sentences_splited = []
    
    for root, dirs, files in os.walk(filename):
        for file in files:
            #print(file)
            #从文件名读取文件内语句的分类信息
            classification = os.path.splitext(file)[0].split('_')[1] 
            #content负责读取文件中所有的句子
            #读取train_app.txt的时候出现了一个问题
            #就是第一个句子前面出现了\ufeff这个东西
            #查询后得知是编码读取模式的问题
            content = open(root + '/' + file, 'r', encoding = 'utf-8-sig').read()
            #切分句子
            sentences = content.split('\n')
            
            for i in range(len(sentences)-1):
                #分词
                sentence = sentences[i]
                sentence = words_cut.cut_words(sentence)
                #print(sentence)
                #拓展分句
                sentences_splited.append(sentence)
                #拓展标签
                labels.append(classification)
        
    return sentences_splited, labels

#实现从test文件夹读取测试案例
#与上面的读取函数略有不同
def read_test(filename):
    #记录分句
    sentences_splited = []
    sentences_origin = []
    
    for root, dirs, files in os.walk(filename):
        for file in files:
            #content负责读取文件中所有的句子
            content = open(root + '/' + file, 'r', encoding = 'utf-8').read()
            #切分句子
            sentences = content.split('\n')
            sentences_origin += sentences
            
            for i in range(len(sentences)):
                #拓展分句
                sentence = sentences[i]
                sentence = words_cut.cut_words(sentence)
                sentences_splited.append(sentence)
            
    return sentences_splited, sentences_origin
 
if __name__ == '__main__' :       
    s, l = read_data_from_dir('data/train')
    a, b = read_test('data/test')
    print(len(l))
    print(len(b))
    