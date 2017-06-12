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

def RepresentsNumber(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False
    
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


def varname(c):
  if c[7] == 'deleteLine:ofList:':
    return c[9] 
  elif c[7] == 'getLine:ofList:' :
    if str(c[9]) == "nan":
      return c[8]
    else:
      return c[9]
  elif c[7] == 'append:toList:' :
    if str(c[9]) == "nan":
      return c[8]
    else:
      return c[9] 
  elif c[7] == 'setLine:ofList:to:' :
    if str(c[9]) == "nan":
      return c[8]
    else:      
      if RepresentsNumber(c[9]) == True:
        return c[8]
      else:
        return c[9]
  elif c[7] == 'deleteLine:toList:' :
    if str(c[9]) == "nan":
      return c[8]
    else:
      return c[9]      
  elif c[7] == 'insert:at:ofList:':
    if str(c[10]) == "nan":
      return c[9]
    else:
      return c[10]
  else:
    return c[8]

def lowervarname(c):
  return str(varname(c)).lower()

def getid(c):
  return c[0]

def length(c):
  return len(str(c['varname']))

def type(c):
  if c[7] == 'deleteLine:ofList:':
    return 'list'
  elif c[7] == 'getLine:ofList:' :
    return 'list'
  elif c[7] == 'append:toList:' :
    return 'list'
  elif c[7] == 'setLine:ofList:to:' :
    return 'list'
  elif c[7] == 'deleteLine:toList:' :
    return 'list'     
  elif c[7] == 'insert:at:ofList:':
    return 'list'
  else:
    if (RepresentsInt(c['argument']) == True):
      return 'int'
    elif (RepresentsNumber(c['argument']) == True):
      return 'float'
    elif len(c['argument']) == 1:
      return 'char'  
    else:
      return 'string'
  
# niet echt heel mooi deze code maar isnan geeft soms een fout zelf als ik eerst 
# representsnumber doe!
# op regel 570 van no_head. Kan ik nig eens uitzoeken maar ga ik vast
# nooit doen


def argument(c):
  try: 
    if math.isnan(c[9]):
      return "---"
    else:
      return c[9]
  except TypeError:
    return c[9]

def vartype(c):
  varname = c['varname']
      
  if (RepresentsInt(varname) == True):
    return 'int'
  elif (RepresentsNumber(varname) == True):
    return 'float'
  elif len(varname) == 1:
    return 'char'  
  else:
    return 'string'
    
def hasSpace(c):
  varname = c['varname']
  return (' ' in varname)      

def numSpace(c):
  varname = c['varname']
  return varname.count(' ')

u = pd.read_csv('all_variables_with_arguments.csv')

u = u[((u['vartype']) == 'char')]  


u.to_csv('all_one_letter_variables_with_arguments.csv')







