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
  total = 2023753
  return occurrences/total




df = pd.read_csv('output/distributions of lengths of functions_percentage_20plus.csv', nrows = 20)

print df

percentages = df['percentage']

percentages.plot.bar(alpha=0.5)

ax = df.A.plot(xticks=df.index, rot=90)
ax.set_xticklabels(df['varlength'])
