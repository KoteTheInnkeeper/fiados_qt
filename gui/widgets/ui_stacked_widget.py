from gui.widgets.py_lineedit import FormLineEdit
from qt_core import *
from gui.gui_constants import *
from gui.widgets.py_pushbutton import FormButton, MinorLeftMenuButtons
from gui.widgets.ui_stacked_stock_widget import UIStockStackedPages
from gui.widgets.py_combobox import *

SELLING_CART_TABLE_COLUMNS = ("Id", "Product name", "Units", "Price", "Total", "Stock after transaction")
SELLING_CART_TABLE_SIZE = (QHeaderView.ResizeToContents, QHeaderView.Stretch, QHeaderView.ResizeToContents, QHeaderView.ResizeToContents, QHeaderView.ResizeToContents, QHeaderView.ResizeToContents)

class UIStackedPages(object):
    def setupUi(self, StackedPages):
        if not StackedPages.objectName():
            StackedPages.setObjectName(u"StackedPages")
        StackedPages.resize(640, 480)
        StackedPages.setWindowTitle(u"StackedWidget")

        # Add operation page
        self.add_op_page = QWidget()
        self.add_op_page.setObjectName(u"sell_page")
        self.add_op_layout = QVBoxLayout(self.add_op_page)
        self.add_op_layout.setSpacing(10)
        self.add_op_layout.setObjectName(u"sell_layout")
        self.add_op_layout.setContentsMargins(10, 10, 10, 10)

        # Test label
        self.add_op_label = QLabel("Agregar operación")

        # Adding to layout
        self.add_op_layout.addWidget(self.add_op_label)

        # Adding this page to the stackedpages widget.        
        StackedPages.addWidget(self.add_op_page)

        # Show totals page
        self.totals_page = QWidget()
        self.totals_page.setObjectName(u"totals_page")
        self.totals_layout = QHBoxLayout(self.totals_page)
        self.totals_layout.setSpacing(0)
        self.totals_layout.setObjectName(u"totals_layout")
        self.totals_layout.setContentsMargins(0, 0, 0, 0)

        # Test label
        self.totals_label = QLabel("Mostrar totales")

        # Adding to layout
        self.totals_layout.addWidget(self.totals_label)

        # Adding this page to the stackedpages widget
        StackedPages.addWidget(self.totals_page)


        # About page
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.about_layout = QVBoxLayout(self.about_page)
        self.about_layout.setSpacing(0)
        self.about_layout.setObjectName(u"about_layout")
        self.about_layout.setContentsMargins(0, 0, 0, 0)
        self.about_label = QLabel(self.about_page)
        self.about_label.setObjectName(u"about_label")

        # Test label
        self.about_label.setText(u"About page")
        self.about_label.setAlignment(Qt.AlignCenter)

        self.about_layout.addWidget(self.about_label)

        StackedPages.addWidget(self.about_page)

        QMetaObject.connectSlotsByName(StackedPages)
    # setupUi

  

