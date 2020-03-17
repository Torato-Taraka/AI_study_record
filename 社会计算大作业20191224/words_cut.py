import jieba

#完成分词以及对标点符号
#同时把话题中对应的一些单个的关键字作为语料拓展，使其能被分出
def cut_words(sentence):
    #读入停用词表
    content = open('data/stop_words.txt', 'r', encoding = 'utf-8').read()
    stop_words = content.split('\n')
    #print(stop_words)
    
    #读入关键字表
    content = open('data/key_words.txt', 'r', encoding = 'utf-8').read()
    topic_single_words = content.split('\n')
    #print(topic_single_words)
    
    #初步分词
    words_initial_list = jieba.lcut_for_search(sentence)
    
    #过滤停用词
    sentence_after_cut = []
    for word in words_initial_list:
        if word not in stop_words:
            sentence_after_cut.append(word)
            
    #分出单字关键词
    for i in range(len(sentence)):
        if sentence[i] in topic_single_words:
            #为了防止分过了再分一次
            if sentence[i] not in sentence_after_cut:   
                sentence_after_cut.append(sentence[i])
    
    return sentence_after_cut
    
#print(cut_words(''))