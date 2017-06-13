from conf import *
import subprocess
import re
import json
import pprint
import pdb

def get_name():
    return 'php'

def can_extract(file_name): 
    return file_name.endswith(".php")

def parseVars(y):
    out = {}
    vars = []
    print('fff')
    
    def checkForName(x, name,isPotentialVar):
    
        if not isPotentialVar:
            return 
        if name == "name":
            
            vars.append(x)
    
    
    def checkForVar(x,name):
        # print('x is %s' % str(x))
        # print('x is %s' % x)
        # print('name is %s' % name)
        if (name == 'consts'):
            return True
        if (name == 'var'):
            return True
        if (name == 'vars'):
            return True
        if (name == 'params'):
            print 'found params'
            print  x
            return True
            
        return False
             
    
    def parser(x, name='',isPotentialVar = False):
        
        checkForName(x,name,isPotentialVar)
        isPotentialVar = checkForVar(x,name)
        if type(x) is dict:
            for a in x:
                parser(x[a], a,isPotentialVar)
        elif type(x) is list or type(x) is tuple:
            i = 0
            for a in x:
                
                parser(a, a,isPotentialVar)
                i += 1
        else:
            checkForName(x,name,isPotentialVar)        

    parser(y)
    return vars
def extract_names(file_name):

    #Running PHP_SCRIPT to get an AST
    ast = subprocess.check_output([PHP_PATH,PHP_AST_PATH, file_name])
    
    try:
        data = json.loads(ast)
        #pdb.set_trace()
        
        vars = parseVars(data)
        
    except ValueError:  # includes simplejson.decoder.JSONDecodeError
        print 'Decoding JSON has failed'
    except Exception as e:
        print e.__doc__
        print e.message
    
    
    #Parsing the given AST to get the variable declarations
    variables = []
    for v in vars:
        
        
        #Adding the name of the variable and its type
        variables.append((v,"unknown"))
    
    return variables

