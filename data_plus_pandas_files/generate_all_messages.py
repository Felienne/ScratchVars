# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math

def hasSpace(c):
  varname = c['varname']
  return (' ' in varname)      

def numSpace(c):
  varname = c['varname']
  return varname.count(' ')


df = pd.read_csv('input/code.csv', names = list(range(0,23)))#, nrows = 1000)


s = df[(df[7] == 'broadcast:') | (df[7] == 'whenIReceive')] #get all rows that have procedure blocks

# now save the block and block and message name for subsequent processing

s['projectid'] = s.loc[:,[0]]
s['messagename'] = s.loc[:,[8]]
s['number_of_spaces'] = s.apply(numSpace, axis=1)


s = s.loc[:,['projectid', 'messagename', 'number_of_spaces']]


s.to_csv('output/all_messages.csv')








