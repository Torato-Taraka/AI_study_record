# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 10:19:50 2021

@author: qzh
"""

import numpy as np

a = np.array([[[1,1,1],[2,2,2],[3,3,3]],[[2,2,2],[3,3,3],[4,4,4]],[[3,3,3],[4,4,4],[5,5,5]]])
for i in a:
    print(sum(i))