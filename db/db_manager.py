import logging

from db.db_cursor import *
from utils.errors import *

log = logging.getLogger("fiados_qt.db_manager")

class Database:
    def __init__(self, host: str) -> None:
        log.debug("Initializing Database object.")
        self.host = host
        print(self.check_file())

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
            return True
