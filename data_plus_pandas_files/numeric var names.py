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

df = df[(df['vartype'] == 'int') | (df['vartype'] == 'float')]


df = df[(df['varname'] != '+1')]


df.to_csv('output/all numeric variables.csv')


pivot = pd.pivot_table(df, values='projectid', index='varname', aggfunc=lambda x: len(x.unique()))
pivot = pivot.sort_values(by=('projectid'), ascending=False)


print pivot

pivot.to_csv('output/distribution of numeric variables.csv')

pivot = pivot[(pivot['projectid'] > 30)]


pivot.plot.bar(alpha=0.5)




