# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math

def isLetter(c):
  funcname = c['varname']
  return funcname.isalpha()

def mergeNameType(c):
  varname = c['varname']
  datatype = c['datatype']
  return varname + "---" + datatype


df = pd.read_csv('output/distributions of datatype of one letter chars.csv')


#count the number of unique projects in which a varname occurs plus their datatype
 
pivot = pd.pivot_table(df, values='projectid', index=['Namelower'], columns=['Type'], aggfunc='sum')
 
print pivot
 

 
pivot.plot(kind='bar', stacked=True)










