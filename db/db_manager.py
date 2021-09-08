import logging
import os

from db.db_cursor import *
from utils.errors import *

log = logging.getLogger("fiados_qt.db_manager")

class Database:
    def __init__(self, host: str) -> None:
        log.debug("Initializing Database object.")
        self.host = self.db_path(host)
        # Checking if the file exists
        file_exists = self.check_file()
        # Setting database file
        self.set_database_file(file_exists)
                   

    def check_file(self) -> bool:
        """Checks if the database file prompted at self.host exists at all."""
        try:
            log.debug("Checking if database file exists.")
            with open(self.host, 'r'):
                pass
        except FileNotFoundError:
            log.critical("Database file doesn't exists.")
            return False
        except Exception:
            log.critical("An exception was raised.")
            raise
        else:
            log.debug("Database file exists.")
            return True

    def set_database_file(self, file_exists: bool) -> None:
        """Sets the entire database file."""
        try:
            if not file_exists:
                log.debug("Creating a file for the database.")
                with open(self.host, 'w'):
                    pass
            log.debug("File already created. Setting up the tables")
            with DBCursor(self.host) as cursor:
                cursor.execute("CREATE TABLE IF NOT EXISTS clients(name TEXT UNIQUE)")
                cursor.execute("CREATE TABLE IF NOT EXISTS operations(id INTEGER UNIQUE PRIMARY KEY, date REAL, amount REAL)")
                cursor.execute("CREATE TABLE IF NOT EXISTS totals(id INTEGER UNIQUE PRIMARY KEY, total REAL)")
            log.debug("Database file tables should be ok.")
        except Exception:
            log.critical("An exception was raised")
            raise
        else:
            log.debug("Database file set successfully.")
    
    def db_path(self, host: str) -> str:
        """Returns the absolute path for the database file provided."""
        app_path = os.path.abspath(os.getcwd())
        folder = 'db'
        path = os.path.join(app_path, folder)
        return os.path.normpath(os.path.join(path, host)) + ".db"
    
