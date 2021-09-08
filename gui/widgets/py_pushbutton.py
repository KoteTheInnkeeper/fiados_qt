import logging
import os

from qt_core import *
from gui.gui_constants import Color, Dimension

from utils.errors import *

log = logging.getLogger("inventory_qt.py_pushbutton")


class LeftMenuPushButton(QPushButton):
    def __init__(
        self,
        text: str="", 
        height: int=Dimension.BTN_DEF_HEIGHT, 
        minimum_width: int=50, 
        text_padding: int=55, 
        text_color: str=Color.BTN_TEXT, 
        icon_path: str="", 
        icon_color: str="black",
        btn_color: str=Color.BTN_BG, 
        btn_hover: str=Color.BTN_HOVER,
        btn_pressed :str=Color.BTN_PRESSED,
        btn_active: str=Color.BTN_ACTIVE,
        btn_active_border_right: str=Color.BTN_ACTIVE,
        btn_active_border_left: str=Color.BTN_ACTIVE,
        btn_active_border_bot: str=Color.BTN_ACTIVE,
        btn_active_border_top: str=Color.BTN_ACTIVE,
        is_active: bool= False
    ):
        super().__init__()

        # Set default parameters
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # Custom parameters
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.icon_path = icon_path
        self.text_color = text_color
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.btn_active = btn_active
        self.btn_active_border_left = btn_active_border_left
        self.btn_active_border_top = btn_active_border_top
        self.btn_active_border_right = btn_active_border_right
        self.btn_active_border_bot = btn_active_border_bot
        self.is_active = is_active

        # Set stylesheet according to what we've entered.
        self.set_style()

    def set_style(self):
        stylesheet_str = f"""
        QPushButton {{
            color: {self.text_color};
            background-color: {self.btn_color};
            padding-left: {self.text_padding}px;
            text-align: left;
            border: none;
            font: 75 12pt 'Segoe UI';
        }}

        QPushButton:hover {{
            background-color: {self.btn_hover};
        }}
        
        QPushButton:pressed {{
            background-color: {self.btn_pressed};
        }}
        """

        active_str =f"""
        QPushButton {{
            background-color: {self.btn_active};
            border-left: 5px solid {self.btn_active_border_left};
            border-top: 5px solid {self.btn_active_border_top};
            border-right: 5px solid {self.btn_active_border_right};
            border-bottom: 5px solid {self.btn_active_border_bot};
        }}
        """

        if not self.is_active:
            self.setStyleSheet(stylesheet_str)
        else:
            self.setStyleSheet(stylesheet_str + active_str)

    def paintEvent(self, event):
        """Custom paintEvent for this custom button."""
        # Painting button
        log.debug("Inside paint event")
        QPushButton.paintEvent(self, event)

        # Creating a QPainter object
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        # Creating a rectangle for reference for our icon
        rect = QRect(0, 0, self.minimum_width, self.minimumHeight())

        # Drawing the icon
        self.draw_icon(qp, self.icon_path, rect, self.icon_color)

        qp.end()

    def draw_icon(self, qp: QPainter, image: str, rect: QRect, color: str):
        # Formatting the path for the image
        app_path = os.path.abspath(os.getcwd())
        folder = 'gui/images/icons'
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))

        # Drawing the icon
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        
        # Drawing pixmap
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()

    def set_active(self, active: bool):
        """Sets the 'is_active' parameter to whatever the 'active' parameter eavluates to."""
        log.debug(f"Setting the {self.objectName()} from {self.is_active} to {active}.")
        self.is_active = active
        self.set_style()

class MinorLeftMenuButtons(QPushButton):
    def __init__(
        self,
        text: str="", 
        height: int=40, 
        minimum_width: int=40, 
        text_padding: int=45, 
        text_color: str=Color.BTN_TEXT, 
        icon_path: str="", 
        icon_color: str="black",
        btn_color: str=Color.MINOR_BTN_BG, 
        btn_hover: str=Color.MINOR_BTN_HOVER,
        btn_pressed :str=Color.MINOR_BTN_PRESSED,
        btn_active: str=Color.MINOR_BTN_ACTIVE,
        btn_active_border_right: str=Color.MINOR_BTN_ACTIVE,
        btn_active_border_left: str=Color.MINOR_BTN_ACTIVE,
        btn_active_border_bot: str=Color.MINOR_BTN_ACTIVE,
        btn_active_border_top: str=Color.MINOR_BTN_ACTIVE,
        is_active: bool= False
    ):
        super().__init__()

        # Set default parameters
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # Custom parameters
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.icon_path = icon_path
        self.text_color = text_color
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.btn_active = btn_active
        self.btn_active_border_left = btn_active_border_left
        self.btn_active_border_top = btn_active_border_top
        self.btn_active_border_right = btn_active_border_right
        self.btn_active_border_bot = btn_active_border_bot
        self.is_active = is_active

        # Set stylesheet according to what we've entered.
        self.set_style()

    def set_style(self):
        stylesheet_str = f"""
        QPushButton {{
            color: {self.text_color};
            background-color: {self.btn_color};
            padding-left: {self.text_padding}px;
            text-align: left;
            border: none;
            font: 75 10pt 'Segoe UI';
        }}

        QPushButton:hover {{
            background-color: {self.btn_hover};
        }}
        
        QPushButton:pressed {{
            background-color: {self.btn_pressed};
        }}
        """

        active_str =f"""
        QPushButton {{
            background-color: {self.btn_active};
            border-left: 5px solid {self.btn_active_border_left};
            border-top: 5px solid {self.btn_active_border_top};
            border-right: 5px solid {self.btn_active_border_right};
            border-bottom: 5px solid {self.btn_active_border_bot};
        }}
        """

        if not self.is_active:
            self.setStyleSheet(stylesheet_str)
        else:
            self.setStyleSheet(stylesheet_str + active_str)

    def paintEvent(self, event):
        """Custom paintEvent for this custom button."""
        # Painting button
        log.debug("Inside paint event")
        QPushButton.paintEvent(self, event)

        # Creating a QPainter object
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        # Creating a rectangle for reference for our icon
        rect = QRect(0, 0, self.minimum_width, self.minimumHeight())

        # Drawing the icon
        self.draw_icon(qp, self.icon_path, rect, self.icon_color)

        qp.end()

    def draw_icon(self, qp: QPainter, image: str, rect: QRect, color: str):
        # Formatting the path for the image
        app_path = os.path.abspath(os.getcwd())
        folder = 'gui/images/icons'
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))

        # Drawing the icon
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        
        # Drawing pixmap
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()

    def set_active(self, active: bool):
        """Sets the 'is_active' parameter to whatever the 'active' parameter eavluates to."""
        log.debug(f"Setting the {self.objectName()} from {self.is_active} to {active}.")
        self.is_active = active
        self.set_style()


class FormButton(QPushButton):
    def __init__(
        self,
        text: str="FormButton",
        height: int=Dimension.FORM_BUTTON_DEF_HEIGHT, 
        minimum_width: int=Dimension.FORM_BUTTON_DEF_WIDTH, 
        text_padding: int=10, 
        text_color: str=Color.FORM_BUTTON_TEXT,
        btn_color: str=Color.FORM_BUTTON_DEF_COLOR, 
        btn_hover: str=Color.FORM_BUTTON_DEF_HOVER,
        btn_pressed :str=Color.FORM_BUTTON_DEF_PRESSED,
    ):
        super().__init__()

        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # Taking the other needed parameters
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed

        self.set_style()

    
    def set_style(self):
        """Sets the stylesheet by the given parameters."""
        stylesheet_str = f"""
        QPushButton {{
            color: {self.text_color};
            background-color: {self.btn_color};
            padding-left: {self.text_padding}px;
            padding-right: {self.text_padding}px;
            text-align: center;
            border: 1px solid {self.btn_color};
            border-radius: {self.height() / 4 }px;
            font: 100 10pt 'Segoe UI';
        }}

        QPushButton:hover {{
            background-color: {self.btn_hover};
            border: 1px solid {self.btn_hover};
        }}
        
        QPushButton:pressed {{
            background-color: {self.btn_pressed};
        }}
        """
        self.setStyleSheet(stylesheet_str)