import logging
import os
import time

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

    def add_client(self, name: str) -> None:
        """Adds a client to the database."""
        try:
            log.debug("Adding a client.")
            with DBCursor(self.host) as cursor:
                cursor.execute("INSERT INTO clients VALUES (?)", (name.lower().strip(), ))
        except sqlite3.IntegrityError:
            log.critical("The name was repeated.")
            raise SuchClientExists("The name provided for this new client is already in the database.")
        except Exception:
            log.critical("An exception was raised.")
            raise
        else:
            log.debug(f"Client {name.title()} added successfully.")

    def add_operation(self, name: str, amount: float) -> None:
        """Adds the operation."""
        try:
            log.debug("Adding a new operation.")
            amount = float(amount)
            with DBCursor(self.host) as cursor:
                cursor.execute("")

        except Exception:
            log.critical("An exception was raised.")

    def get_id(self, name: str) -> int:
        """Get's a client's id by it's name."""
        try:
            log.debug(f"Getting {name.title()}'s id.")
            with DBCursor(self.host) as cursor:
                cursor.execute("SELECT rowid FROM clients WHERE name=?", (name.lower().strip(), ))
                result = cursor.fetchone()
                if not result:
                    log.debug(f"We couldn't find any client in database named {name.title()}")
                    raise ClientNotFound("There's no client named like so in the database.")
        except Exception:
            log.critical("An exception was raised.")
            raise
        else:
            log.debug(f"The following id was found for {name.title()}: {result[0]}.")
            return int(result[0])
    
