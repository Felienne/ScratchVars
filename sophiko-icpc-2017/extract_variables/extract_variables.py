from conf import *
import sys, os, time, logging
import pprint
import extractors
from pymongo import MongoClient

def load_extractors():
    '''
    Loads all the extractor modules
    '''
    res = []
    for module in extractors.__all__:
        mod = __import__("extractors.%s" % module)
        mod = eval('mod.%s' % module)
        res.append({'can_extract'   : mod.can_extract,
                    'extract_names' : mod.extract_names,
                    'get_name'      : mod.get_name})
    return res

def configure_logging():
    '''
    Configuring the loggers used
    '''
    logger = logging.root
    logger.setLevel(LOG_LEVEL)
    fh = logging.FileHandler(LOG_FILE_PATH)
    fh.setLevel(LOG_LEVEL)
    ch = logging.StreamHandler()
    ch.setLevel(LOG_LEVEL)
    formatter = logging.Formatter(LOG_FORMAT)
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)

def main():

    #Reading the commandline arguments
    if len(sys.argv) != 2:
        print "USAGE: %s <SOURCE_DIRECTORY>" % sys.argv[0]
        return
    source_directory = sys.argv[1]

    configure_logging()
    print "connecting to dbserver: %s" % DATABASE_SERVER
    db_client = MongoClient(DATABASE_SERVER, DATABASE_PORT)
    extractors = load_extractors()
    print "connected: %s" % DATABASE_SERVER
    
    pprint.pprint(extractors)
    print "scaning: %s" % source_directory
    #Going over each source file
    for root, directory, files in os.walk(source_directory):
        for file_name in files:
            full_name = os.path.join(root, file_name)
            print "anaylze: %s" % full_name
            #Finding the matching extractor
            for extractor in extractors:
                if extractor['can_extract'](full_name):

                    #Getting the names from the source file
                    try:
                        variables = extractor['extract_names'](full_name)
                    except Exception as ex:
                        logging.warning('Failed to extract %s' % full_name)
                        continue 

                    #Inserting each name entry into the database
                    for variable_name, variable_type in variables:
                        db_client.extract_vars.variables.insert_one({'extractor'     : extractor['get_name'](),
                                                                     'full_name'     : full_name,
                                                                     'file_name'     : file_name,
                                                                     'variable_name' : variable_name,
                                                                     'variable_type' : variable_type,
                                                                     'time_added'    : time.time()}) 

if __name__ == "__main__":
    main()


