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

        # Sell page
        self.sell_page = QWidget()
        self.sell_page.setObjectName(u"sell_page")
        self.sell_layout = QVBoxLayout(self.sell_page)
        self.sell_layout.setSpacing(10)
        self.sell_layout.setObjectName(u"sell_layout")
        self.sell_layout.setContentsMargins(10, 10, 10, 10)
        
        # Frames for this page
        # Frame for the input in products
        self.add_product_frame = QFrame()
        self.add_product_frame.setObjectName(u"sell_product_frame")
        # A layout for this frame
        self.add_product_layout = QHBoxLayout(self.add_product_frame)
        self.add_product_layout.setSpacing(10)
        self.add_product_layout.setContentsMargins(10, 0, 10, 0)
        
        # A label that preceds the combobox
        self.add_product_label = QLabel("Product")
        self.add_product_label.setStyleSheet("font: 100 13pt 'Segoe UI';")
        self.add_product_label.setAlignment(Qt.AlignLeft)
        # A combobox to select the product
        self.add_product_combobox = FormCombobox(visible=True, enabled=False, editable=True)
        # Label that preceds the units
        self.sell_units_label = QLabel("Units")
        self.sell_units_label.setStyleSheet("font: 100 13pt 'Segoe UI';")
        self.sell_units_label.setAlignment(Qt.AlignLeft)
        # A line edit to have the units
        self.sell_units_lineedit = FormLineEdit(visibility=True, width=50, text_alignment='right')
        validator = QRegularExpressionValidator(QRegularExpression("[0-9]+"))
        self.sell_units_lineedit.setValidator(validator)
        # A spacer to show the button at the most right
        self.top_button_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # A button to add this product and it's units to the sell list
        self.add_item_btn = FormButton("+", height=25)
        # Adding this items to the add_product_layout
        self.add_product_layout.addWidget(self.add_product_label)
        self.add_product_layout.addWidget(self.add_product_combobox)
        self.add_product_layout.addWidget(self.sell_units_label)
        self.add_product_layout.addWidget(self.sell_units_lineedit)
        self.add_product_layout.addItem(self.top_button_spacer)
        self.add_product_layout.addWidget(self.add_item_btn)


        # Frame for add the selling process.
        self.complete_sell_frame = QFrame()
        self.complete_sell_frame.setObjectName(u"complete_sell_frame")
        # A layout for this one
        self.complete_sell_layout = QHBoxLayout(self.complete_sell_frame)
        self.complete_sell_layout.setSpacing(10)
        self.complete_sell_layout.setContentsMargins(10, 0, 10, 0)

        # A clear btn 
        self.clear_sell_btn = FormButton("Clear")
        # A spacer
        self.bottom_sell_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # Concrete sell btn
        self.concrete_sell_btn = FormButton("Complete sell")
        # Adding these to the complete_sell_layout
        self.complete_sell_layout.addWidget(self.clear_sell_btn)
        self.complete_sell_layout.addItem(self.bottom_sell_spacer)
        self.complete_sell_layout.addWidget(self.concrete_sell_btn)



        # Table where we can see the products for this transaction
        self.selling_table = QTableWidget()
        self.selling_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.selling_table.setStyleSheet("background-color: white;")
        # Setting the columns
        # A font for this one
        column_font = QFont()
        column_font.setFamily('Segoe UI')
        column_font.setPointSize(12)
        column_font.setBold(True)
        column_font.setWeight(QFont.Weight.Bold)
        # Setting the header
        if self.selling_table.columnCount() < len(SELLING_CART_TABLE_COLUMNS):
            self.selling_table.setColumnCount(len(SELLING_CART_TABLE_COLUMNS))
        for i, column in enumerate(SELLING_CART_TABLE_COLUMNS, 0):
            item = QTableWidgetItem()
            item.setText(column)
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(column_font)
            self.selling_table.setHorizontalHeaderItem(i, item)
        self.selling_table.horizontalHeader().setDefaultSectionSize(100)
        self.selling_table.horizontalHeader().setMinimumSectionSize(80)
        # Formatting the size for each header
        for i, size in enumerate(SELLING_CART_TABLE_SIZE, 0):
            self.selling_table.horizontalHeader().setSectionResizeMode(i, size)
        # Showing horizontal header and hiding the vertical one
        self.selling_table.horizontalHeader().setVisible(True)
        self.selling_table.verticalHeader().setVisible(False)
         
        # Adding widgets and frames to this layout
        self.sell_layout.addWidget(self.add_product_frame)
        self.sell_layout.addWidget(self.selling_table)
        self.sell_layout.addWidget(self.complete_sell_frame)

        StackedPages.addWidget(self.sell_page)

        self.stock_page = QWidget()
        self.stock_page.setObjectName(u"stock_page")
        self.stock_layout = QHBoxLayout(self.stock_page)
        self.stock_layout.setSpacing(0)
        self.stock_layout.setObjectName(u"stock_layout")
        self.stock_layout.setContentsMargins(0, 0, 0, 0)
        
        self.stock_menu = QFrame()
        self.stock_menu.setStyleSheet(f"background-color: {Color.STOCK_LEFT_MENU};")
        self.stock_menu.setMaximumWidth(Dimension.STOCK_LEFT_MENU_WIDTH)
        self.stock_menu.setMinimumWidth(Dimension.STOCK_LEFT_MENU_WIDTH)

        # Stock left menu layout
        self.stock_menu_layout = QVBoxLayout(self.stock_menu)
        self.stock_menu_layout.setContentsMargins(0, Dimension.BTN_DEF_HEIGHT - Dimension.TOP_BAR_HEIGHT, 0, 0)
        self.stock_menu_layout.setSpacing(0)
        self.stock_menu_layout.setAlignment(Qt.AlignTop)

        # Stock left menu buttons
        self.add_buy_btn = MinorLeftMenuButtons("Add buy", icon_path="stock_add_icon.svg", btn_active_border_right=Color.CONTENT_BACKGROUND, is_active=True)
        self.show_stock_btn = MinorLeftMenuButtons("Show stock", icon_path="stock_list_icon.svg", btn_active_border_right=Color.CONTENT_BACKGROUND)

        # Adding this stock left buttons to the left menu from stock
        self.stock_menu_layout.addWidget(self.add_buy_btn)
        self.stock_menu_layout.addWidget(self.show_stock_btn)

        self.stock_layout.addWidget(self.stock_menu)
        

        # Adding the stock stacked pages to this page
        self.stock_stacked_widget = QStackedWidget()
        # STYLEESHEET REQUIRED? #
        # Set the pages
        self.ui_stock_stacked_pages = UIStockStackedPages()
        self.ui_stock_stacked_pages.setupUi(self.stock_stacked_widget)
        self.stock_stacked_widget.setCurrentWidget(self.ui_stock_stacked_pages.add_buy_page)

        self.stock_layout.addWidget(self.stock_stacked_widget)



        StackedPages.addWidget(self.stock_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.about_layout = QVBoxLayout(self.about_page)
        self.about_layout.setSpacing(0)
        self.about_layout.setObjectName(u"about_layout")
        self.about_layout.setContentsMargins(0, 0, 0, 0)
        self.about_label = QLabel(self.about_page)
        self.about_label.setObjectName(u"about_label")
        self.about_label.setText(u"About page")
        self.about_label.setAlignment(Qt.AlignCenter)

        self.about_layout.addWidget(self.about_label)

        StackedPages.addWidget(self.about_page)

        self.retranslateUi(StackedPages)

        QMetaObject.connectSlotsByName(StackedPages)
    # setupUi

    def retranslateUi(self, StackedPages):
        pass
    # retranslateUi

