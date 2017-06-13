from conf import *
import subprocess
import re
import json
import pprint
import pdb

def get_name():
    return 'perl'

def can_extract(file_name): 
    return file_name.endswith(".pl")


def extract_names(file_name):

    #Running PERL_SCRIPT to get an OPCODE/AST
    ast = subprocess.check_output([PERL_PATH,PERL_COMMAND_LINE_PASRER, file_name])
     
    #Parsing the given AST to get the variable declarations
    variables = []
    for line in ast.split('\n'):
        
        #Is this a variable declaration?
        PERL_REGEX_VAR_FINDER = "(\[)(\*.+)(\])"
        #"(gvsv\[)(\*.+)(\])"
        #print line
        match = re.search(PERL_REGEX_VAR_FINDER, line)
        if not match:
            continue      
        
        
        #Adding the name of the variable and its type
        variables.append((match.group(2)[1:],"unknown"))
    
    return variables

