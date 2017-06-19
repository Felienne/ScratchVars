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

pivot = pd.pivot_table(df, values='number_of_spaces', index='projectid', aggfunc='max')



pivot.to_csv('output/maximal_number_of_spaces_per_project.csv')

maxspaces = pd.read_csv('output/maximal_number_of_spaces_per_project.csv')


#count the number of unique projects in which a length occures

maxspacespivot = pd.pivot_table(maxspaces, values='projectid', index='number_of_spaces', aggfunc='count')

print maxspacespivot

maxspacespivot.to_csv('output/maximal_number_of_spaces_per_project_pivot.csv')

maxspacespivot.plot.bar(alpha=0.5)







