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


df = pd.read_csv('output/distributions of one letter chars_upper and lower.csv')


df.plot(kind='bar', stacked=True)





