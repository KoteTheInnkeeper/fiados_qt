from qt_core import *
from gui.gui_constants import *


class FormLineEdit(QLineEdit):
    def __init__(
        self,
        width: int=Dimension.LINE_EDIT_DEF_WIDTH,
        height: int=Dimension.LINE_EDIT_DEF_HEIGHT,
        bg_color: str = Color.LINE_EDIT_DEF_BG_COLOR,
        bg_hover: str = Color.LINE_EDIT_DEF_HOVER_COLOR,
        text_alignment: str = "left",
        visibility: bool=True
    ):
        super().__init__()

        self.width, self.height = width, height

        self.is_visible = visibility
        self.bg_color = bg_color
        self.bg_hover = bg_hover
        self.text_alignment = text_alignment
        self.setMinimumHeight(height)
        self.setMinimumWidth(width) 
        self.setMaximumWidth(width)
        self.setVisible(self.is_visible)

        # Applying the additional methods
        self.set_style()
        self.set_alignment()


    def set_alignment(self):
        """Sets the alignment according to the entered string for this parameter."""
        POSSIBLE_ALIGNMENTS = {
            "right": Qt.AlignRight,
            "center": Qt.AlignCenter,
            "left": Qt.AlignLeft
        }
        self.setAlignment(POSSIBLE_ALIGNMENTS[self.text_alignment])

    
    def set_style(self):
        """Sets a stylesheet"""
        stylesheet_str = f"""
        QLineEdit {{
            background-color: {self.bg_color};
        }}

        QLineEdit:hover {{
            background-color: {self.bg_hover};
        }}
        """

        self.setStyleSheet(stylesheet_str)

