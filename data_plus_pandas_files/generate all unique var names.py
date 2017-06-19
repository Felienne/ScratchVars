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

def numSpace(c):
  varname = str(c['varname'])
  return varname.count(' ')

df = pd.read_csv('output/all_variables_with_arguments.csv')



df = df.drop_duplicates(subset='varname')


print df


df.to_csv('output/all_unique_variables_with_arguments.csv')



pivot = df.pivot_table(df, values='varname', index='number_of_spaces', aggfunc='count')

print pivot

pivot.plot.bar(alpha=0.5)



pivot.to_csv('output/distributions of spaces for unique names.csv')









