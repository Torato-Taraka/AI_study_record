# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:29:02 2020

@author: 10541
"""

import random

for i in range(10):
    x = random.randint(0,1000000)
    if (x / 10000 < 0.5):
        print("SP")
    else:
        if (x / 10000 < 2.0):
            print("SSR")
        else:
            if (x / 10000 < 10):
                print("SR")
            else:
                if (x / 10000 < 50):
                    print("R")
                else:
                    print("N")

