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


df = pd.read_csv('all_variables_with_arguments.csv')

print df

#filter our the variables with length 1 and type char
df = df[((df['varlength']) == 1)]  

#count the number of unique projects in which a varname occurs plus their datatype

pivot = pd.pivot_table(df, values='projectid', index=['varname','datatype'], aggfunc=lambda x: len(x.unique()))

print pivot

pivot.to_csv('distributions of datatype of one letter chars.csv')

#sorting does not work due to a key error WHYYYYY?!
#pivotsorted = pivot.sort_values(by='varlength', ascending=False)
#pivotsorted.to_csv('distributions of lengths_sorted.csv')




pivot.plot.bar(alpha=0.5)





