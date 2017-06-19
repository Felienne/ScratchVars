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

def getPercentage(c):
  occurrences = float(c['projectid'])
  total = 190083
  return (occurrences/total)*100




df = pd.read_csv('output/all_variables_with_arguments.csv')


print df

#count the number of unique projects in which a length occures

pivot = pd.pivot_table(df, values='projectid', index='varlength', aggfunc=lambda x: len(x.unique()))
pivot['percentage'] = pivot.apply(getPercentage, axis=1)

pivot.to_csv('output/distributions of lengths_percentage.csv')




print dfpivot




