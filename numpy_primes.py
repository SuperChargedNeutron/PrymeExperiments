# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 19:01:12 2019

@author: cesar
"""

import numpy as np

def isprime(lb, ub, num):

    ubsq = int((np.sqrt(ub)))

    divd_array = list(range(2, ubsq+1))
    primedivlist = divd_array[:]

    for divv in range(2, int(np.sqrt(ubsq))):
        for nummm in primedivlist:
            if nummm%divv == 0 and divv != nummm:
                primedivlist.remove(nummm)

    for i in primedivlist:
        if num%i != 0 and i != num:
            return True 
        else: 
            return False


lb = int(input('Choose your lower bound: '))
ub = int(input('Choose your upper bound: '))

# numpy makes array, list makes list, int prime list??
num_array = np.arange(lb, ub+1)
num_list = list(num_array)

primelist = []

for i in num_list:
    if isprime(lb, ub, i):
        primelist.append(i)

print(primelist)



