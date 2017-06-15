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


df = pd.read_csv('output/all_variables_with_arguments.csv')

print df

#filter our the variables with length 1 and type char
df = df[((df['varlength']) == 1)  & (df['vartype'] == 'char') ]  

#now add whether a name is a letter
df['isLetter'] = df.apply(isLetter, axis=1)

#and filter on it 
df = df[(df['isLetter'] == True) ]

#count the number of unique projects in which a varname occurs plus their datatype

pivot = pd.pivot_table(df, values='projectid', index=['varname'], columns=['datatype'], aggfunc=lambda x: len(x.unique()))

print pivot

pivot.to_csv('output/distributions of datatype of one letter chars.csv')

pivot.plot(kind='bar', stacked=True)










