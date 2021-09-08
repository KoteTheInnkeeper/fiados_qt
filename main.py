import logging

# Erasing previous logfile
with open('log.log', 'w'):
    pass

# Setting up the logger
logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s", level=logging.DEBUG,
                    filename='log.log')

from db.db_manager import *
# GUI
from qt_core import *
from gui.windows.main_window.ui_main_window import UIMainWindow
from gui.gui_constants import *

from utils.errors import *
from typing import List, Union

db_object = Database('db_file')


# Main window, the one we show.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
         # Setting the title
        self.setWindowTitle("Saldos")
        self.setWindowIcon(QIcon('gui/windows/main_window/main_icon.png'))

        # Setting up the main window
        self.ui = UIMainWindow()
        self.ui.setup_ui(self)

        # Signals for left menu buttons
        self.ui.toggle_btn.clicked.connect(self.show_menu)
        self.ui.add_btn.clicked.connect(self.add_btn_clicked)
        self.ui.totals_btn.clicked.connect(self.totals_btn_clicked)
        self.ui.about_btn.clicked.connect(self.about_btn_clicked)

        self.show()

    def reset_btns(self):
        """Resets all btns"""
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except Exception:
                log.critical("An exception was raised.")
                raise
    
    def add_btn_clicked(self):
        """Changes the page to add btn"""
        log.debug("Add btn clicked on the left menu.")
        self.ui.top_label_left.setText("Agregar operación")
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.add_op_page)
        self.reset_btns()
        self.ui.add_btn.set_active(True)

    def totals_btn_clicked(self):
        """Changes the page to add btn"""
        log.debug("Totals btn clicked on the left menu.")
        self.ui.top_label_left.setText("Saldos")
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.totals_page)
        self.reset_btns()
        self.ui.totals_btn.set_active(True)

    def about_btn_clicked(self):
        """Changes the page to add btn"""
        log.debug("About btn clicked on the left menu.")
        self.ui.top_label_left.setText("Información")
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.about_page)
        self.reset_btns()
        self.ui.about_btn.set_active(True)

    def show_menu(self):
        """An animation to show the left menu."""
        log.debug("Show menu btn clicked.")
        menu_width = self.ui.left_menu.width()
        width = Dimension.LEFT_MENU_WIDTH
        if menu_width == 50:
            width = Dimension.LEFT_MENU_EXPANDED_WIDTH
        
        # Start animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())