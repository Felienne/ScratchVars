# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
import os 


def getname(c):
  procArgument = c[8]
  locFirstPercentage = procArgument.find('%')
  if locFirstPercentage == -1:
    return procArgument
  else:
    return procArgument[:locFirstPercentage-1]

def getArguments(c):
  procArgument = c[8]
  locFirstPercentage = procArgument.find('%')
  
  if locFirstPercentage == -1:
    return []
  else:
    remainingText = procArgument[locFirstPercentage:]
    return remainingText.split(' ')
  
def getTextArguments(c):
  arguments = c['allArguments']
  if arguments == [] or not isinstance(arguments, list):
    return []
  else:
    return [x for x in arguments if (x != "" and x[0] != '%')]

def getDefaultArguments(c):
  arguments = c['allArguments']
  if arguments == [] or not isinstance(arguments, list):
    return []
  else:
    return [x for x in arguments if (x != "" and x[0] == '%')]

dir_path = os.path.dirname(os.path.realpath(__file__))

df = pd.read_csv(dir_path+'/input/code.csv', names = list(range(0,23)))#, nrows = 20000)


s = df[(df[7] == 'procDef') | (df[7] == 'call')] #get all rows that have procedure blocks

# now save the block and block and varname for subsequent processing

s['projectid'] = s.loc[:,[0]]
s['procedure'] = s.loc[:,[7]]
s['procedure_Argument'] = s.loc[:,[8]]
s['name'] =  s.apply(getname, axis=1)
s['allArguments'] =  s.apply(getArguments, axis=1)


s = s.loc[:,['projectid', 'procedure', 'procedure_Argument', 'name','allArguments']]

# now split the arguments in the default ones (empty holes) and text labels in between
s['defaultArguments'] =  s.apply(getDefaultArguments, axis=1)
s['textArguments'] =  s.apply(getTextArguments, axis=1)


s.to_csv(dir_path+'/output/all_functions.csv')








