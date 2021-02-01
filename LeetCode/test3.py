# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 16:14:09 2021

@author: qzh
"""

class Solution:
    def checkIPs(self , rules , ips ):
        filt = []
        for rule in rules:
            temp = []
            if rule[0] == 'a':
                ip = rule[6:]
                temp.append('allow')
            else:
                ip = rule[5:]
                temp.append('deny')
                
            ip = ip.split('/')
            ip[0] = ip[0].split('.')
            num = int(ip[0][0]) << 24 + int(ip[0][1]) << 16 + int(ip[0][2]) << 8 + int(ip[0][3])
            
            fix = 32
            if len(ip) > 1:
                fix = int(ip[1])
            num = num - num % (1 << (32 - fix))
            temp.append(num)
            temp.append(fix)
            filt.append(temp)
        
        result = []
        for ip in ips:
            ip = ip.split('.')
            num = int(ip[0]) << 24 + int(ip[1]) << 16 + int(ip[2]) << 8 + int(ip[3])
            flag = 0
            for i in range(len(filt)):
                if num - num % (1 << (32 - fix)) == filt[i][1]:
                    result.append(filt[i][0])
                    flag = 1
            if flag == 0 :
                result.append('allow')
        return result
                
solution = Solution()
print(solution.checkIPs(["allow 1.2.3.4/30","deny 1.1.1.1","allow 127.0.0.1","allow 123.234.12.23/3","deny 0.0.0.0/0"],["1.2.3.4","1.2.3.5","1.1.1.1"]))