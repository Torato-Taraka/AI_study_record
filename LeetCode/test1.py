# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 15:24:03 2021

@author: qzh
"""

class Solution:
    def checkToken(self , seed , token , req ):
        dic = {}
        for i in seed:
            dic[i] = 0
        print(dic)
        if (len(req) % len(seed) != 0):
            return False
        for i in range(len(token)):
            if token[i] != '?' and token[i] != req[i]:
                return False
        N = len(req) // len(seed)
        for i in req:
            if i in seed:
                dic[i] += 1
                if dic[i] > N :
                    return False
            else:
                return False
        return True
        
solution = Solution()
print(solution.checkToken("abc","a??bbcabc","aacbbcabc"))
print(solution.checkToken("abc","a??bbcabc","aaabbcabc"))
print(solution.checkToken("abc","a??bbcabc","acdbbcabc"))
print(solution.checkToken("abc","a??bbcabc","aacbbca"))
print(solution.checkToken("abc","a??bbcabc","acabbcabc"))
print(solution.checkToken("abc","a??bbcabc","aaccbcabc"))