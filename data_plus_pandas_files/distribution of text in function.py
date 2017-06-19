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


df = pd.read_csv('output/all text arguments trimmed.csv')



#count the number of unique projects in which a length occures

pivot = pd.pivot_table(df, values='projectid', index='textArguments', aggfunc=lambda x: len(x.unique()))
pivot = pivot.sort_values(by=('projectid'), ascending=False)

print pivot

pivot.to_csv('output/distributions of text arguments.csv')

pivot = pivot[(pivot['projectid'] > 200)]

pivot.plot.bar(alpha=0.5)







