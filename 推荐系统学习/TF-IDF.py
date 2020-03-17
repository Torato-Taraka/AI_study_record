import numpy as np
import pandas as pd

wordA = "The cat is on my bed"
wordB = "The dog is on my kneel"

bowA = wordA.split(" ")
bowB = wordB.split(" ")

wordSet = set(bowA).union(set(bowB))
#print(wordSet)

#用统计字典来保存词出现的次数
wordDictA = dict.fromkeys(wordSet, 0)
wordDictB = dict.fromkeys(wordSet, 0)

#统计词频
for word in bowA:
    wordDictA[word] += 1
    
for word in bowB:
    wordDictB[word] += 1
    
pd.DataFrame([wordDictA, wordDictB], index = ['A', 'B'])

def computeTF( wordDict , bow ):
    tfDict = {}
    bowCount = len(bow)
    
    for word, number in wordDict.items():
        tfDict[word] = number / bowCount
        
    return tfDict 

def computeIDF( wordDictList ):
    idfDict = dict.fromkeys( wordDictList[0] , 0)
    N = len( wordDictList )
    
    import math
    
    for wordDict in wordDictList:
        for word, count in wordDict.items():
            if count > 0:
                idfDict[word] += 1
           
    for word, Ni in idfDict.items():
        idfDict[word] = math.log10( (N + 1) / (Ni + 1) )
    
    return idfDict

tfA = computeTF(wordDictA, bowA)
tfB = computeTF(wordDictB, bowB)
#print(tfA)

wordDictList = [wordDictA, wordDictB]
idf = computeIDF(wordDictList)
#print(idf)

def computeTFIDF(tf, idf):
    tf_idf = {}

    for word, count in tf.items():
        tf_idf[word] = count * idf[word]
    
    return tf_idf

tfidfA = computeTFIDF(tfA, idf)
tfidfB = computeTFIDF(tfB, idf)

pd.DataFrame([tfidfA, tfidfB], index = ['A', 'B'])