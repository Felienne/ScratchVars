from conf import *
import subprocess

def get_name(): 
    return 'java'

def can_extract(full_name):
    return full_name.endswith(".java")

def extract_names(full_name): 

    #Running the Java AST dumper which dumps variable types and names
    names_and_types = subprocess.check_output([JAVA_PATH, "-jar", VARDUMP_JAR_PATH, full_name]).strip().split('\n')

    if len(names_and_types) < 2:
        return []

    #Parsing the given AST to get the variable declarations
    variables = []
    for i in range(0, len(names_and_types), 2):

        var_type = names_and_types[i]
        var_name = names_and_types[i+1]

        #Adding the name of the variable and its type
        variables.append((var_name, var_type))

    return variables
