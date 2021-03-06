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

#filter our the variables with length 1 and type char
df = df[(df['varlength'] == 1)  & (df['vartype'] == 'char')]

#count the number of unique projects in which a varname occurs

pivot = pd.pivot_table(df, values='projectid', index='varname', aggfunc=lambda x: len(x.unique()))

print pivot

pivot.to_csv('output/distributions of one letter chars.csv')

pivot.plot.bar(alpha=0.5)





