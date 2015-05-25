from copy import deepcopy
import logging
import os
import TestRunner

# Setup debug level:
logging.basicConfig(level=logging.DEBUG)
logging.debug('DEBUG - debug message')
logging.info('INFO - info message')
logging.warning('WARNING - warning message')
logging.error('ERROR - error message ')
logging.critical('CRITICAL - critical message')


try:
    import AutomationFramework.parser.SCXML as SCXMLparsing
    import AutomationFramework.parser.AccessDataModel as AccessData
except ImportError:
    logging.critical('parser for SCXML not found, please solve this before continue testing')


class MyMainClass:
    ''' Class where all stuctures are saved and control all workflow
    '''

    def run(self, file_script):
        logging.debug('starting ran of the Script')
