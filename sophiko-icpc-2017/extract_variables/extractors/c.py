from conf import *
import subprocess
import re

def get_name():
    return 'c'

def can_extract(file_name): 
    return file_name.endswith(".c")

def extract_names(file_name):

    #Running CLANG to get an AST
    ast = subprocess.check_output([CLANG_PATH, "-Xclang", "-ast-dump", "-fsyntax-only", "-fno-color-diagnostics", file_name])
    
    #Parsing the given AST to get the variable declarations
    variables = []
    for line in ast.split('\n'):
        
        #Is this a variable declaration?
        match = re.match("^.*VarDecl[^>]*>\s*(\S+)\s*\'([^']*)'$", line)
        if not match:
            continue
        
        #Adding the name of the variable and its type
        variables.append((match.group(1), match.group(2)))
    
    return variables

