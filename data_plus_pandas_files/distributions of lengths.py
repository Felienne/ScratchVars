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


df = pd.read_csv('output/all_variables_with_arguments.csv')

print df

#count the number of unique projects in which a length occures

pivot = pd.pivot_table(df, values='projectid', index='varlength', aggfunc=lambda x: len(x.unique()))


pivot.to_csv('output/distributions of lengths.csv')

dfpivot = pd.read_csv('output/distributions of lengths.csv')
print dfpivot


#sorting only works when first saving... otherwise we get a key error

dfpivot = dfpivot.sort_values(by='varlength', ascending=True)
dfpivot.to_csv('distributions of lengths_sorted.csv')

#plot only under 20
dfpivot = dfpivot[dfpivot['varlength'] <= 21]
dfpivot.plot.bar(alpha=0.5)
dfpivot.ylabel(list(range(1,20)))




