import logging
import os
import time
from typing import Tuple, List

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
                cursor.execute("CREATE TABLE IF NOT EXISTS operations(id INTEGER, date REAL, amount REAL)")
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
            client_id = self.get_id(name)
            with DBCursor(self.host) as cursor:
                cursor.execute("INSERT INTO operations VALUES(?, ?, ?)", (client_id, time.time(), amount))
        except Exception:
            log.critical("An exception was raised.")
            raise
        else:
            log.debug("The operation was successfully added. Updating totals.")
            self.update_totals()

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
    
    def update_totals(self):
        """Updates the totals in 'totals' table."""
        try:
            log.debug("Updating totals.")
            totals = self.get_all_totals()
            with DBCursor(self.host) as cursor:
                cursor.execute("DELETE FROM totals")
                for id, total in totals:
                    cursor.execute("INSERT INTO totals VALUES(?, ?)", (id, total))
        except Exception:
            log.critical("An exception was raised.")
            raise
    
    def get_all_totals(self) -> List[Tuple[int, float]]:
        """Get's all totals"""
        try:
            log.debug("Getting all totals.")
            totals = []
            with DBCursor(self.host) as cursor:
                for client in self.get_all_clients_id():
                    this_clients_total = 0
                    cursor.execute("SELECT amount FROM operations WHERE id=?", (client, ))
                    results = cursor.fetchall()
                    for operation in results:
                        this_clients_total += operation[0]
                    totals.append((client, this_clients_total))
        except Exception:
            log.critical("An exception was raised.")
            raise
        else:
            log.debug("Totals successfully calculated.")
            return totals

    def get_all_clients_id(self) -> List[int]:
        """Get's all client's id."""
        try:
            with DBCursor(self.host) as cursor:
                cursor.execute("SELECT rowid FROM clients")
                clients_id = [result[0] for result in cursor.fetchall()]
                if not clients_id:
                    raise ClientNotFound("There are no clients.")
        except Exception:
            log.critical("An exception was raised.")
            raise
        else:
            return clients_id

    def get_clients_names(self) -> List[str]:
        """Get's all client's names."""
        try:
            with DBCursor(self.host) as cursor:
                cursor.execute("SELECT name FROM clients")
                names = [result[0].title() for result in cursor.fetchall()]
                if not names:
                    raise ClientsNotFound("There are no clients.")
        except Exception:
            log.critical("An exception was raised.")
            raise
        else:
            return names