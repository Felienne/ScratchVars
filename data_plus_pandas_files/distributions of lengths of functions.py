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

#yes magic number sorry! rush job.
# sorry future self
# is obtained by summing column B of distributions of lengths of functions_percentage
def getPercentage(c):
  occurrences = float(c['projectid'])
  total = 549425
  return (occurrences/total)*100


df = pd.read_csv('output/all_functions.csv')


print df

#count the number of unique projects in which a length occures

pivot = pd.pivot_table(df, values='projectid', index='varlength', aggfunc='count')
pivot['percentage'] = pivot.apply(getPercentage, axis=1)

pivot.to_csv('output/distributions of lengths of functions_percentage.csv')

dfpivot = pd.read_csv('output/distributions of lengths of functions_percentage.csv')


print dfpivot





