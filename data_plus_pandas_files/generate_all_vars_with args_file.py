# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
import os 

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

def getvarname(c):
  return str(varname(c))
  #return str(varname(c)).lower()

def firstCharisLetter(c):
  varname = c['varname']
  
  if len(varname) == 0:
    return false
  else:
    return str(varname[0]).isalpha()

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
    if varname.isalpha():
      return 'char'  
    else:
      return 'symbol'
  else:
    return 'string'
    
def hasSpace(c):
  varname = c['varname']
  return (' ' in varname)      

def numSpace(c):
  varname = c['varname']
  return varname.count(' ')


matplotlib.style.use('ggplot')


dir_path = os.path.dirname(os.path.realpath(__file__))

df = pd.read_csv(dir_path+'/input/code.csv', names = list(range(0,23)))#, nrows = 1000)

datablocks = ['readVariable','contentsOfList:','lineCountOfList:','setVar:to:','list:contains:','showList:','hideVariable:','showVariable:','changeVar:by:','hideList:', 'getLine:ofList:', 'append:toList:', 'deleteLine:ofList:', 'setLine:ofList:to:', 'insert:at:ofList:']

#
s = df[(df[7] == datablocks[0]) | (df[7] == datablocks[1])  | (df[7] == datablocks[2]) | (df[7] == datablocks[3])  | (df[7] == datablocks[4]) | (df[7] == datablocks[5])  | (df[7] == datablocks[6]) | (df[7] == datablocks[7]) | (df[7] == datablocks[8])  | (df[7] == datablocks[9]) | (df[7] == datablocks[10])  | (df[7] == datablocks[11]) | (df[7] == datablocks[12])  | (df[7] == datablocks[13]) ] #get all rows that have a data related block

# not sure why, something with bool types but the line below does not work :()
#s = df[(df[7] == x for x in datablocks) ]

# get the correct variable names (not always in column 8 for some blocks it is further)
s['varname'] = s.apply(getvarname, axis=1)

# also obtain the argument to analyze the datatype
s['argument'] = s.apply(argument, axis=1)

s = s[(s['argument']) != '---']

# now save the argiment and varname for subsequent processing
t = s.loc[:,['varname', 'argument', 0, 7]]


t['varlength'] = t.apply(length, axis=1)
t['datatype'] = t.apply(type, axis=1)
t['vartype'] = t.apply(vartype, axis=1)
t['projectid'] = t[0]
t['number_of_spaces'] = t.apply(numSpace, axis=1)
t['firstCharisLetter'] = t.apply(firstCharisLetter, axis=1)



u = t.loc[:,['varname', 'number_of_spaces', 'firstCharisLetter', 'argument', 'varlength', 'datatype', 'vartype', 'projectid']]

u.to_csv(dir_path+'/output/all_variables_with_arguments.csv')






