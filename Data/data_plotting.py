#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:31:02 2019

@author: >Kang Liu
"""

import os 
import numpy as np
import matplotlib.pyplot as plt


filename ='clogging/width_change/CloggingLog_inifile_clogging_w_2.txt'
figname = filename + ".png"



data = np.loadtxt(filename)    



t = data[:,1]  


n = data[:,2]  

plt.plot(t,n)


plt.xlabel('Time in (s) ')
plt.ylabel('Clogging_occurrence',rotation=90)
print(figname)

plt.savefig(figname)



