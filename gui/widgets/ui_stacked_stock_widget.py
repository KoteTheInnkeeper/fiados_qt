from PySide6 import QtGui, QtWidgets
import PySide6
from qt_core import *
from gui.gui_constants import *
from gui.widgets.py_pushbutton import *
from gui.widgets.py_lineedit import FormLineEdit
from gui.widgets.py_combobox import FormCombobox

ADD_TABLE_COLUMS = ("Id", "Product name", "Units","Cost", "Price")
ADD_TABLE_SIZE_FORMAT = (QHeaderView.ResizeToContents, QHeaderView.Stretch, QHeaderView.ResizeToContents,QHeaderView.ResizeToContents, QHeaderView.ResizeToContents)
SHOW_TABLE_COLUMS = ("Id", "Product name", "Last buy", "Cost", "Price", "In storage")
SHOW_TABLE_SIZE_FORMAT = (QHeaderView.ResizeToContents, QHeaderView.Stretch, QHeaderView.ResizeToContents,QHeaderView.ResizeToContents, QHeaderView.ResizeToContents, QHeaderView.ResizeToContents)

class UIStockStackedPages(object):
    def setupUi(self, StockStackedPages: QStackedWidget):
        if not StockStackedPages.objectName():
            StockStackedPages.setObjectName(u"StockStackedPages")
        StockStackedPages.resize(800, 600)
        StockStackedPages.setWindowTitle(u"StockStackedPages")

        # Making the widgets for add buy page
        self.add_buy_page = QWidget()
        self.add_buy_page.setObjectName(u"add_buy_page")
        # Setting up a layout for add buy page
        self.add_buy_layout = QVBoxLayout(self.add_buy_page)
        self.add_buy_layout.setContentsMargins(10, 10, 10, 10)
        self.add_buy_layout.setSpacing(10)
        self.add_buy_layout.setAlignment(Qt.AlignVCenter)
        # Making the elements that are going to fit within this layout
        # A frame to hold the 'products' widgets
        self.set_product_frame = QFrame()
        self.set_product_frame.setMinimumHeight(20)
        self.set_product_frame.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        # A layout for this frame
        self.set_product_layout = QHBoxLayout(self.set_product_frame)
        self.set_product_layout.setSpacing(10)
        self.set_product_layout.setContentsMargins(0, 0, 0, 0)
        # Elements for this frame
        # Label
        self.set_product_label = QLabel("Product")
        self.set_product_label.setStyleSheet("font: 100 13pt 'Segoe UI';")
        # Combobox for products that are already in database
        self.set_product_combobox = FormCombobox(enabled=False, editable=True)
        # A line edit in case the product is a new one
        self.new_product_linedit = FormLineEdit(visibility=True)
        # A checkbox to tell if the product is a new one
        self.new_product_checkbox = QCheckBox()
        self.new_product_checkbox.setChecked(True)
        self.new_product_checkbox.setText("New")

        # A cost label
        self.cost_label = QLabel("Cost")
        self.cost_label.setStyleSheet("font: 100 13pt 'Segoe UI';")
        # A cost line_edit
        self.cost_lineedit = FormLineEdit(visibility=True, width=75, text_alignment = "right")
        validator = QRegularExpressionValidator(QRegularExpression("[0-9]*\.[0-9]{2}"))
        self.cost_lineedit.setValidator(validator)
        # Cash label
        self.cash_label = QLabel("$")
        self.cash_label.setStyleSheet("font: 100 13pt 'Segoe UI';")
        self.cash_label.setAlignment(Qt.AlignLeft)

        # A price label
        self.price_label = QLabel("Price")
        self.price_label.setStyleSheet("font: 100 13pt 'Segoe UI';")
        # A price line_edit
        self.price_lineedit = FormLineEdit(visibility=True, width=75, text_alignment = "right")
        self.price_lineedit.setValidator(validator)
        # Cash label
        self.cash_label_2 = QLabel("$")
        self.cash_label_2.setStyleSheet("font: 100 13pt 'Segoe UI';")
        self.cash_label_2.setAlignment(Qt.AlignLeft)

        # Units label
        self.units_label = QLabel("Units")
        self.units_label.setStyleSheet("font: 100 13pt 'Segoe UI';")
        # Units lineedit
        self.units_lineedit = FormLineEdit(visibility=True, width=50, text_alignment="right")
        validator = QRegularExpressionValidator(QRegularExpression("[0-9]+"))
        self.units_lineedit.setValidator(validator)        

        # Spacer
        self.btn_spacer_2 = QSpacerItem(100000, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # A button to add this product
        self.add_product_btn = FormButton("+", height=25)

        # Let's add these three elements to the layout
        self.set_product_layout.addWidget(self.set_product_label)
        self.set_product_layout.addWidget(self.set_product_combobox)
        self.set_product_layout.addWidget(self.new_product_linedit)
        self.set_product_layout.addWidget(self.new_product_checkbox)
        self.set_product_layout.addWidget(self.cost_label)
        self.set_product_layout.addWidget(self.cost_lineedit)
        self.set_product_layout.addWidget(self.cash_label)
        self.set_product_layout.addWidget(self.price_label)
        self.set_product_layout.addWidget(self.price_lineedit)
        self.set_product_layout.addWidget(self.cash_label_2)
        self.set_product_layout.addWidget(self.units_label)
        self.set_product_layout.addWidget(self.units_lineedit)
        self.set_product_layout.addItem(self.btn_spacer_2)
        self.set_product_layout.addWidget(self.add_product_btn)

        # A table for us to show what's currently being added as a buy
        self.buy_list_table = QTableWidget()
        self.buy_list_table.setMinimumWidth(724)
        self.buy_list_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.buy_list_table.setStyleSheet("background-color: white;")
        # Setting the columns
        column_font = QFont()
        column_font.setFamily('Segoe UI')
        column_font.setPointSize(12)
        column_font.setBold(True)
        column_font.setWeight(QFont.Weight.Bold)
        if self.buy_list_table.columnCount() < len(ADD_TABLE_COLUMS):
            self.buy_list_table.setColumnCount(len(ADD_TABLE_COLUMS))
        for i, column in enumerate(ADD_TABLE_COLUMS, 0):
            item = QTableWidgetItem()
            item.setText(column)
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(column_font)
            self.buy_list_table.setHorizontalHeaderItem(i, item)
        self.buy_list_table.horizontalHeader().setDefaultSectionSize(100)
        self.buy_list_table.horizontalHeader().setMinimumSectionSize(80)
        # Formatting the size for each header
        for i, size in enumerate(ADD_TABLE_SIZE_FORMAT, 0):
            self.buy_list_table.horizontalHeader().setSectionResizeMode(i, size)
        # Showing horizontal header and hiding vertical
        self.buy_list_table.horizontalHeader().setVisible(True)
        self.buy_list_table.verticalHeader().setVisible(False)
    
        # A frame to hold the "add" and "clear list" buttons
        self.stock_btn_frame = QFrame()
        # Setting a layout
        self.stock_btn_layout = QHBoxLayout(self.stock_btn_frame)
        self.stock_btn_layout.setContentsMargins(0, 0, 0, 0)
        self.stock_btn_layout.setSpacing(0)
        self.stock_btn_layout.setAlignment(Qt.AlignCenter)
        # Buttons for this layout
        self.add_stock_btn = FormButton("Add to stock")
        self.clear_stock_btn = FormButton("Clear list")
        # A spacer to space them
        self.btn_spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # Adding these to the layout
        self.stock_btn_layout.addWidget(self.clear_stock_btn)
        self.stock_btn_layout.addItem(self.btn_spacer)
        self.stock_btn_layout.addWidget(self.add_stock_btn)

        # Adding all of this to the add_page layout
        self.add_buy_layout.addWidget(self.set_product_frame)
        self.add_buy_layout.addWidget(self.buy_list_table)
        self.add_buy_layout.addWidget(self.stock_btn_frame)

        # Making the widgets for see stock page
        self.stock_list_page = QWidget()
        self.stock_list_page.setObjectName(u"stock_list_page")
         # Setting up a layout for add buy page
        self.stock_list_page_layout = QVBoxLayout(self.stock_list_page)
        self.stock_list_page_layout.setContentsMargins(10, 10, 10, 10)
        self.stock_list_page_layout.setSpacing(10)
        self.stock_list_page_layout.setAlignment(Qt.AlignVCenter)
        # Making the elements that are going to fit within this layout
        # A frame to hold the 'products' widgets
        self.select_product = QFrame()
        self.select_product.setMinimumHeight(20)
        self.select_product.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        # A layout for this frame
        self.select_product_layout = QHBoxLayout(self.select_product)
        self.select_product_layout.setSpacing(10)
        self.select_product_layout.setContentsMargins(0, 0, 0, 0)
        # Elements for this frame
        # Label
        self.select_product_label = QLabel("Product")
        self.select_product_label.setStyleSheet("font: 100 13pt 'Segoe UI';")
        # Combobox for products that are already in database
        self.select_product_combobox = FormCombobox(visible=True, enabled=False, editable=True)
        self.select_product_combobox.setEditable(True)
        # A checkbox to show all of the products
        self.show_all_products_checkbox = QCheckBox("Show all")
        self.show_all_products_checkbox.setChecked(True)
        # Adding this to the layout
        self.select_product_layout.addWidget(self.select_product_label)
        self.select_product_layout.addWidget(self.select_product_combobox)
        self.select_product_layout.addWidget(self.show_all_products_checkbox)

        # A table to show the products
        self.show_stock_list_page_table = QTableWidget()
        self.show_stock_list_page_table.setMinimumWidth(724)
        self.show_stock_list_page_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.show_stock_list_page_table.setStyleSheet("background-color: white;")
        # Setting the columns
        column_font = QFont()
        column_font.setFamily('Segoe UI')
        column_font.setPointSize(12)
        column_font.setBold(True)
        column_font.setWeight(QFont.Weight.Bold)
        if self.show_stock_list_page_table.columnCount() < len(SHOW_TABLE_COLUMS):
            self.show_stock_list_page_table.setColumnCount(len(SHOW_TABLE_COLUMS))
        for i, column in enumerate(SHOW_TABLE_COLUMS, 0):
            item = QTableWidgetItem()
            item.setText(column)
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(column_font)
            self.show_stock_list_page_table.setHorizontalHeaderItem(i, item)
        self.show_stock_list_page_table.horizontalHeader().setDefaultSectionSize(100)
        self.show_stock_list_page_table.horizontalHeader().setMinimumSectionSize(80)
        # Formatting the size for each header
        for i, size in enumerate(SHOW_TABLE_SIZE_FORMAT, 0):
            self.show_stock_list_page_table.horizontalHeader().setSectionResizeMode(i, size)
        # Showing horizontal header and hiding vertical
        self.show_stock_list_page_table.horizontalHeader().setVisible(True)
        self.show_stock_list_page_table.verticalHeader().setVisible(False)

        # A frame to put the button to update
        self.update_stock_frame = QFrame()
        self.update_stock_frame.setObjectName(u"update_stock_frame")
        # A layout for this frame
        self.update_stock_layout = QHBoxLayout(self.update_stock_frame)
        self.update_stock_layout.setSpacing(10)
        self.update_stock_layout.setContentsMargins(0, 0, 0, 0)

        # A spacer to push this button to the most right
        self.update_stock_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # A button to save changes in stock
        self.save_changes_btn = FormButton("Save changes")
        
        # Adding these to the update_stock_layout
        self.update_stock_layout.addItem(self.update_stock_spacer)
        self.update_stock_layout.addWidget(self.save_changes_btn)


        # Adding the select product frame and table to this layout
        self.stock_list_page_layout.addWidget(self.select_product)
        self.stock_list_page_layout.addWidget(self.show_stock_list_page_table)
        self.stock_list_page_layout.addWidget(self.update_stock_frame)

        # Adding both pages to the stacked stock pages.
        StockStackedPages.addWidget(self.add_buy_page)
        StockStackedPages.addWidget(self.stock_list_page)

        StockStackedPages.setCurrentWidget(self.add_buy_page)
        


        QMetaObject.connectSlotsByName(StockStackedPages)
