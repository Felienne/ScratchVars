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


df = pd.read_csv('output/all_variables_with_arguments.csv')

print df

#filter our the variables with length 1 and type char
df = df[((df['varlength']) == 1)  & (df['vartype'] == 'char') ]  

#now add whether a name is a letter
df['isLetter'] = df.apply(isLetter, axis=1)

#and filter on it 
df = df[(df['isLetter'] == True) ]

# now and a new field for name plus datatype (so we count double occurrences double) 
#and filter on it 
df['mergeNameType'] = df.apply(mergeNameType, axis=1)










