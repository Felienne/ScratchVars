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
 

#count the number of unique projects in which a varname occurs plus their datatype

pivot = pd.pivot_table(df, values='projectid', index='varname', aggfunc=lambda x: len(x.unique()))

print pivot

pivot.to_csv('output/distributions of vars over projects.csv')


pivot.plot.bar(alpha=0.5)





