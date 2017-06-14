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

def length(c):
  return len(str(c['name']))

def lowerfunctionname(c):
  return str(c['name']).lower()

def isLetter(c):
  funcname = c['functionname']
  return funcname.isalpha()
 


df = pd.read_csv('output/all_functions.csv')

df['varlength'] = df.apply(length, axis=1)
df.to_csv('output/all_functions.csv')
df['functionname'] = df.apply(lowerfunctionname, axis=1)

#filter the variables with length 1 
df = df[(df['varlength'] == 1) ]

#now add whether a name is a letter
df['isLetter'] = df.apply(isLetter, axis=1)

#and filter on it 
df = df[(df['isLetter'] == True) ]


pivot = pd.pivot_table(df, values='projectid', index='functionname', aggfunc=lambda x: len(x.unique()))
#sorting does not work due to a key error WHYYYYY?!
#pivot = pivot.sort_values(by='functionname', ascending=False)


print pivot

pivot.to_csv('output/distributions of one letter functions.csv')



#pivotsorted.to_csv('distributions of lengths_sorted.csv')




pivot.plot.bar(alpha=0.5)





