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

df = df[(df['number_of_spaces'] > 0) & (df['number_of_spaces'] < 7)]


#count the number of unique projects in which a length occures

pivot = pd.pivot_table(df, values='projectid', index='number_of_spaces', aggfunc=lambda x: len(x.unique()))

print pivot

pivot.to_csv('output/distributions of spaces.csv')



pivot.plot.bar(alpha=0.5)







