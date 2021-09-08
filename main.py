import logging

# Erasing previous logfile
with open('log.log', 'w'):
    pass

# Setting up the logger
logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s", level=logging.DEBUG,
                    filename='log.log')

from db.db_manager import *

db_object = Database('db_file')
