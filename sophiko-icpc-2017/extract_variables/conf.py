import logging

#The path of the clang binary
CLANG_PATH = "clang"

#The path of the node binary
NODE_PATH = "node"

#The path of the Java binary
JAVA_PATH = "java"

#The path of the Php binary
PHP_PATH = "php"

#The path of the ast dumper for php
PHP_AST_PATH = "extractors/php/getast.php"


PERL_PATH = "perl"

PERL_COMMAND_LINE_PASRER = "-MO=Concise"

#The path of the variable dumper JAR
VARDUMP_JAR_PATH = "extractors/DumpVariables.jar"

#The server on which the database is listening
DATABASE_SERVER = "localhost"

#The port on which the database is listening
DATABASE_PORT = 27017

#The log level used
LOG_LEVEL = logging.DEBUG

#The log file used
LOG_FILE_PATH = 'extract_variables.log'

#The format of the log messages
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
