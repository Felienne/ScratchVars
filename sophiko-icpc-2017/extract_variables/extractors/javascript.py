from conf import *
import subprocess
import re

def get_name():
    return 'javascript'

def can_extract(file_name):
    return file_name.endswith(".js")

def extract_names(file_name):

    #Running the analyzer script to get the variable names
    variable_names = subprocess.check_output(['node', "extractors/analyze.js", file_name])
    
    #Parsing the given AST to get the variable declarations
    variables = []
    for var_name in variable_names.split('\n'):
        
        #Adding the name of the variable and its type
        variables.append((var_name, "unknown"))
    
    return variables

