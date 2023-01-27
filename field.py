import sys
from PyQt5.QtWidgets import (
    QPushButton,
    QWidget,
    QApplication,
    QDesktopWidget,
    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,
    QLabel
    )
from PyQt5.QtCore import Qt
from Game import Generator

start_resolution = [600, 400]

class Field(QWidget):

    def __init__(self):
        super().__init__()
        self.field = Generator()
        self.top_bar_n = 3
        self.initUI()

    def initUI(self):
        self.resize(*start_resolution)

        self.gamefield_layout = QGridLayout()
        self.info_layout = QHBoxLayout()
        pagelayout = QVBoxLayout()
        
        pagelayout.addLayout(self.info_layout)
        pagelayout.addLayout(self.gamefield_layout)
        
        self.set_info_layout()
        self.set_gamelayout()
        self.setLayout(pagelayout)

        self.center_window()
        self.setWindowTitle("MineSweeper by ArturBV")
        self.show()

    def set_info_layout(self):
        # top_bar_positions = self.field.get_top_pos(self.top_bar_n)
        top_bar_widgets = [QLabel("Mines left: 0"), QLabel("^_^"), QLabel("TODO timer")]
        for widget in top_bar_widgets:
            widget.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
            self.info_layout.addWidget(widget)

    def set_gamelayout(self):
        # 3 for counter, smile and timer(?)

        btn_positions = [(i, j) for i in range(self.field.size) for j in range(self.field.size)]
        btn_widgets = [QPushButton(f"{i}", self) for i in range(self.field.size * self.field.size)]
        for btn, pos in zip(btn_widgets, btn_positions):
            btn.setMinimumSize(start_resolution[1] // self.field.size, start_resolution[1] // self.field.size)
            # btn.setMaximumSize(start_resolution[1] // self.field.size, start_resolution[1] // self.field.size)
            self.gamefield_layout.addWidget(btn, *pos)

    def center_window(self):
        w_frame = self.frameGeometry()
        desktop_center = QDesktopWidget().availableGeometry().center()
        w_frame.moveCenter(desktop_center)
        self.move(w_frame.topLeft())

class Button(QPushButton):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    print("Hello")
    app = QApplication(sys.argv)
    window = Field()
    sys.exit(app.exec_())
    print()