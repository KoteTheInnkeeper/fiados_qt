from gui.gui_constants import Dimension, Color
from qt_core import *


class FormCombobox(QComboBox):
    def __init__(
        self,
        width: int = Dimension.COMBOBOX_MIN_WIDTH,
        height: int = Dimension.COMBOBOX_MIN_HEIGHT,
        bg_color: str = Color.COMBOBOX_DEF_COLOR,
        bg_hover: str = Color.COMBOBOX_DEF_HOVER_COLOR,
        select_bg_color: str = Color.COMBOBOX_DEF_SELECT_BG_COLOR,
        select_text_color: str = Color.COMBOBOX_DEF_SELECT_TEXT_COLOR,
        visible: bool = False,
        enabled: bool = False,
        editable: bool = False
    ):
        super().__init__()

        self.setMinimumSize(QSize(width, height))

        # Saving the other parameters
        self.bg_color = bg_color
        self.bg_hover = bg_hover
        self.select_bg_color = select_bg_color
        self.select_text_color = select_text_color

        # Setting the enabled an visible parameters
        self.setEnabled(enabled)
        self.setVisible(visible)
        # Set the editable
        self.setEditable(editable)


        # Setting the style
        self.set_style()

        

    def set_style(self):
        """Set's a stylesheet"""
        stylesheet_str = f"""
        QComboBox {{
            background-color: {self.bg_color};
            selection-background-color: {self.select_bg_color};
            selection-color: {self.select_text_color};
        }}
        
        QComboBox:hover {{
          background-color: {self.bg_hover};  
        }}"""

        disabled_str = f"""
        QComboBox {{
            background-color: {Color.CONTENT_BACKGROUND};
            color: grey;
        }}
        """
        if self.isEnabled():
            self.setStyleSheet(stylesheet_str)
        else:
            self.setStyleSheet(stylesheet_str + disabled_str)
